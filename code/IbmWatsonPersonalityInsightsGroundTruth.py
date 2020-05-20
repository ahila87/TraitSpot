
'''
Created on Jan 13, 2020

@author: ahila
# '''
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname
import json
import pandas as pd


filename = 'C:/univ/yelp_dataset/user0.txt'
filename2 = 'C:/univ/FinalProject/FinalDataSets/TargetUsers.csv'

df = pd.read_csv(filename2)
row=901
with open(join(dirname(__file__), filename), encoding="utf8") as file:
    for line in file:   
       # row =int(line[0])
        print(row)
        print (df.at[row,'user_id'])
        
        authenticator = IAMAuthenticator('CChsGRq6NTFcFfK7JRt9nspQR69qaVafGvxGEG0sj-dQ')
        personality_insights = PersonalityInsightsV3(
            version='2017-10-13',
            authenticator=authenticator
            )
    
        personality_insights.set_service_url('https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/14259103-3349-4af8-8fad-e44c161b0a59')
    
 
        review = personality_insights.profile(
            line.strip(),
            'application/json',
            content_type='text/plain',
            consumption_preferences=True,
            raw_scores=True
        ).get_result()
        
        
        review['user_id'] = df.at[row,'user_id']
       
        with open('output901-1053.json', 'a') as json_file:
            json.dump(review, json_file, indent = 2)
            json_file.write('\n\n\n')     
                    
        personality = json.dumps(review)
        dict = json.loads(personality)
        
         
        df.loc[row,'Openness'] = round((dict['personality'][0]['percentile']),5)
        df.loc[row,'Conscientiousness'] = round((dict['personality'][1]['percentile']),5)
        df.loc[row,'Extraversion'] = round((dict['personality'][2]['percentile']),5)
        df.loc[row,'Agreeableness'] = round((dict['personality'][3]['percentile']),5)
        df.loc[row,'Neuroticism'] = round((dict['personality'][4]['percentile']),5)
        df.loc[row,'Openness-raw'] = round((dict['personality'][0]['raw_score']),5)
        df.loc[row,'Conscientiousness-raw'] = round((dict['personality'][1]['raw_score']),5)
        df.loc[row,'Extraversion-raw'] = round((dict['personality'][2]['raw_score']),5)
        df.loc[row,'Agreeableness-raw'] = round((dict['personality'][3]['raw_score']),5)
        df.loc[row,'Neuroticism-raw'] = round((dict['personality'][4]['raw_score']),5)
        row=row+1
  
  
df.to_csv('TargetUsers901-1053')
