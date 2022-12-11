brand1=input()
brand2=input()
brand3=input()
color1=input()
color2=input()
color3=input()
car={brand1:color1,brand2:color2,brand3:color3}
x=open("ans.txt","a")
for k,v in car.items():
    print(k,v)
    print(k,v,file=x)
print(car)
print(car,file=x)