class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Number cant be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """
        Return self.quantity.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Change the value of self.cuantity.
        """
        # Validate the value of cuantity
        if quantity < 0:
            raise ValueError("Number cant be negative")
        # Set the new Value
        self.quantity = quantity

        # if the cuantity is 0 set self.active to False
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Returns the active status.
        """
        return self.active

    def activate(self):
        """
        Activate the Product.
        """
        self.activate = True

    def deactivate(self):
        """
        Deactivate the Product.
        """
        self.activate = False

    def show(self) -> str:
        """
        Returns a string that represents the product.
        """
        product_representation = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        
        return product_representation

    def buy(self, quantity) -> float:
        """
        Buys the product and update the quantity.
        """
        # Validate data
        if quantity < 0:
            raise ValueError("Number cant be negative")
        
        # Check if quantity ist bigger then availible
        if self.quantity >= quantity:
            self.quantity -= quantity
            return self.show()
        else:
            raise ValueError("The quantity you want to buy is bigger then availible")
        


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()