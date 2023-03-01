# -*- coding: utf-8 -*-

# Helpers.py should be in the same directory
from Helpers import *
import nltk  # NLP library

filePath = "subcorpus_mini/1.txt"

# Prepare text
# - Read
# - Delete headers
text = open( filePath, encoding="utf8" ).read()
text = filterTextLines( text, [ "^fileName:", "^folderPath:" ] )

# Get tokens
taggedTokens_ls = nltk.word_tokenize(text)

tokensAndTags_tup_ls = [ nltk.tag.str2tuple( token ) for token in taggedTokens_ls ]

# Eliminate punctuation
# Traditional way
tmp_ls = []
for i in tokensAndTags_tup_ls:
	# i = ("book","NNS"), (";",";")
	if i[0] not in punct_ls:
		tmp_ls.append( i )
tokensAndTags_tup_ls = tmp_ls

# Using list comprehension
tokensAndTags_tup_ls = [ 
	i 
	for i in tokensAndTags_tup_ls 
	if i[0] not in punct_ls
	]
