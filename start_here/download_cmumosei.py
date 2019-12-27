import mmsdk
from mmsdk import mmdatasdk
from mmsdk.mmdatasdk import log
import ChallengeHML20   
import numpy


def download_data(keys):
	print ("You only need to download the data once!")
	cmumosei_challenge_acl20={}
	for key in keys:
		cmumosei_challenge_acl20[key]=mmdatasdk.mmdataset(ChallengeHML20.challenge20_data[key],'cmumosei_%s/'%key)
		cmumosei_challenge_acl20
	return cmumosei_challenge_acl20

if __name__=="__main__":
	#download_data(["raw"])
	#to download everything, uncomment the following. The highlevel and raw features should be enough for the challenge.
	cmumosei_challenge_20=download_data(list(ChallengeHML20.challenge20_data.keys()))
	log.success("Dataset downloaded")






