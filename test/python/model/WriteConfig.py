# CopyRight Shangxuan Wu @ Myriad of Things
# 03 Feb 2018

# This script is for writing a JSON file "test/resource/mockdata/config" for testing use.

import json, pdb

def generateMLPConfig():
    data = {
        'Type': 'MLP',
        'Layers': '10, 10, 10',
        }
    with open('../', 'w') as outfile:
        json.dump(data, outfile)
    print('Successfully dumped mockdata JSON file for MLP.')
    return

def generateNaiveBayesConfig():
    data = {
        'Type': 'Naive Bayes',
        }
    with open('../', 'w') as outfile:
        json.dump(data, outfile)
    print('Successfully dumped mockdata JSON file for Naive Bayes.')
    return