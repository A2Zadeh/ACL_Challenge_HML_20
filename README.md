# COVID-19 UPDATE:

We hope everyone and their loved ones are staying safe during the COVID-19 pandemic.

**||Extension||**  We understand that quarantine is now in effect in many countries around the world, and that has taken a heavy toll on the speed of scientific research. Most of these days have been overlapping with the preparation days for this workshop. Due to this, and to allow fairness in submissions, we are extending all the deadlines by at least 3 weeks (deadlines hour still end of the day everywhere on earth). We hope this extension makes up for the lost time during the pandemic. The new deadlines are shown in http://multicomp.cs.cmu.edu/acl2020multimodalworkshop/.

**||Online||** As for the workshop day (July 10th 2020), we follow the same policy as the ACL 2020. We will hold the workshop online, and a zoom link will be announced here. The workshop is open to everyone without the need for conference registration.  The workshop will start at 9:00 a.m PDT (Seattle time).

# Welcome to ACL 2020 Grand-Challenge and Workshop on Multimodal Language Github page
This github will guide you through the process of participating in the grand-challenge for both CMU-MOSEI and MELD datasets. First, a quick recap of the datasets:

CMU-MOSEI: CMU Multimodal Opinion Sentiment and Emotion Intensity (CMU-MOSEI) dataset is the largest dataset of multimodal sentiment analysis and emotion recognition to date. The dataset contains nearly 23,500 sentence utterance videos from more than 1000 online YouTube speakers across 250 topics. The dataset is gender balanced. All the sentences utterance are randomly chosen from various topics and monologue videos. The videos are transcribed and properly punctuated. We strongly suggest participants use CMU Multimodal SDK for working with CMU-MOSEI. The winning team of CMU-MOSEI track will receive a certificate of achievement and a gift of  at least $1,000 USD in value.

MELD: Multimodal Emotion Lines Dataset (MELD) has been created by enhancing and extending EmotionLines dataset. MELD contains the same dialogue instances available in EmotionLines, but it also encompasses audio and visual modality along with text. MELD has more than 1400 dialogues and 13000 utterances from Friends TV series. Multiple speakers participated in the dialogues. Each utterance in a dialogue has been labeled by any of these seven emotions -- Anger, Disgust, Sadness, Joy, Neutral, Surprise and Fear. MELD also has sentiment (positive, negative and neutral) annotation for each utterance. The winning team of MELD will recieve a certificate of achievement. No private test-set will be released for MELD dataset.

This starting page is split into two parts: 1) CMU-MOSEI, 2) MELD. To particicpate in the grand-challenge, you can participate in either or both of the datasets. 

# Begin with CMU-MOSEI 

To start with the challenge on CMU-MOSEI dataset, you have two options:

A. Use CMU Multimodal SDK (recommended)

B. Download the raw data and process it

NOTE: When you are ready for the challenge test set, you have to contact the challenge organizers to get the intervals of sentences in the test set. You also have to fill the file Challenge_HML_PA.pdf and send it to orgainzers. 

## Option A: Using the CMU Multimodal SDK

First clone the CMU Multimodal SDK from https://github.com/A2Zadeh/CMU-MultimodalSDK. Install it using the short and easy installation steps in the MMSDK. We refer to the path to MMSDK as MMSDK\_PATH. Subsequently, clone this github repository. We will refer to the path to this repository as CHALHML\_PATH. Add both paths to your PYTHONPATH environment variable using:

```bash
export PYTHONPATH="MMSDK_PATH:CHALHML_PATH/ChallengeSDK"
```

Example if you have copied both to  /usr/some\_dope\_username/acl20challenge/ (do not use this directly, change the paths to yours): 

```bash
export PYTHONPATH="/usr/some_dope_username/acl20challenge/CMU-MultimodalSDK:/usr/some_dope_username/acl20challenge/git_challenge/ChallengeSDK/"
```

Subsequently run the start\_here/test\_sdk.py if you get the following message: 

```bash
Welcome to ACL20 Challenge - HML CMU-MOSEI Subchallenge. SDK Works! 
```

Now, off to getting the data. We have provided a sample code that will do the job for you, simply run 

```bash
CHALHML_PATH/start_here/download_cmumosei.py
```

This will download all the CMU-MOSEI train, validation and public test data for you. **note: public test data is not the same as private test data**. The process will also create "cmumosei_highlevel" and "cmumosei_labels" folders. Inside, there will be computational sequence data (csd) files containing the features and labels of CMU-MOSEI respectively. 

After download is finished, simply run the process_cmumosei to start the word alignment of the CMU-MOSEI. 

```bash
CHALHML_PATH/start_here/process_cmumosei.py
```

The above will first do word alignment. Once the word alignment is done, it will create "word_aligned_highlevel" folder with word aligned csd files. Subsequently, the code aligns everything to labels and creates "final_aligned" folder. since processing CMU-MOSEI is computationally heavy, we also provide these folders for download here, identical to what you would get if you ran the above command locally: http://immortal.multicomp.cs.cmu.edu/ACL20Challenge/


## Option B: Download Raw Data

This option is not recommended since multimodal data processing can be cumbersome, specially for CMU-MOSEI. However, if you decided to take this path, the raw data is available here: http://immortal.multicomp.cs.cmu.edu/raw\_datasets/CMU\_MOSEI.zip

Private test data will be release on Feb 15th.  

# Begin with MELD

MELD is not yet a part of CMU Multimodal SDK. Therefore, it is up to the participants to process the dataset (e.g. word alignment). You can find the starting page of MELD here: https://github.com/SenticNet/MELD

# Contacting the organizers

Have questions? You can reach us at challengehml20@gmail.com


