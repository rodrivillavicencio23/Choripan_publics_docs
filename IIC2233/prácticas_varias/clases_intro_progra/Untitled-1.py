#Variables y lista de temperaturas
t = int(input("Input a temperature value 1: "))
t2 = int(input("Input a temperature value 2: "))
t3 = int(input("Input a temperature value 3: "))
ts = [t,t2,t3]
value=0
value2=0
value3=0
value4=0
value5=0
value6=0
print(ts)
#Recorrer lista ingresada
for ints in ts:
    if 0<=ints<=99:
        value +=1
    elif 100<=ints<=199:
        value2+=1
    elif 200<=ints<=299:
        value3+=1
    elif 300<=ints<=399:
        value4+=1
    elif 400<=ints<=499:
        value5+=1
    elif ints>=500:
        value6+=1
#Evaluación de variantes
if value >= 2:
    print("Well")
elif value2>=2:
    print("regular")
elif value3>=2:
    print("precaution")
elif value4>=2:
    print("alert")
elif value5>=2:
    print("search a best place")
elif value6>=2:
    print("in 10 minutes you will burned")