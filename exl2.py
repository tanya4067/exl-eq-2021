import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\tanya\Downloads\Book1.xlsx')
from collections import Counter
r=dict()
f=1
s=0
for i in range(0,3131):
    t=(df.iloc[i])
    x=t['stateFIPS']
    if(x==f):
        s+=t['C_TOT_POP']
    else:
        r[f]=s
        s=0
        s+=t['C_TOT_POP']
        f=x
r[f]=s
print(r)
