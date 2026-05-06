class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def get_sum(self):
        return self.a + self.b
    
    def get_subrtraction(self):
        return self.a - self.b
    
    def get_multiplication(self):
        return self.a * self.b

    def get_division(self):
        return self.a / self.b

if __name__ == "__main__":
    myCalc = Calculator(a=3,b=5)
    print(myCalc.get_division())
