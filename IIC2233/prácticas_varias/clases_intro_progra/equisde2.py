n = 5
a = 1
b = 10

# a+b
#1,10,11,21,32,53,85
"""def fibonacci_recursivo(n):
  if n <= 1 or b <= 1:
    return n
  else:
    return fibonacci_recursivo(n-a) + fibonacci_recursivo(n-b)
  
print(fibonacci_recursivo(6))"""

#a = 1
#b = 10
#n = 5

#a = 1
#b = 10
#n = 4



def deltanacci(a,b,n):
  if n == 1:
    return a
  elif n == 2:
    return b
  else:
    #print("_________________________________")
    return deltanacci(a,b,n-1)  + deltanacci(a,b,n-2)

print(deltanacci(4,7,16))


#deltanacci(1,4,3) = 5
# deltanacci(1,4,4) = 9


#deltanacci(1,4,5) = deltanacci(1,4,4)  + #deltanacci(1,4,3) 
#                  =( deltanacci(1,4,3) + deltanacci(1,4,2) ) + deltanacci(1,4,2) + deltanacci(1,4,1) )
#                  = deltanacci(1,4,2) + deltanacci(1,4,1) + 4 + 4 + 1 
#                  = 4 + 1 + 4 + 4 + 1 = 14

print(deltanacci(1,4,3))

#1,4,5,9,14,23,37,50,87,137,224,357,481












3



def ultranacci(a,b,c,n):
  if n == 1:
    print("----",a)
    return a
  elif n == 2:
    print("----",b)
  elif n == 3:
    return c
  else:
    print("----")
    print(n-1)
    print(n-2)
    return deltanacci(a,b,n-1)  + deltanacci(a,b,n-2)  + deltanacci(a,b,n-3) 


#1,99,100,199,299,498,797


