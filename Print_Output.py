# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:22:04 2019

@author: skotsan
"""

# file-output.py
import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime
filename = 'Run_Log_-%s.txt'%datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])




X = range(10)
plt.plot(X, [x*x for x in X])
plt.show()

f = open(filename,'w')
f.write('hello world')
f.write("\n")
f.write('second line of code')
f.write("\n")

f.close()
with open(filename, 'a') as f:
    df.to_csv(f, sep='\t', index=False)

print(filename)