import csv
from msilib.schema import InstallUISequence


class item(object):
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []
    def __init__(self,name : str,price: float, quantity):
        #Run validations to the received arguments
        assert price>=0, f"Price {price} is not greate than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"


        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # print("I am created")

        #object-instance collection
        item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for i in items:
            print(i)
    
    def __repr__(self) -> str:
        return f"item('{self.name}',{self.price},{self.quantity})"
    

item.instantiate_from_csv()