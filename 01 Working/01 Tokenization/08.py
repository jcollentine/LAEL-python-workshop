# -*- coding: utf-8 -*-

# Helpers.py should be in the same directory
from Helpers import *
import nltk  # NLP library
from nltk.util import ngrams
import csv

def countWords(tokens_ls):
	return len(tokens_ls)

def typeToken(tokens_ls):
	# get uniq tokens 
	try:
		unique_n = len( set( tokens_ls ) )
		total_n = countWords(tokens_ls)
		ttr_f = unique_n/total_n
	except:
		ttr_f = -99
	return ttr_f

def typeTokenFirstN(tokens_ls, n):
	try:
		tokens_ls = tokens_ls[0:n]
		unique_n = len( set( tokens_ls ) )
		total_n = countWords(tokens_ls)
		ttr_f = unique_n/total_n
	except:
		ttr_f = -99
	return ttr_f

def countTagByPrefix( tags_ls, prefix ):
	try:
		matches_ls = [
				i 
				for i in tags_ls
				if i.startswith( prefix )
			]
	except:
		matches_ls = []
	return len( matches_ls )


filePath = "subcorpus_mini/1.txt"

# Prepare text
# - Read
# - Delete headers
text = open( filePath, encoding="utf8" ).read()
text = filterTextLines( text, [ "^fileName:", "^folderPath:" ] )

# Get tokens
taggedTokens_ls = nltk.word_tokenize(text)

tokensAndTags_tup_ls = [ nltk.tag.str2tuple( token ) for token in taggedTokens_ls ]
tokensAndTags_tup_ls = [ i for i in tokensAndTags_tup_ls if i[0] not in punct_ls ]
tokensAndTags_tup_ls = [ i for i in tokensAndTags_tup_ls if i[1] not in ["",None] ]

# put tags and tokens in separate lists
# i = ("book","NNS"), ("send","VB")
tokens_ls = [ i[0] for i in tokensAndTags_tup_ls]
tags_ls = [ i[1] for i in tokensAndTags_tup_ls]

# Declare a dictionary
d = {}
d["ttr"] = typeTokenFirstN(tokens_ls, 100)
d["nouns"] = countTagByPrefix(tags_ls, "N")
d["verbs"] = countTagByPrefix(tags_ls, "V")
d["conjunctions"] = countTagByPrefix(tags_ls, "C")
d["pronouns"] = countTagByPrefix(tags_ls, "P")

with open('tabs.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows( d.items() )

