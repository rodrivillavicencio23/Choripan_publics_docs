class Contador1a5:
    def __init__(self):
        self.n = 1
        self.limite = 6
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n >= self.limite:
            raise StopIteration()
        item = self.n
        self.n += 1
        return item

for x in Contador1a5():
    print(x)