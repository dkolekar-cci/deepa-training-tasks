# Task 7: Product Catalog System (Class, Object, List)

## Pseudocode

**`Step 1:`** Define class Product  
 Attributes: name, price, category  
 Method: display_info()  
  Display name, price, and category

**`Step 2:`** Create empty list called `product_list

**`Step 3:`** Input number of products  
n <- total number of products  

**`Step 4:`** Repeat n times:  
 Input name, price, category  
 Create object of Product class  
 Append object to product_list

**`Step 5:`** Ask for a category to search  
Input target_category  

**`Step 6:`** Display all products in target_category  
For each product in product_list:  
 If product.category equals target_category then  
  Call product.display_info()

**`Step 7:`** Find the product with highest price  
max_price <- -1  
expensive_product <- null  

For each product in product_list:  
 If product.price > max_price then  
  max_price <- product.price  
  expensive_product <- product

**`Step 8:`** Return details of expensive_product

---
## Dry Run Example 1

**Input:**  
`Phone, 30000, Electronics`  
`Pen, 20, Stationery`  
  

**Target category:** Stationery

**Steps:**  
Add Phone to product_list  
Add Pen to product_list    

Filter products in "Stationery":  
Pen  
  

Compare prices:  
Phone is 30000  
Pen is 20    

**Output:**  
`Highest price product is Phone costing ₹30000`

