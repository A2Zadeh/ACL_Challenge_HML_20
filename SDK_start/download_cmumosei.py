import mmsdk
from mmsdk import mmdatasdk
import ChallengeHML20   
import numpy


def download_data(keys):
	print ("You only need to download the data once!")
	for key in keys:
		cmumosei_highlevel=mmdatasdk.mmdataset(ChallengeHML20.challenge20_data[key],'cmumosei/')

if __name__=="__main__":
	#download_data(["raw"])
	#to download everything, uncomment the following. The highlevel and raw features should be enough for the challenge.
	download_data(list(ChallengeHML20.challenge20_data.keys()))

