# -*- coding: utf-8 -*-

import pandas
from scipy.stats import zscore

df = pandas.read_csv("05/data1.csv")

sub_df = df[ ["wordCount", "ttr", "ttr_100", "nouns", "verbs", "conjunctions", "pronouns"] ]
sub_df = sub_df.apply( zscore )


better_sub_df = df.apply(
	lambda column: zscore(column) 
	if column.name in ["wordCount", "nouns", "verbs", "conjunctions", "pronouns"]
	else column
)

better_sub_df.to_csv("05/data2.csv", index=False)