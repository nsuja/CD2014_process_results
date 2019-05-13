#!/usr/bin/python
# -*- coding: utf-8 -*-

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Nil Goyette
# University of Sherbrooke
# Sherbrooke, Quebec, Canada. April 2012

"""Please notice that in the metrics you calculate may different from the ones 
that are going to be shown on changedetection.net, since only half of the 
ground truth is available to calculate locally with this code, while the 
changedetection.net calculates metrics based on all the ground truth."""

import os
import shutil
import subprocess
import sys
import threading
import time
import queue

from Stats import Stats

jobs_queue = queue.Queue()
threads = []
max_threads = os.cpu_count()
categories_checkbox = {}
stats_hash = {}
stats_lock = threading.Lock()

call = subprocess.call

def job(videoPath, binaryPath, category, video, algorithm):
    print('['+str(threading.get_ident())+'] Running: '+algorithm+' '+category+' '+video)
    processVideoFolder(videoPath, binaryPath, algorithm)
    confusionMatrix = compareWithGroungtruth(videoPath, binaryPath)  #STATS
    stats_lock.acquire()
    try:
        stats_hash[algorithm].update(category, video, confusionMatrix)  #STATS
    finally:
        stats_lock.release()
        print('['+str(threading.get_ident())+'] End')


def main():    
    datasetPath = sys.argv[1]
    binaryRootPath = sys.argv[2]
    #TODO FIXME XXX Validate args
    #algorithm = sys.argv[3]
    
    if not isValidRootFolder(datasetPath):
        print('The folder ' + datasetPath + ' is not a valid root folder.');
        return
    
    if os.path.exists(binaryRootPath):
        print('The folder ' + binaryRootPath + ' has been cleaned.');
        shutil.rmtree(binaryRootPath)
    os.mkdir(binaryRootPath)

    #categories_subset = set(['baseline','dynamicBackground','badWeather','cameraJitter','intermittentObjectMotion','lowFramerate','nightVideos','PTZ','shadow','thermal','turbulence']);
    categories_subset = set(['baseline','dynamicBackground'])
    for cat in categories_subset:
        categories_checkbox[cat] = False
    #algorithms_subset = set(['FrameDifference','SuBSENSE','LOBSTER','IndependentMultimodal'])
    algorithms_subset = set(['FrameDifference','StaticFrameDifference'])
    #algorithms_subset = set(['SuBSENSE'])
    
    for algorithm in algorithms_subset:
        print('---- Adding: ' + algorithm)
        processFolder(datasetPath, binaryRootPath, algorithm, categories_subset)

    last_category = ''
    last_algorithm = ''
    while(1):
        try:
            print('Saco')
            job_args = jobs_queue.get(False)
        except queue.Empty:
            #Termine
            print('Terminee')
            for th in threads:
                th.join()
            stats_hash[last_algorithm].writeCategoryResult(last_category)  #STATS
            categories_checkbox[last_category] = True
            done = True
            for cat in categories_subset:
                if(categories_checkbox[cat] != True):
                    done = False
                    break
            if(done == True):
                #Termine con todas las categorias
                print('----')
                print('---- Fin: ' + last_algorithm + ' Escribiendo resultados')
                print('----')
                stats_hash[last_algorithm].writeOverallResults()  #STATS

            break
        else:
            print('hay')
            category = job_args[2]
            algorithm = job_args[4]
            while(len(threads) >= max_threads):
                for th in threads:
                    th.join(0.1)
                    if(th.is_alive()):
                        #timeout
                        continue
                    else:
                        threads.remove(th)
                        print('Termino thread')
                time.sleep(1)
            if(last_category != '' and last_category != category):
                #Tengo que esperar que todo termine
                print('Cambio de categoria:: Last: '+last_category+' next: '+category)
                for th in threads:
                    th.join()
                stats_hash[last_algorithm].writeCategoryResult(last_category)  #STATS
                categories_checkbox[last_category] = True
                done = True
                for cat in categories_subset:
                    if(categories_checkbox[cat] != True):
                        done = False
                        break
                if(done == True):
                    #Termine con todas las categorias
                    print('----')
                    print('---- Fin: ' + last_algorithm + ' Escribiendo resultados')
                    print('----')
                    stats_hash[last_algorithm].writeOverallResults()  #STATS
                    for cat in categories_subset:
                        categories_checkbox[cat] = False
            last_category = category
            last_algorithm = algorithm
            x = threading.Thread(target=job, args=(job_args))
            print(job_args)
            threads.append(x)
            x.start()
            print(x.ident)
            print('Thread ' + str(x.ident) + ':: Args: ' + str(job_args))



def processFolder(datasetPath, binaryRootPath, algorithm, categories_subset):
    """Call your executable for all sequences in all categories."""
    algo_path = algorithm + "_result"
    os.mkdir(os.path.join(binaryRootPath, algo_path))
    stats = Stats(datasetPath, os.path.join(binaryRootPath, algo_path))  #STATS
    stats_hash[algorithm] = stats;
    for category in getDirectories(datasetPath):
        if not category in categories_subset:
            #print('---- Category: ' + category + ' not in subset... ignoring')
            continue
        stats.addCategories(category)  #STATS
        
        categoryPath = os.path.join(datasetPath, category)
        os.mkdir(os.path.join(binaryRootPath, algo_path, category))
        print('rootpath ' + binaryRootPath)
        
        for video in getDirectories(categoryPath):
            videoPath = os.path.join(categoryPath, video)
            binaryPath = os.path.join(binaryRootPath, algo_path, category, video)
            print('binarypath ' + binaryPath)
            if isValidVideoFolder(videoPath):
                args = [videoPath, binaryPath, category, video, algorithm]
                jobs_queue.put(args)
                #processVideoFolder(videoPath, binaryPath, algorithm)
                #confusionMatrix = compareWithGroungtruth(videoPath, binaryPath)  #STATS
                #stats.update(category, video, confusionMatrix)  #STATS

        #stats.writeCategoryResult(category)  #STATS
    print('---- Fin: ' + algorithm + ' Escribiendo resultados')
    #stats.writeOverallResults()  #STATS

def processVideoFolder(videoPath, binaryPath, algorithm):
    """Call your executable on a particular sequence."""
    os.mkdir(binaryPath);
    print(videoPath)
    print(binaryPath)
    retcode = call(['/home/ubuntu/sandbox/frame_difference/build/FrameDifferenceTest', videoPath, binaryPath, algorithm], shell=False)

def compareWithGroungtruth(videoPath, binaryPath):
    """Compare your binaries with the groundtruth and return the confusion matrix"""
    statFilePath = os.path.join(binaryPath, 'stats.txt')
    deleteIfExists(statFilePath)

    retcode = call([os.path.join('exe', 'comparator'),
                    videoPath, binaryPath],
                   shell=False)
    
    return readCMFile(statFilePath)

def readCMFile(filePath):
    """Read the file, so we can compute stats for video, category and overall."""
    if not os.path.exists(filePath):
        print("The file " + filePath + " doesn't exist.\nIt means there was an error calling the comparator.")
        raise Exception('error')
	
    with open(filePath) as f:
        for line in f.readlines():
            if line.startswith('cm:'):
                numbers = line.split()[1:]
                return [int(nb) for nb in numbers[:5]]





def isValidRootFolder(path):
    """A valid root folder must have the six categories"""
    categories = set(['dynamicBackground', 'baseline', 'cameraJitter', 'intermittentObjectMotion', 'shadow', 'thermal', 'badWeather', 'lowFramerate', 'nightVideos', 'PTZ', 'turbulence'])
    folders = set(getDirectories(path))
    return len(categories.intersection(folders)) == 11

def isValidVideoFolder(path):
    """A valid video folder must have \\groundtruth, \\input, ROI.bmp, temporalROI.txt"""
    return os.path.exists(os.path.join(path, 'groundtruth')) and os.path.exists(os.path.join(path, 'input')) and os.path.exists(os.path.join(path, 'ROI.bmp')) and os.path.exists(os.path.join(path, 'temporalROI.txt'))

def getDirectories(path):
    """Return a list of directories name on the specifed path"""
    return [file for file in os.listdir(path)
            if os.path.isdir(os.path.join(path, file))]

def deleteIfExists(path):
    if os.path.exists(path):
        os.remove(path)


if __name__ == "__main__":
    main()
