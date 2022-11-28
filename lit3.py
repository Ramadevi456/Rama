##import pandas as pd
#df=pd.DataFrame()
#print(df)
import pandas as pd
data = {'country' : ['belgium','india','brazil'],
'capital' : ['brussels','new Delhi','brasilia'],
'population' : [114536,76456,9876544]}
df = pd.DataFrame(data, columns=['country','capital','population'])
print(df)
