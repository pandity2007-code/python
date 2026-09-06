import random


class train():
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def ticket(self,fro,to,):
        print(f"your ticket is booked {fro} to {to} in trainNO:{self.trainNo}")    
    def status(self,fro,to):
        print(f"the train {self.trainNo} is running on time")
    def price(self,fro,to):
        print(f"the fare of train {self.trainNo} is { random.randint (200,2000)}from {fro} to {to}. ")

    @staticmethod 
    def hello():
        print("Thankyou")  
a=train(12555)   
a.ticket("rampur","delhi")
a.status("rampur","delhi")
a.price("rampur","delhi")
    