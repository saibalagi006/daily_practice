import pandas as pd
import numpy as np 
import os 
from sklearn.linear_model import LinearRegression
import pickle

def model_build():
    path = "C:\\Users\\balagis\\Desktop\\Personal\\github\\10232022"
    os.chdir(path)
    df = pd.read_csv('housing.csv')
    df.fillna(0,inplace=True)
    df = df[['housing_median_age','total_rooms','total_bedrooms','median_house_value']]
    #print(df.head())
    X = df[['housing_median_age','total_rooms','total_bedrooms']]
    y = df[['median_house_value']]

    regressor = LinearRegression()
    regressor.fit(X,y)
    ### saving model to disk
    pickle.dump(regressor, open('model.pkl','wb'))

if __name__=="__main__":
    model_build()
    