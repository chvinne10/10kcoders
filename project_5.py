from abc import ABC,abstractmethod
class Online_shoping_cart(ABC):
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    @abstractmethod
    def add_cart(self):
        pass
    @abstractmethod
    def remove_cart(self):
        pass
    @abstractmethod
    def checkout(self):
        pass
class Product(Online_shoping_cart):
    def __init__(self, name, price, stock):
        self.quantity=0
        super().__init__(name, price, stock)
    def add_cart(self):
        self.quantity=int(input("enter the quantity"))
        self.stock-=self.quantity
        print(f"Product:{self.name},qunatity:{self.quantity},price:{self.price},")
    def remove_cart(self):
        self.quantity=0
        self.name="NULL"
    def checkout(self):
        print(f"total stock remain:{self.stock}")
    def view_cart(self):
        print(f"|name:{self.name}|price:{self.price},|stock:{self.stock},quantity:{self.quantity}")
        
while True:
    print("1.add to cart\n 2.remove_cart \n3.checkout\n4.view cart\n")
    x=int(input("enter the choice:"))
    match(x):
        case 1:
            name=input("enetr the name of product:")
            price=int(input("enetr the price of the product:"))
            p=Product(name,price,100)
        case 2:
            p.add_cart()
        case 3:
            p.checkout()
        case 4:
            p.view_cart()
        case 5:
            break
        case _:
            print("invalid")
            
            
        