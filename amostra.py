import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def calc_sample(populacao, erro):
    aprox = (1/erro**2)
    amostra = round((populacao*aprox)/(populacao+aprox))
    return amostra

def simple_random_sample(df, amostra):
    return df.sample(n=amostra)

def stratified_sample(df, coluna, amostra):
    X_train, X_test, y_train, y_test = train_test_split(df.drop('{}'.format(coluna),axis=1),
    df['{}'.format(coluna)],stratify=df['{}'.format(coluna)],test_size=amostra)
    return df.loc[y_test.index,:]

def systematic_sample(df):
    semente = np.random.choice(10, 1)
    indices = np.arange(0,df.shape[0],semente)
    return df.loc[indices, :]
