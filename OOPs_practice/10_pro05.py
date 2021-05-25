class Train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
        # self.seats=seasNo
    def getFareInfo(self):
        print(f"Fare of {self.name} is {self.fare}")
    def getStatusInfo(self):
        print(f"name of train is {self.name}")
        print(f"seats in train is  {self.seats}")
    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked and Your seat No. is {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"Your ticket cann't be booked no of ticket are  {self.seats}")
    def cancelTicket(self,seasNo):
        self.seats=self.seats+1
        print(f"Now seats after cancelling  is {self.seats}")
    

godam=Train("Godam Express-10145", 45, "Rs450")
godam.getFareInfo()
godam.getStatusInfo()
kolhapuri=Train("kolhapuri Express", 12, "Rs550")
kolhapuri.getFareInfo()
kolhapuri.getStatusInfo()
# kolhapuri.bookTicket()
# kolhapuri.bookTicket()
# godam.bookTicket()
# godam.bookTicket()
# godam.bookTicket()
# godam.bookTicket()
# godam.bookTicket()
# godam.bookTicket()
# godam.bookTicket()
kolhapuri.bookTicket()
kolhapuri.cancelTicket(12)