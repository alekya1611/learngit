import pandas as pd 
a1=[1,2,3,4,5]
a2=[6,7,8,9,10]
s1=pd.Series(a1)
s2=pd.Series(a2)
print(s1)
print(s2)
add=s1+s2
sub=s1-s2
mul=s1*s2
div=s1/s2
mod=s1%s2
print("Add two Series : ")
print(add)
print("subtract two series :")
print(sub)
print("multiply two series :")
print(mul)
print("divide two series :")
print(div)
print("remainder of two series :")
print(mod)

