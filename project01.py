tempreture=float(input("Enter the temprature = "))
scaler=str(input("Enter the scale = "))
scaler=scaler.upper()
if(scaler=="C"):
    F=(tempreture*9/5)+32
    k=tempreture+273.15
    print(f"The tempreature in Ferenheit is {F}")
    print(f"The tempreature in Kelvin is {k}")
elif(scaler=="F"):
    C=5/9*(tempreture-32)
    K=C+273.15
    print("The temprature in Celcious is {C}")
    print("The temprature in Kelvin is {K}")
elif(scaler=="K"):
    C=tempreture-273.15
    F=(C*9/5)+32
    print(f"The tempratue in celcius is {C}")
    print(f"The tempratue in Ferenheit is {F}")
else:
    print("you have Entered wrong entity")