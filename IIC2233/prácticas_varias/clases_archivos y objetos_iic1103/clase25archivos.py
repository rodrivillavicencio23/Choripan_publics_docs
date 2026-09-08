class Fraccion:

    def __init__(self, num, den):
        self.num = num
        self.den = den


    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def __add__(self,other):
        if type(other) == int:
            return Fraccion(self.num + other * self.den, self.den)

        if self.den == other.den:
            return Fraccion(self.num+other.num, self.den)
        nuevo_num = self.num * other.den+other.num * self.den
        nuevo_den = self.den * other.den
        nueva = Fraccion(nuevo_num, nuevo_den)
        return nueva

    

f1 = Fraccion(3,4)
print(f1)
f2 = Fraccion(1,2)
g = f1+4
print(g)