class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"the square of {self.number} number is {self.number **2}")
    def squareRoot(self):
        print(f"the square of {self.number} number is {self.number **0.5}")
    def cube(self):
        print(f"the square of {self.number} number is {self.number **3}")

n=int(input("enter the number:\n"))
a=Calculator(n)
a.square()
a.squareRoot()
a.cube()



