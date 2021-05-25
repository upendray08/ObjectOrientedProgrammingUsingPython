class Employees:
    company="foogle"
    def __init__(self,name,salary,id):
        print("Employees class ban gaya hai")
        self.name="upendra"
        self.salary="100k"
        self.id=250
        
    def printDetails(self):
        print(f"name is {self.name}")
        print(f"salary is {self.salary}")
        print(f"id is {self.id}")



upendra=Employees("upendra","100k",250)
upendra.printDetails()