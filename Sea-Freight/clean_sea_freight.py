import pandas as pd

df = pd.read_csv('AtmoSync_Route_SeaFreight.csv')


print(df.head()) 
#getting to know my first few rows how they look

print(df.info()) 
#total columns with names and datatypes

print(df.shape) 
#total counts of rows and coloum (262, 18)
 
print(df.isnull().sum())
#total missing values we have in each column    

print(df.duplicated().sum())
#count of total missing values(5)
print(df[df.duplicated(keep=False)])
#dispalyed all the duplicates rows n columns and count 10x18)

print(df.describe())
#displyed all statistical calculations of numeric values
#ex : count,mean,std,min,max   

print(df['spoilage_status'].unique())
print(df['cargo_type'].unique())
print(df['transport_mode'].unique())
#finding the values present in column 
#helping to identify spelling mistakes, spacing, capitalization  