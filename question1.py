sum=0
for i in range(0,5):
    n=int(input())
    if (n>0):
        sum=sum+n
    else:
        print("enter positive numbers")
else:
    print(sum)  
x=open("ans.txt","a")
print("ans:",sum,file=x)
print("ans:",sum)  