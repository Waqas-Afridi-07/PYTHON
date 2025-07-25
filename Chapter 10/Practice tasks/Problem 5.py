from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo  

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        fare = randint(222, 555)
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is ₹{fare}")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
