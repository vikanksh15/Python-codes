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
    
    def __repr__(self) -> str:
        return f"item('{self.name}',{self.price},{self.quantity})"
    
item1 = item("Phone",12000,2)
item2 = item("Laptop",70000,1)
item3 = item('Cable',2000,10)
item4 = item('Mouse',8000,5)
item5 = item('Gamepad',10000,4)
# print(item1.calculate_total_price())

for instance in item.all:
    print(instance,end='\n')