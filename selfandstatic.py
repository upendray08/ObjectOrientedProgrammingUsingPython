class Employees:
    company="TCS"
    @staticmethod
    def time():
        print("the time is 9am")
    def greet(self):
        print(f"Hello How are U {self.name}?")
    def printData(self):
        print(f"company is {self.company}")
        print(f"salary is {self.salary}")
        print(f"id is  {self.id}")



upendra=Employees()
ramesh=Employees()
upendra.salary="300"
ramesh.name="ramesh"
upendra.name="upendra"
upendra.id=423
upendra.greet()
ramesh.greet()
upendra.printData() 
upendra.time()

