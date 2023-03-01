# -*- coding: utf-8 -*-

# Helpers.py should be in the same directory
from Helpers import *
import nltk
import csv
import glob
import pandas
import random

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

df = pandas.DataFrame( columns = ["fileName", "wordCount", "ttr"] )

files_ls = glob.glob( "subcorpus/*.txt" )
random.shuffle( files_ls )
files_ls = files_ls[0:10]


for filePath in files_ls:

	fileInfo_d = getFileInfo( filePath )
	fileName = fileInfo_d["fileName"]
	folderPath = fileInfo_d["folderPath"]
	
	text = open( filePath, encoding="utf8" ).read()
	text = filterTextLines( text, [ "^fileName:", "^folderPath:" ] )

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
	d["fileName"] = fileName
	d["wordCount"] = countWords( tokens_ls )
	d["ttr"] = typeToken( tokens_ls )
	
	df = df.append( d, ignore_index = True )

df.to_csv( "04/data1.csv", index=False )
