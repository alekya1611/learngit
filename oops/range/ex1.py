n=int(input())
for i in range(n):
    print(i)
    x=open("rng.txt","a")
    print(i,file=x)