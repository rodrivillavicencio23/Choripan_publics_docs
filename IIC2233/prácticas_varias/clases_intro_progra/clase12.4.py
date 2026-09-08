word1 = input("Input a word: ")
#Invertir string sin tanto show
word2 = word1 [:: -1]

if word1 == word2:
    print("La palabrinha es palíndroma")
else:
    print("la palabra POR SUPUESTO QUE NO es palíndroma")

#Imprimir cord. de caracter determinado por el []
print(word1[2])

s ="gato"

def palindrome (s):
    for i in range(len(s)):
        if s[i] != s[len(s)-(i+1)]:
            return False
        else:
            return True
        
#terminalo oe te crei figura
word3 = "reconocer"     
palindrome(word3)
