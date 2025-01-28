import pandas as pd

data = {
    "Tid" : [1,2,3,4,5,6,7,8,9,10],
    "Refund" : ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status" : ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income" : ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat" : ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df=pd.DataFrame(data)
print(df)

rows_3to7 = df.iloc[3:8]
print("\nRows from Index 3 to 7:")
print(rows_3to7)

rows_4to8_cols_2to4 = df.iloc[4:9,2:5]
print("\nRows from 4 to 8 and Columns from 2 to 4:")
print(rows_4to8_cols_2to4)

cols_1to3 = df.iloc[:,1:4]
print("\nColumns from 1 to 3:")
print(cols_1to3)