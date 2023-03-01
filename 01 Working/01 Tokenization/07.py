# -*- coding: utf-8 -*-

# Helpers.py should be in the same directory
from Helpers import *
import nltk  # NLP library
from nltk.util import ngrams
import json
import csv

def countWords(tokens_ls):
	return len(tokens_ls)

def typeToken(tokens_ls):
	# get uniq tokens 
	unique_n = len( set( tokens_ls ) )
	total_n = countWords(tokens_ls)
	return unique_n/total_n

def typeTokenFirstN(tokens_ls, n):
	# get first n
	tokens_ls = tokens_ls[0:n]
	# get uniq tokens 
	unique_n = len( set( tokens_ls ) )
	total_n = countWords(tokens_ls)
	return unique_n/total_n


def countTagByPrefix( tags_ls, prefix ):
	matches_ls = [
			i 
			for i in tags_ls
			if i.startswith( prefix )
		]
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

ttr = typeTokenFirstN(tokens_ls, 100)
nouns = countTagByPrefix(tags_ls, "N")
verbs = countTagByPrefix(tags_ls, "V")
conjunctions = countTagByPrefix(tags_ls, "C")
pronouns = countTagByPrefix(tags_ls, "P")