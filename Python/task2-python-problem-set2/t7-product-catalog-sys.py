class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Name: {self.name}, Price: Rs{self.price}, Category: {self.category}")

product1 = Product("Phone", 30000, "Electronics")
product2 = Product("Pen", 20, "Stationery")
product3 = Product("Pencil", 10, "Stationery")

products = [product1, product2, product3]

highest_price_product = max(products, key=lambda p: p.price)

print(f"Highest price product is {highest_price_product.name} costing Rs{highest_price_product.price}")
