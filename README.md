# ACL 2020 Grand-Challenge and Workshop on Multimodal Language: CMU-MOSEI Start Page

To start with the challenge on CMU-MOSEI dataset, you have two options:

A. Use CMU Multimodal SDK (recommended)

B. Download the raw data and process it

## Option A: Using the CMU Multimodal SDK

First clone the CMU Multimodal SDK from https://github.com/A2Zadeh/CMU-MultimodalSDK. Install it using the short and easy installation steps in the SDK. We refer to the path to SDK as SDK\_PATH. Subsequently, clone this github repository. We will refer to the path to this repository as CHALHML\_PATH. Add both paths to your PYTHONPATH environment variable using:

```bash
export PYTHONPATH="SDK\_PATH:CHALHML\_PATH"
```

Example (do not use this directly, change the paths to yours): 

```bash
export PYTHONPATH="/usr/abagherz/CMU-MultimodalSDK:/usr/abagherz/ACL_Challenge_HML_20"
```

Subsequently run the SDK\_start/test\_sdk.py if you get the following message: "Welcome to ACL20 Challenge - HML CMU-MOSEI Subchallenge. SDK Works! "


Now, off to getting the data. We have provided a sample code that will do the job for you, simply run SDK\_start/dl\_cmumosei.py

This will download all the CMU-MOSEI train, validation and public test data for you. The file SDK\_start/folds\_cmumosei.py includes all the ids for the different folds. 

## Option B: Download Raw Data

The raw data is available here: http://immortal.multicomp.cs.cmu.edu/raw\_datasets/CMU\_MOSEI.zip

Private test data will be release on Feb 15th. 

## Contacting the organizers

You can reach us at challengehml20@gmail.com


