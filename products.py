from store import Store


class Product:
    def __init__(self, name, price, quantity):
        # Check if price and quantity is not negative
        if price < 0 or quantity < 0:
            raise ValueError("Number can´t be negative!")

        # Checks if name is not empty
        if len(name) == 0:
            raise ValueError("Name can´t be empty!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

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
        self.active = False

    def __str__(self) -> str:
        """
        Returns a string that represents the product.
        """
        product_representation = (
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        )

        if self.promotion != None:
            product_representation += f", Promotion: {self.promotion.name}"

        return product_representation

    def buy(self, quantity) -> float:
        """
        Buys the product and update the quantity.
        """
        # Validate data
        if quantity < 0:
            raise ValueError("Number cant be negative")

        # Check if quantity ist bigger then availible
        if self.quantity < quantity:
            raise ValueError("The quantity you want to buy is bigger then availible")

        # Update quantity
        self.quantity -= quantity

        # If quantity is 0 deactivate product
        if self.quantity == 0:
            self.deactivate()
        return self.__str__()

    def set_promotion(self, promotion):
        """
        Set a Promotion.
        """
        if isinstance(promotion, Promotion):
            self.promotion = promotion
        else:
            raise ValueError("Promotion must be a Promotion instance!")

    def get_promotion(self):
        """
        Get a Promotion.
        """
        return self.promotion()

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        # Check if price and quantity is not negative
        if price < 0:
            raise ValueError("Number can´t be negative!")

        # Checks if name is not empty
        if len(name) == 0:
            raise ValueError("Name can´t be empty!")

        self.name = name
        self.price = price
        self.active = True
        self.promotion = None

    def get_quantity(self):
        raise NotImplementedError("Product has no quantity")

    def set_quantity(self, quantity):
        raise NotImplementedError("Product has no quantity")

    def __str__(self) -> str:
        """
        Returns a string that represents the product.
        """
        product_representation = f"{self.name}, Price: {self.price}"

        if self.promotion != None:
            product_representation += f", Promotion: {self.promotion.name}"

        return product_representation

    def buy(self):
        return self.__str__()


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self) -> str:
        """
        Returns a string that represents the product.
        """
        product_representation = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

        if self.promotion != None:
            product_representation += f", Promotion: {self.promotion.name}"

        return product_representation

    def buy(self, quantity):
        """
        Buys the product and update the quantity.
        """
        # Validate data
        if quantity < 0:
            raise ValueError("Number cant be negative")

        # Check if quantity ist bigger then availible
        if self.quantity < quantity:
            raise ValueError("The quantity you want to buy is bigger then availible")

        # Check if quantity not bigger than maximum
        if quantity > self.maximum:
            raise ValueError("Quantity is bigger than maximum!")

        # Update quantity
        self.quantity -= quantity

        # If quantity is 0 deactivate product
        if self.quantity == 0:
            self.deactivate()
        return self.__str__()
