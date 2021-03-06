#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:26:56 2018

@author: loey
"""

import time
import sys
import csv
import re
csv.field_size_limit(sys.maxsize)
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
filenames = dict()

def main():
    start_time = time.time()
    with open('split/training_allFiles.csv', 'r') as csv_file_r:
        training_file = open('train_kenlm.txt', 'w')
        reader = csv.DictReader(csv_file_r)
        
        for r in reader:
            if r['filename'] not in filenames:
                filenames[r['filename']] = [r['filename']]
                print(r['filename'])
            
            training_file.write(r['text'] + "\n")
        training_file.close()
        csv_file_r.close()
    print("writeTrainingTxt_kenlm.py Run Time: " + str(time.time()-start_time) + " seconds")

main()