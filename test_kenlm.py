#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:03:27 2018

@author: loey
"""

import time
import kenlm
import sys
import csv
csv.field_size_limit(sys.maxsize)
from nltk.tokenize import RegexpTokenizer
filenames = dict()
start_time = time.time()
model = kenlm.LanguageModel('lm/reddit.binary')
#sentence = 'this is a sentence .'
#print(model.score(sentence))
model_train_end_time = time.time()
model_train_time = model_train_end_time - start_time

with open('../../Ummm/postExtract/sample_testing_allFiles.csv', 'r') as csv_file_r:
	csv_file_w = open('../../Ummm/umm_kenlm_output.csv', 'w')
	reader = csv.DictReader(csv_file_r)
	fieldnames = ['filename', 'author', 'subreddit', 'title', 'lexicalType', 'lexicalItem', 'lexicalLength', 'text', 'sentLength', 'timestamp', 'kenlm_output']
	writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
	writer.writeheader()

	for r in reader:
		if r['filename'] not in filenames:
			filenames[r['filename']] = [r['filename']]
			print(r['filename'])

		score = model.score(r['text'])
		writer.writerow({'filename':r['filename'], 'author':r['author'], 'subreddit':r['subreddit'], 'title':r['title'], 'lexicalType':r['lexicalType'], 'lexicalItem':r['lexicalItem'], 'lexicalLength':r['lexicalLength'], 'text':r['text'], 'sentLength':r['sentLength'], 'timestamp':r['timestamp'], 'kenlm_output':score})
	csv_file_w.close()
	csv_file_r.close()
print("Model Run Time: " + str(model_train_time) + " seconds")
print("Remaining Run Time: " + str(time.time()-model_train_end_time) + " seconds")
