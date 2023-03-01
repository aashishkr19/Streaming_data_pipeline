import pandas as pd
data=pd.read_csv("/home/aashish/Desktop/StreamData/Sample-Spreadsheet-10-rows.csv")
df2 = data.to_dict('records')
print(df2)