import pandas as pd
df = pd.read_excel('sample.xlsx')
df['LinePrice'] = df['Quantity']*df['UnitPrice']
df.head()
print(df)
df_customers = df.groupby('customer').agg(
    orders=('InvoiceNo', 'nunique'),
    skus=('code','nunique'))
