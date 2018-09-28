# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:23:32 2017

@author: Gunnvant
"""

import pandas as pd
import numpy as np
import os

data_dir="E:\\Work\\Python\\PythonTrainings\\PythonMcKinsey\\Data\\demo_data"

os.chdir(data_dir)

data=pd.read_csv("Store.csv",encoding="latin")

## Data Manipulation tasks:
# Filtering data
# Selecting columns 
# Sorting data
# Adding new columns
# Group By aggregations
# Handling dates
# Handling text
# Treating Missing Values

print(data.shape)

print(data.head())

## How many transactions have happened in East Region (Filter)
data[data['Region']=='East'].shape
data[data['Region']=='East'].shape[0]

# A more elegant API
data.query("Region=='East'").shape

# What was the total quantity sold in region East?
data[data['Region']=='East'][['Region','Quantity']].head() #Column Selection
data[data['Region']=='East']['Quantity'].sum()

data.query("Region=='East'")['Quantity'].sum()

## Ordering data
# Who are the most valuable customers in South Region by Sales?
data[data['Region']=="South"].head(3)

data[data['Region']=="South"].sort_values("Sales",ascending=False).head()

# In the east region who are the most valuable customers, select their cust ids
data.query("Region=='East'").sort_values("Sales",ascending=False)['Customer ID'].head()

### Adding new columns
# KPI- Sales as %age of average sales

data['SalesbyAverage']=data['Sales']/data['Sales'].mean()

# Create a column on Cost

data['Cost']=data['Sales']-data['Profit']

## Read the data called starbucks_final.csv
# An ideal diet should contain optimum level of nutrients
# can you find out the names of the items on menu that contain:
    #Upto 450 calories
    #Upto 40 g protein
    #Upto 10 g fat
    #Upto 40 g Carbs
    #Upto 5 g fibre
# Give the names of items on menu that satisfy the above criteria but contain least carbs but maximum protien


### Groupby aggregations

# Average quantity sold in each region
data.groupby("Region",as_index=False).agg({'Quantity':np.mean})
data.groupby("Region",as_index=False).agg({'Quantity':'mean'})
#or
data.groupby("Region",as_index=False)['Quantity'].mean()
#or 
data.groupby("Region",as_index=False)['Quantity'].agg('mean')

# What is the average and total sales by region
data.groupby("Region",as_index=False).agg({'Sales':[np.mean,np.sum]})

data.groupby("Region",as_index=False)['Sales'].agg([np.mean,np.sum]).reset_index()

# Find segment wise total sales and maximum profits
data.groupby("Segment",as_index=False).agg({'Sales':np.sum,"Profit":np.max})

# Arrange by Profits
data.groupby("Segment",as_index=False).agg({'Sales':np.sum,"Profit":np.max}).sort_values("Profit",ascending=False)

### Work on python data manipulation 1.docx

### lambdas, apply and map

# Assume we want to apply a differential charge based on Shiping model, if shipping mode was first class, 100 should be deducted from Sales

def get_normal_sales(row):
    if row["Ship Mode"]=="First Class":
        return row["Sales"]-100
    else:
        return row["Sales"]
data["Sales_Normalised"]=data.apply(get_normal_sales,axis=1)

# Create a binned version of profit column with values > 5000 as one group and <= as the other


data["Profit"].map(lambda x: "Above 200" if x>200 else "Below 200")


### Working with datetime
data.dtypes
# How much time it takes to place an order and ship it

data["Order Date"]=pd.to_datetime(data["Order Date"])
data["Ship Date"]=pd.to_datetime(data["Ship Date"])

data["Duration"]=data["Ship Date"]-data["Order Date"]
data["Duration"].head()

## How many times has it taken more than 5 days from placing the order to shipping
data[data["Duration"]>'5 days'].shape[0]


## How many orders were made during each day of week
data["Week_Day"]=data["Order Date"].dt.weekday #Monday =0, Sunday =6
data.groupby("Week_Day").size()
#String manipulations
st=pd.read_csv("E:\Work\Python\Python Trainings\Python Advanced\Data\Strings.csv")

print st.head()

st['Income_M'].mean()

st['Income_M']=st['Income_M'].str.replace("Rs","")
print st.head()

st['Income_M']=st['Income_M'].str.replace("/-","")
print st.head()

st['Income_M'].mean()

st.Income_M=pd.to_numeric(st.Income_M)
st.Income_M.mean()


## Handling missing values
# Counting the number of missing values in each column
dat_m=pd.read_csv('F:\\Work\\Jigsaw Academy\\Credit Loan\\Credit.csv',na_values=['Missing',""])
# Number of missing values
dat_m.isnull().sum()

#Subsetting by missing values
dat_m[dat_m['MonthlyIncome'].isnull()]['DebtRatio']

#Replacing missing values
dat_m['age']=dat_m['age'].fillna(20)
