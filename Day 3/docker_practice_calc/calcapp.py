import math

class Calculator:
    def __init__(self, a):
        self.a = a
        
    def get_square_root(self):
        return math.sqrt(self.a)
    
if __name__ == "__main__":
    myCalc = Calculator(a=435,)
    print(myCalc.get_square_root())
