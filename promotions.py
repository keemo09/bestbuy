from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Name cant blank!")
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        '''
        Abstract method which returns the price of speciefic promotion.
        '''
        # Checks if product is Product instance.
        if isinstance(product, Product) == False:
            raise ValueError("Product must be a Product instance!")
        
        # Checks quantity is positive.
        if quantity < 0:
            raise ValueError("Quantity must be positive!")
        
        # Checks quantity is not bigger than availible.
        if quantity > product.get_quantity():
            return ValueError("Quantity is bigger then availible!")
         


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("Please enter a valid percentage number from 0 to 100")
        self.percent = percent

    def apply_promotion(self, product, quantity):
         '''
         Return the price after the promotion is applied.
         '''
         super().apply_promotion(self, product, quantity)
         multiplier = 1 - (self.percent / 100)
         product_price = product.price 
         price_without_promotion = product_price * quantity
         total_price = price_without_promotion * multiplier
         return total_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        '''
         Return the price after the promotion is applied.
         '''
        super().apply_promotion(self, product, quantity)
        promo_quantity = quantity // 2
        product_price = product.price
        total_promo = (promo_quantity * product_price) % 2
        total_price = (product.price * quantity) - total_promo
        return total_price
    

class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        '''
         Return the price after the promotion is applied.
         '''
        super().apply_promotion(self, product, quantity)
        free_products = quantity // 3
        product_price = product.price
        total_price = product_price * (quantity - free_products)
        return total_price