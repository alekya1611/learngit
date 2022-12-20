import pandas as pd  
a=[int(input("enter the  inputs :")) for i in range(5)]
sq=pd.Series(a)
l=sq**2
p=pd.Series(l)
print(p)

