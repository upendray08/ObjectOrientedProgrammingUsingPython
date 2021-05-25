class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def printDetails(self):
        print(f"name of programmer is {self.name}")
        print(f"working is {self.product}")


Upendra = Programmer("Upendra", "visual studio code")
Upendra.printDetails()
alka = Programmer("alka", "skype")
alka.printDetails()
akash=Programmer("akash", "zoom")
