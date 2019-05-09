#!/usr/bin/perl
#├ badWeather
#│   ├ blizzard
#│   ├ skating
#│   ├ snowFall
#│   └ wetSnow
#├ baseline
#│   ├ highway
#│   ├ office
#│   ├ pedestrians
#│   └ PETS2006
#├ cameraJitter
#│   ├ badminton
#│   ├ boulevard
#│   ├ sidewalk
#│   └ traffic
#├ dynamicBackground
#│   ├ boats
#│   ├ canoe
#│   ├ fall
#│   ├ fountain01
#│   ├ fountain02
#│   └ overpass
#├ intermittentObjectMotion
#│   ├ abandonedBox
#│   ├ parking
#│   ├ sofa
#│   ├ streetLight
#│   ├ tramstop
#│   └ winterDriveway
#├ lowFramerate
#│   ├ port_0_17fps
#│   ├ tramCrossroad_1fps
#│   ├ tunnelExit_0_35fps
#│   └ turnpike_0_5fps
#├ nightVideos
#│   ├ bridgeEntry
#│   ├ busyBoulvard
#│   ├ fluidHighway
#│   ├ streetCornerAtNight
#│   ├ tramStation
#│   └ winterStreet
#├ PTZ
#│   ├ continuousPan
#│   ├ intermittentPan
#│   ├ twoPositionPTZCam
#│   └ zoomInZoomOut
#├ shadow
#│   ├ backdoor
#│   ├ bungalows
#│   ├ busStation
#│   ├ copyMachine
#│   ├ cubicle
#│   └ peopleInShade
#├ thermal
#│   ├ corridor
#│   ├ diningRoom
#│   ├ lakeSide
#│   ├ library
#│   └ park
#└ turbulence
#    ├ turbulence0
#	    ├ turbulence1
#		    ├ turbulence2
#			    └ turbulence3

#my @names=( "pepe");
my @names=( "AdaptiveBackgroundLearning", "AdaptiveSelectiveBackgroundLearning", "Amber", "CodeBook", "DPAdaptiveMedian", "DPEigenbackground", "DPGrimsonGMM", "DPMean", "DPPratiMediod", "DPTexture", "DPWrenGA", "DPZivkovicAGMM", "FrameDifference", "FuzzyChoquetIntegral", "FuzzySugenoIntegral", "GMG", "IndependentMultimodal", "KDE", "LBAdaptiveSOM", "LBFuzzyAdaptiveSOM", "LBFuzzyGaussian", "LBMixtureOfGaussians", "LBP_MRF", "LBSimpleGaussian", "LOBSTER", "MixtureOfGaussianV1", "MixtureOfGaussianV2", "MultiCue", "MultiLayer", "MyBGS", "PAWCS", "PixelBasedAdaptiveSegmenter", "SigmaDelta", "StaticFrameDifference", "SuBSENSE", "T2FGMM_UM", "T2FGMM_UV", "T2FMRF_UM", "T2FMRF_UV", "TwoPoints", "ViBe", "VuMeter", "WeightedMovingMean", "WeightedMovingVariance");

foreach my $name (@names) {
	my $dirname = $name."_result";
	mkdir $dirname;
	mkdir $dirname."/badWeather/";
	mkdir $dirname."/badWeather/blizzard";
	mkdir $dirname."/badWeather/skating";
	mkdir $dirname."/badWeather/snowFall";
	mkdir $dirname."/badWeather/wetSnow";
	mkdir $dirname."/baseline";
	mkdir $dirname."/baseline/highway";
	mkdir $dirname."/baseline/office";
	mkdir $dirname."/baseline/pedestrians";
	mkdir $dirname."/baseline/PETS2006";
	mkdir $dirname."/cameraJitter";
	mkdir $dirname."/cameraJitter/badminton";
	mkdir $dirname."/cameraJitter/boulevard";
	mkdir $dirname."/cameraJitter/sidewalk";
	mkdir $dirname."/cameraJitter/traffic";
	mkdir $dirname."/dynamicBackground";
	mkdir $dirname."/dynamicBackground/boats";
	mkdir $dirname."/dynamicBackground/canoe";
	mkdir $dirname."/dynamicBackground/fall";
	mkdir $dirname."/dynamicBackground/fountain01";
	mkdir $dirname."/dynamicBackground/fountain02";
	mkdir $dirname."/dynamicBackground/overpass";
	mkdir $dirname."/intermittentObjectMotion";
	mkdir $dirname."/intermittentObjectMotion/abandonedBox";
	mkdir $dirname."/intermittentObjectMotion/parking";
	mkdir $dirname."/intermittentObjectMotion/sofa";
	mkdir $dirname."/intermittentObjectMotion/streetLight";
	mkdir $dirname."/intermittentObjectMotion/tramstop";
	mkdir $dirname."/intermittentObjectMotion/winterDriveway";
	mkdir $dirname."/lowFramerate";
	mkdir $dirname."/lowFramerate/port_0_17fps";
	mkdir $dirname."/lowFramerate/tramCrossroad_1fps";
	mkdir $dirname."/lowFramerate/tunnelExit_0_35fps";
	mkdir $dirname."/lowFramerate/turnpike_0_5fps";
	mkdir $dirname."/nightVideos";
	mkdir $dirname."/nightVideos/bridgeEntry";
	mkdir $dirname."/nightVideos/busyBoulvard";
	mkdir $dirname."/nightVideos/fluidHighway";
	mkdir $dirname."/nightVideos/streetCornerAtNight";
	mkdir $dirname."/nightVideos/tramStation";
	mkdir $dirname."/nightVideos/winterStreet";
	mkdir $dirname."/PTZ";
	mkdir $dirname."/PTZ/continuousPan";
	mkdir $dirname."/PTZ/intermittentPan";
	mkdir $dirname."/PTZ/twoPositionPTZCam";
	mkdir $dirname."/PTZ/zoomInZoomOut";
	mkdir $dirname."/shadow";
	mkdir $dirname."/shadow/backdoor";
	mkdir $dirname."/shadow/bungalows";
	mkdir $dirname."/shadow/busStation";
	mkdir $dirname."/shadow/copyMachine";
	mkdir $dirname."/shadow/cubicle";
	mkdir $dirname."/shadow/peopleInShade";
	mkdir $dirname."/thermal";
	mkdir $dirname."/thermal/corridor";
	mkdir $dirname."/thermal/diningRoom";
	mkdir $dirname."/thermal/lakeSide";
	mkdir $dirname."/thermal/library";
	mkdir $dirname."/thermal/park";
	mkdir $dirname."/thermal/park";
	mkdir $dirname."/turbulence";
	mkdir $dirname."/turbulence/turbulence0";
	mkdir $dirname."/turbulence/turbulence1";
	mkdir $dirname."/turbulence/turbulence2";
	mkdir $dirname."/turbulence/turbulence3";
}
