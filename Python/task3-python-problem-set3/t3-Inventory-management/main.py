from product import Product, PerishableProduct
from inventory_utils import display_products, cal_total_inventory_value

Product_1 = Product("52A13", "Rice", 50, 400)
Product_2 = Product("52A14", "Sugarr", 30, 200)
Product_3 = PerishableProduct("53B11", "Bread", 20, 150, True)
Product_4 = PerishableProduct("53B12", "Cheese", 10, 300, False)

product_list = [Product_1, Product_2, Product_3, Product_4]

display_products(product_list)

total_inventory_value = cal_total_inventory_value(product_list)

print("Total inventory value is: Rs", total_inventory_value)