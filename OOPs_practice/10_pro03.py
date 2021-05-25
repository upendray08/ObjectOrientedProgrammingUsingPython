class num:
    a = 2

    def __init__(self):
        self.a = 0
        
    def getinfo(self):
        print(f"the value is {self.a}")


object = num()
# print(num.a)
num.a = 0
print(num.a)
object.getinfo()
