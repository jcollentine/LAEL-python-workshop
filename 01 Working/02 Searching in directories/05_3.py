# -*- coding: utf-8 -*-

# Helpers.py should be in the same directory
from Helpers import *
import pandas
from scipy.stats import zscore
import numpy

df = pandas.read_csv("05/data1.csv")

df = df.apply(
	lambda column: zscore(column) 
	if column.name in ["wordCount", "nouns" ]
	else column
)

df = df.apply(
	lambda column: numpy.log10(column) 
	if column.name in [ "verbs", "conjunctions", "pronouns" ]
	else column
)

df = df.apply(
	lambda column: regexReplaceIt(column, "\.txt", "") 
	if column.name in [ "fileName" ]
	else column
)


df.to_csv("05/data3.csv", index=False)