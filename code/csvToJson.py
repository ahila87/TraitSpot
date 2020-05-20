'''
Created on Feb 20, 2020

@author: ahila
'''
# import csv
# import json
# 
# csvfile = open('AllReviews.csv', 'r')
# jsonfile = open('file.json', 'w')
# 
# fieldnames = ("user_id","combinedText")
# reader = csv.DictReader( csvfile, fieldnames)
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')

import pandas as pd
import csv
import json
df = pd.read_csv('AllReviews.csv', nrows=100)
jsonfile = open('AllReviews.json', 'w')
print(df)
# any operations on dataframe df
for row in df.itertuples():
    print(row)
    json.dump(row, jsonfile)
    jsonfile.write('\n')
