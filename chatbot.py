                              # MULTICALCULATOR CHATBOT
                                                                          # CH.GOPI SAI TEJA(19PA1A0432)
                                                                          # D.YUVA TEJA (19PA1A0439)

import math
    # greetings
print("welocome to the multicalculator chatbot")

print("can I know your name please !")

    #Taking username 
user_name=str(input())

print("welcome"+" "+user_name)

print("services that I am providing are")

services_providing=["1.General calculator","2.BMI calculator","3.Trigonometric calculator"]

general_calculator=["1.addition","2.subraction","3.multiplication","4.division","5.square root of a number","6.square of a number","7.logarithm of a number"]

Trigonometric_calculator=["1.sine","2.cosine","3.tan","4.sinh","5.cosh","6.tanh","7.inverse sinh","8.inverse cosh","9.inverse tanh","10.inverse sine","11.inverse cosine","12.inverse tan"]

for i in range(0,len(services_providing)):
    print(services_providing[i])                  # printing the services

print("please enter the serial number of that service you want :")

service_number=str(input())

if(service_number=="1"):
    print(" please select the serial number of calculation you want :")   # for general calculator

    for j in range(0,len(general_calculator)):
        print(general_calculator[j])

    a=input()
    
    if(a=="1"):
        num1=int(input("enter 1st number :"))       #addition
        num2=int(input("enter 2nd number :"))
        print(f"{num1}+{num2}={num1+num2}")

    elif(a=="2"):
        num1=int(input("enter big number :"))           #subraction
        num2=int(input("enter small number :"))
        print(f"{num1}-{num2}={num1-num2}")

    elif(a=="3"):
        num1=int(input("enter 1st number :"))
        num2=int(input("enter 2nd number :"))         # multiplication
        print(f"{num1}*{num2}={num1*num2}")

    elif(a=="4"):
        num1=int(input("enter 1st number :"))
        num2=int(input("enter 2nd number :"))         # division
        print(f"{num1}/{num2}={num1/num2}")

    elif(a=="5"):
        num=int(input("enter a number :"))
        print("square root of "+str(num)+"is",math.sqrt(num))   # square root

    elif(a=="6"):
        num=int(input("enter a number :"))          # sqare
        print("square  of "+str(num)+"is",num*num)
    

    elif(a=="7"):
        num1=int(input("enter number :"))             #logarithm
        num2=int(input("enter base number :"))
        print(math.log(num1,num2))

    else:
        print("plaese enter a valid number !")


elif(service_number=="3"):
    for k in range(0,len(Trigonometric_calculator)):              #trigonometric calculator
        print(Trigonometric_calculator[k])
    
    b=str(input())

    if(b=="1"):
        num1=int(input("enter a number :"))         #sine
        print(math.sin(num1))

    elif(b=="2"):
        num1=int(input("enter a number :"))          #cosine
        print(math.cos(num1))

    elif(b=="3"):
        num1=int(input("enter a number :"))      # tan
        print(math.tan(num1))
    elif(b=="4"):
        num1=int(input("enter a number :"))       #sinh
        print(math.sinh(num1))

    elif(b=="5"):
        num1=int(input("enter a number :"))         # cosh
        print(math.cosh(num1))
    
    elif(b=="6"):
        num1=int(input("enter a number :"))            # tanh
        print(math.tanh(num1))

    elif(b=="7"):
        num1=int(input("enter a number :"))          # inverse sinh
        print(math.asinh(num1))

    elif(b=="8"):
        num1=int(input("enter a number :"))            # inverse cosh
        print(math.acosh(num1))

    elif(b=="9"):
        num1=int(input("enter a number :"))         # inverse tanh
        print(math.atanh(num1))

    elif(b=="10"):
        num1=int(input("enter a number :"))        # inverse sine
        print(math.asin(num1))

    elif(b=="11"):
        num1=int(input("enter a number :"))    #inverse cosine
        print(math.acos(num1))

    elif(b=="12"):
        num1=int(input("enter a number :"))         # inverse tan
        print(math.atan(num1))

    else:
        print("enter a valid number !")

elif(service_number=="2"):
    num1=int(input("enter your weight in kgs :"))
    num2=int(input("enter your height in cm :"))        # bmi calculator
    x=(num1/(num2*num2))*1000
    print("your BMI value is :",x)
    if(x<18):
        print("you are under weight!")
    elif(x>25 and x<30):
        print("you are over weight!")
    elif(x>30):
        print("you are obessed!")
    else:
        print("you are in safe range!")
    
else:
    print("choose a valid number !")
print("Thank you!")



       




