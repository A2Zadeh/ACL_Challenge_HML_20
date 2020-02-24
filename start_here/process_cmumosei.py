import mmsdk
from mmsdk import mmdatasdk
from mmsdk.mmdatasdk import log
import ChallengeHML20   
import numpy

def myavg(intervals,features):
        return numpy.average(features,axis=0)

def deploy(in_dataset,destination):
	deploy_files={x:x for x in in_dataset.keys()}
	in_dataset.deploy(destination,deploy_files)

def process_data(folders=["cmumosei_highlevel","cmumosei_labels"]):
	log.status("You only need to run this script once. CMU-MOSEI processing requires a combination of 300GB in RAM and swap combined. As optimized as the process is, it may take up to a day to finish.")
	log.status("Alternatively, you can send us your computational sequences to align for you if you don't have enough computational power for alignment.")
	log.status("The standard aligned features are availabel on the challenge github.")
	log.status("You can also download the data from here: http://immortal.multicomp.cs.cmu.edu/ACL20Challenge/")
	
	cmumosei_challenge_acl20={}
	for folder in folders:
		cmumosei_challenge_acl20[folder.split("_")[1]]=mmdatasdk.mmdataset(folder)
	
	#performs word alignment. Labels are not part of the word alignment process.
	cmumosei_challenge_acl20["highlevel"].align("glove_vectors")
	#replacing missing modality information for words - some words may experience failed COVAREP, etc.
	cmumosei_challenge_acl20["highlevel"].impute('glove_vectors')
	#this writes the word aligned computational sequences to the disk
	deploy(cmumosei_challenge_acl20["highlevel"],"word_aligned_highlevel")
	#if you want to load the word aligned from the disk, comment out the lines for align and impute, and uncomment the line below.
	#cmumosei_challenge_acl20["highlevel"]=mmdatasdk.mmdataset("word_aligned_highlevel")

	#now aligning to the labels - first adding labels to the dataset
	cmumosei_challenge_acl20["highlevel"].computational_sequences["All Labels"]=cmumosei_challenge_acl20["labels"]["All Labels"]
	#the actual alignment without collapse function this time
	cmumosei_challenge_acl20["highlevel"].align("All Labels")
	#removing sentences which have missing modality information
	cmumosei_challenge_acl20["highlevel"].hard_unify()

	#writing the final aligned to disk
	deploy(cmumosei_challenge_acl20["highlevel"],"final_aligned")

	#reading from the disk - if the above process is done. 
	#cmumosei_challenge_acl20["highlevel"]=mmdatasdk.mmdataset("final_aligned")

	#getting the final tensors for machine learning - pass the folds to this function to get data based on tr,va,te folds.
	tensors=cmumosei_challenge_acl20["highlevel"].get_tensors(seq_len=50,non_sequences=["All Labels"],direction=False,folds=[mmdatasdk.cmu_mosei.standard_folds.standard_train_fold,mmdatasdk.cmu_mosei.standard_folds.standard_valid_fold,mmdatasdk.cmu_mosei.standard_folds.standard_test_fold])

	fold_names=["train","valid","test"]

	for i in range(3):	
		#output the shape of the tensors
		for csd in list(cmumosei_challenge_acl20["highlevel"].keys()):
			print ("Shape of the %s computational sequence for %s fold is %s"%(csd,fold_names[i],tensors[i][csd].shape))

if __name__=="__main__":
	cmumosei_challenge_20=process_data()
	log.success("Dataset processed")


