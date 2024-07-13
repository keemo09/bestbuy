class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """
        Add a product of Product class to the store.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        """
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products
        """
        total_quantity = 0
        for product in self.product_list:
            product_quantity = product.get_quantity()
            total_quantity += product_quantity
        return total_quantity

    def get_all_products(self) -> list:
        """
        Return all active products in store.
        """
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Refresh quantity of the products in store and return the total price
        """
        total_price = 0
        for order in shopping_list:
            product = order[0]
            quantity = order[1]
            try:
                product.buy(quantity)
                price = product.price * quantity
                total_price += price
            except ValueError:
                raise ValueError("Product out of stock")

        return total_price

    def __contains__(self, product):
        return product in self.product_list

    def __add__(self, other):
        combined_product_list = self.product_list + other.product_list
        return Store(combined_product_list)
