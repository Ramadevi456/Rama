#import pandas as pd
#ser=pd.Series()
#print(ser)
import pandas as pd
import numpy as np
data = np.array(['g','e','e','k','f'])
s = pd.Series(data, index=[10,11,13,14])
print(s)
