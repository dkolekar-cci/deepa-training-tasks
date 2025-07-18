# Task 1: Sum of All Items in a Dictionary

## Pseudocode

**Function:** `SumOfItems(dict)`  
  **Step-1:** Initialize a variable to store the sum  
  `Integer total <- 0`  

  **Step-2:** For each key in dict  
  `For each key in dict:`  
    `total <- total + dict[key]`  

  **Step-3:** Return total  
  `Return total`

## Dry Run Test 1

**Input:**  
`dict = {‘a’: 400, ‘b’: 200, ‘c’: 300}`

**Step-1:**  
`total <- 0`

**Step-2:**  
`total <- total + 400 → total = 400`  
`total <- total + 200 → total = 600`  
`total <- total + 300 → total = 900`

**Output:**  
`900`

## Dry Run Test 2

**Input:**  
`dict = {‘x’: 35, ‘y’: 18, ‘z’: 45}`

**Step-1:**  
`total <- 0`

**Step-2:**  
`total <- total + 35 → total = 35`  
`total <- total + 18 → total = 53`  
`total <- total + 45 → total = 98`

**Output:**  
`98`
