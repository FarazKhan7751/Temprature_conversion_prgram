import random
a=random.randint(0,10)
b=int(input("Enter the number = "))
while(a<b):
    print("low")
    print("They are not equal ")
    b=int(input("Enter the number = "))
while(b<a):
    print("high")
    print("They are not eqial")
    b=int(input("Enter the number = "))
if(a==b):
    print("They are equal")