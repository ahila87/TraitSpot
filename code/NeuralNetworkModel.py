'''
Created on Mar 8, 2020

@author: ahila
'''
import numpy as np
import pandas as pd


import sklearn.feature_extraction.text as sk_text
file_path='C:/univ/FinalProject/FinalDataSets/DataSet3_200Users.csv'
df = pd.read_csv(file_path)
file_path1="C:/univ/FinalProject/FinalDataSets/DataSet0 -200Users.csv"
df1 = pd.read_csv(file_path1)
text = df.text


vectorizer = sk_text.TfidfVectorizer(
                             #min_df=1
							 )

tfidf_mat = vectorizer.fit_transform(text).toarray()
print(type(tfidf_mat),tfidf_mat.shape)
print(tfidf_mat)
vectorizer.get_feature_names()



from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
import statistics
RMSE = []
y = np.asarray(df1['Agreeableness'])
for i in range(0, 10):
    X_train, X_test, y_train, y_test = train_test_split(tfidf_mat, y, test_size=0.2)
    mlp = MLPRegressor(hidden_layer_sizes=(1000,200,100), max_iter=5000, early_stopping=True)
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)    
    z = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    RMSE.append(z)
    
print(RMSE)
print ("mean =  "+str(statistics.mean(RMSE) ))
print ("variance =  "+str(statistics.variance(RMSE)))
