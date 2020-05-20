'''
Created on Feb 21, 2020

@author: ahila
'''

import pandas as pd
import matplotlib.pyplot as plt
file = "C:/univ/FinalProject/FinalDataSets/TargetUsersWithGroundTruthValues -DataSet0.csv"
df = pd.read_csv(file)
hist = df.hist(column='Neuroticism-raw')
plt.xlabel("Percentile")
plt.ylabel("Frequency")
plt.savefig("Neuroticism-raw.png")