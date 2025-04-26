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

#relationship -------------

relation = set(data['relationship'])
print(relation)

data['relationship'] = data['relationship'].map({' Own-child': 0,' Unmarried': 1,' Other-relative': 2, ' Husband': 3,' Not-in-family': 4,' Wife': 5}).astype(int)
print(data.head(10))

data.groupby('relationship').income.mean().plot(kind = 'bar')
plt.show()

#occupation -------------

occup = set(data['occupation'])
print(occup)

data['occupation'] = data['occupation'].map({' Exec-managerial': 0, ' Farming-fishing': 1, ' Other-service': 2, ' Craft-repair': 3, ' Armed-Forces': 4, ' Prof-specialty': 5, ' ?': 6, ' Tech-support': 7, ' Priv-house-serv': 8, ' Machine-op-inspct': 9, ' Transport-moving': 10, ' Protective-serv': 11, ' Adm-clerical': 12, ' Handlers-cleaners': 13, ' Sales': 14}).astype(int)
print(data.head(10))

data.groupby('occupation').income.mean().plot(kind = 'bar')
plt.show()

#marital-status ------------

marit = set(data['marital'])
print(marit)

data['marital'] = data['marital'].map({' Married-AF-spouse': 0, ' Separated': 1, ' Divorced': 2, ' Widowed': 3, ' Never-married': 4, ' Married-civ-spouse': 5, ' Married-spouse-absent': 6}).astype(int)
print(data.head(10))

data.groupby('marital').income.mean().plot(kind = 'bar')
plt.show()

#education ------------

edu = set(data['education'])
print(edu)

data['education'] = data['education'].map({' Doctorate': 0, ' 10th': 1, ' 7th-8th': 2, ' 12th': 3, ' Bachelors': 4, ' Masters': 5, ' Prof-school': 6, ' Preschool': 7, ' Some-college': 8, ' Assoc-acdm': 9, ' 5th-6th': 10, ' 1st-4th': 11, ' HS-grad': 12, ' 11th': 13, ' Assoc-voc': 14, ' 9th': 15}).astype(int)
print(data.head(10))

data.groupby('education').income.mean().plot(kind = 'bar')
plt.show()

#workclass -------------

work = set(data['workclass'])
print(work)

data['workclass'] = data['workclass'].map({' Federal-gov': 0, ' Private': 1, ' Never-worked': 2, ' Without-pay': 3, ' Local-gov': 4, ' Self-emp-not-inc': 5, ' State-gov': 6, ' ?': 7, ' Self-emp-inc': 8}).astype(int)
print(data.head(10))

data.groupby('workclass').income.mean().plot(kind = 'bar')
plt.show()
