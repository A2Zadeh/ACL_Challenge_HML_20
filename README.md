# Welcome to ACL 2020 Grand-Challenge and Workshop on Multimodal Language Github page
This github will guide you through the process of participating in the grand-challenge for both CMU-MOSEI and MELD datasets. First, a quick recap of the datasets:

CMU-MOSEI: CMU Multimodal Opinion Sentiment and Emotion Intensity (CMU-MOSEI) dataset is the largest dataset of multimodal sentiment analysis and emotion recognition to date. The dataset contains nearly 23,500 sentence utterance videos from more than 1000 online YouTube speakers across 250 topics. The dataset is gender balanced. All the sentences utterance are randomly chosen from various topics and monologue videos. The videos are transcribed and properly punctuated. We strongly suggest participants use CMU Multimodal SDK for working with CMU-MOSEI. The winning team of CMU-MOSEI track will receive a certificate of achievement and a gift of  at least $1,000 USD in value.

MELD: Multimodal Emotion Lines Dataset (MELD) has been created by enhancing and extending EmotionLines dataset. MELD contains the same dialogue instances available in EmotionLines, but it also encompasses audio and visual modality along with text. MELD has more than 1400 dialogues and 13000 utterances from Friends TV series. Multiple speakers participated in the dialogues. Each utterance in a dialogue has been labeled by any of these seven emotions -- Anger, Disgust, Sadness, Joy, Neutral, Surprise and Fear. MELD also has sentiment (positive, negative and neutral) annotation for each utterance. The winning team of MELD will recieve a certificate of achievement. No private test-set will be released for MELD dataset.

This starting page is split into two parts: 1) CMU-MOSEI, 2) MELD. To particicpate in the grand-challenge, you can participate in either or both of the datasets. 

# Begin with CMU-MOSEI 

To start with the challenge on CMU-MOSEI dataset, you have two options:

A. Use CMU Multimodal SDK (recommended)

B. Download the raw data and process it

## Option A: Using the CMU Multimodal SDK

First clone the CMU Multimodal SDK from https://github.com/A2Zadeh/CMU-MultimodalSDK. Install it using the short and easy installation steps in the SDK. We refer to the path to SDK as SDK\_PATH. Subsequently, clone this github repository. We will refer to the path to this repository as CHALHML\_PATH. Add both paths to your PYTHONPATH environment variable using:

```bash
export PYTHONPATH="SDK\_PATH:CHALHML\_PATH\ChallengeSDK"
```

Example if you have copied both to  /usr/some\_dope\_username/acl20challenge/ (do not use this directly, change the paths to yours): 

```bash
export PYTHONPATH="/usr/some_dope_username/acl20challenge/CMU-MultimodalSDK:/usr/some_dope_username/acl20challenge/git_challenge/ChallengeSDK/"
```

Subsequently run the start\_here/test\_sdk.py if you get the following message: "Welcome to ACL20 Challenge - HML CMU-MOSEI Subchallenge. SDK Works! "

Now, off to getting the data. We have provided a sample code that will do the job for you, simply run SDK\_start/dl\_cmumosei.py

This will download all the CMU-MOSEI train, validation and public test data for you. The file SDK\_start/folds\_cmumosei.py includes all the ids for the different folds used in the challenge. Note the private test will be released on Feb 15th.  

## Option B: Download Raw Data

This option is not recommended since multimodal data processing can be cumbersome. However, if you decided to take this path, the raw data is available here: http://immortal.multicomp.cs.cmu.edu/raw\_datasets/CMU\_MOSEI.zip

Private test data will be release on Feb 15th.  


# MELD

MELD is not yet a part of CMU Multimodal SDK. Therefore, it is up to the participants to process the dataset (e.g. word alignment). You can find the starting page of MELD here: https://github.com/SenticNet/MELD

# Contacting the organizers

Have questions? You can reach us at challengehml20@gmail.com


