number = int(input())
lenny = 0
if number%(number%100)== 0:
    print(True)
    lenny+=1
else:
    print(False)
if (number//10000) < ((number//100)%10):
    print(True)
    lenny+=1
else:
    print(False)
if ((number//1000)%10) > (number%10):
    print(True)
    lenny+=1
else:
    print(False)
if ((number//10)%10) <= (number%10):
    print(True)
    lenny+=1
else:
    print(False)
if lenny == 4:
    print( "LENNY!")
else:
    print("NOT LENNY!")