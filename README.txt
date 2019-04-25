This Python code is provided to help you process the videos of the
changedetection.net dataset and gather statistics

1)	Download the dataset and unzip all the files in the same folder. ex :
"c:\dataset"
	You should get this :
		c:\dataset\baseline\highway\input\
		c:\dataset\baseline\highway\groundtruth\
		c:\dataset\baseline\...
		c:\dataset\...
		c:\dataset\thermal\...

	*** Please do not change or put anything else in the "dataset" folder ***


	On the same level as dataset\, there is a 'results' folder filled with the
proper folder hierarchy.  These folders are all empty and will contain your
results.


2A)	If you already have an executable for your motion detection method and
would like to run it on every video, search for the 'TODO' in
'processFolder.py' and set the path to your executable.
	The first two arguments of your executable must be
	- path to video. ex : "C:\dataset\baseline\highway"
	- path to save the binary images. ex : "C:\results\baseline\highway"

2B)	If on the other hand you need to code your method, than follow these
steps :

	The code in the "c++ code" folder is an OpenCV*-based template that may
help you code your method.
	Put your code in 'YourMethod.h' and use the methods defined in
'YourMethod.cpp'

	* OpenCV is a free library of programming functions for real time computer
vision.  You can download it at http://sourceforge.net/projects/opencvlibrary/


3)      If you want the Python code to produce a stat file, uncomment the
line ending with '#STATS' in the 'processFolder' function.
	The stat file contains the number of TruePositive, FalseNegative,
FalsePositive, TrueNegative and number of missed shadow for all videos,
categories and overall.
	You can use the stat file to find the best set of parameters for your
method.

4)	Call "processFolder.py datasetPath binaryRootPath"

	ex :  "python processFolder C:\dataset C:\results"

5)	Once you are ready, zip the 'results' folder and fill out the form on the
changedetection.net Upload page.

	*** Please, use only zip for compression, we support no other compression
format. tar, gz, 7z, etc. are not supported  ****

	*** This code calculates 7 metrics, namely (1)Recall, (2)Specificity, (3)FPR, (4)FNR, (5)PBC, (6)Precision, (7)FMeasure. The metric "FPR-S" is only calcualated for "Shadow" category on the server side, but not in this code. If it's really necessary, 

FPR_S = float(nbShadowError) / nbShadow

where nbShadowError is the number in the last column in the 'cm' file you get, that is the number of times a pixel is labeled as shadow in GT but detected as moving object. nbShadow is the total number of pixel labeled as shadow in GT for a video or category.****

	***Please notice that in the metrics you calculate may different from the ones that are going to be shown on changedetection.net, since only half of the ground truth is available to calculate locally with this code, while the changedetection.net calculates metrics based on all the ground truth.***