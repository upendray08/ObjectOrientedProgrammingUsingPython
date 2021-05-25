class Student:
    college="k.j"
    def __init__(self,name,rollno,div):
        self.name="ramesh"
        self.rollno=56
        self.div="B"
    def printDetails(self):
        print(f"college is {self.college}")
        print(f"name is {self.name}")
        print(f"rollno is {self.rollno}")
        print(f"div is {self.div}")

# upendra=Student("upendra", 34,"B" )
ramesh=Student("ramesh", 56, "B")
# upendra.printDetails()
ramesh.printDetails()

