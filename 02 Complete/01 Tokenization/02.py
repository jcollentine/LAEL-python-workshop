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

# Separate token and tag

# Traditional way
# - Create an empty list
# - loop through taggedTokens_ls
# - separate token and tag 
# - append to list

tokensAndTags_tup_ls = []
for token in taggedTokens_ls:
	tokensAndTags_tup_ls.append( nltk.tag.str2tuple( token ) )

# Modern way, using 'list comprehension'
# NEW VARIABLE = [ MODIFY EACH ITEM for LOOP THRU ITEMS  ]
tokensAndTags_tup_ls = [ nltk.tag.str2tuple( token ) for token in taggedTokens_ls ]
