import pandas as pd
data= pd.read_csv(r'C:\Pythoncode\Giants.csv')
df=(pd.DataFrame(data,columns=['id','age']))
print(df)
