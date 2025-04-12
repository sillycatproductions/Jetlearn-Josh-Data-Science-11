import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('adult.csv')

data.columns = ['age', 'workclass','Id','education','educational-num','marital-status','occupation','relationship',
                'race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']

data.rename(columns = {'capital-gain': 'capital gain',
                       'capital-loss' : 'capital loss',
                       'hours-per-week' : 'hours per week',
                       'native-country' : 'native country',
                       'marital-status' : 'marital',
                       'educational-num' : 'educational num'}, inplace = True)

#gives mathematical values based off of numerical data
print(data.describe())

print(data.head())
print(data.info())

#checks if there are any special characters in the data (punctuation)
print(data.isin(['?']).sum(axis = 0))

#drops unwanted columns
data.drop(['educational num','age','hours per week','Id','capital gain','capital loss','native country'], axis = 1, inplace = True)

print(data.head())

#finds unique data
income = set(data['income'])
print(income)

#maps the data into numerical data using map function
data['income'] = data['income'].map({' <=50K': 0,' >50K': 1}).astype(int)

print(data.head(10))

#gender -----------
gender = set(data['gender'])
print(gender)

data['gender'] = data['gender'].map({' Male': 0,' Female': 1}).astype(int)

print(data.head(10))

data.groupby('gender').income.mean().plot(kind = 'bar')
plt.show()

#race -----------
race = set(data['race'])
print(race)

data['race'] = data['race'].map({' Asian-Pac-Islander': 0,' Other': 1, ' Black' : 2, ' White' : 3, ' Amer-Indian-Eskimo' : 4}).astype(int)
print(data.head(10))

data.groupby('race').income.mean().plot(kind = 'bar')
plt.show()