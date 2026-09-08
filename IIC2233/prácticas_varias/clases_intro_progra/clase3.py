t = int(input("Input a temperature value 1: "))
t2 = int(input("Input a temperature value 2: "))
t3 = int(input("Input a temperature value 3: "))
value = 0

#Condicional (Test of temperature with different ranges)

if (0 <= t <= 99) or (0 <= t2 <= 99) or (0 <= t3 <= 99):
    value +=1
if (100 <= t <= 199) or (100 <= t2 <= 199) or (100 <= t3 <= 199):
    value +=1
if (200 <= t <= 299) or (200 <= t2 <= 299) or (200 <= t3 <= 299):
    value +=1
if (300 <= t <= 399) or (300 <= t2 <= 399) or (300 <= t3 <= 399):
    value +=1
if (400 <= t <= 499) or (400 <= t2 <= 499) or (400 <= t3 <= 499):
    value +=1
if (t < 0) or (t2 < 0) or (t3 < 0):
    print("out of range, restart the input/program")
if (t > 500) or (t2 > 500) or (t3 > 500):
    value +=1

print(value) 

if value ==0:
    print("Great")
elif value ==1: 
    print("Regular")
elif value ==2:
    print("Alert")
elif value ==2: 
    print("Precaution")
elif value ==4:
    print("Dangerous")
elif value ==5:
    print("bro get out of that place right now")