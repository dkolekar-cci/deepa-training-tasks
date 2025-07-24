class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, new_id):
        self.__product_id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price


    def get_value(self):
        return self.__quantity * self.__price

class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity, price, expiring_soon):
        super().__init__(product_id, name, quantity, price)
        self.expiring_soon = expiring_soon

    def get_value(self):
        if self.expiring_soon:  
            return super().get_value() * 0.3
        else:
            return super().get_value()
