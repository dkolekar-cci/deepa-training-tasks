
def display_products(product_list):
    for item in product_list:
     value = item.get_value()
     print(f"{item.name} - Rs {value}")

def cal_total_inventory_value(product_list):
    total_inventory_value=0
    for item in product_list:
       total_inventory_value += item.get_value()
    return total_inventory_value 
