# Task 6: Sum of 2 Numbers

## Pseudocode

**Step 1:** Take inputs  
  `nums ← list of integers`  
  `target ← integer value`  

**Step 2:** Initialize an empty dictionary  
  `seen ← empty map`

**Step 3:** Loop through nums with index i  
  `current_number ← nums[i]`  
  `difference ← target - current_number`  

  If difference in seen then  
    `Return [seen[difference], i]`  
  `Else`  
    `seen[current_number] ← i`  

---
## Dry Run Example 1

**Input:**  
`nums = [2, 7, 11, 15]`  
`target = 9`  

**Steps:**  
i = 0, current_number = 2  
difference = 7  
7 not in seen  
Add 2 to seen with index 0  

i = 1, current_number = 7  
difference = 2  
2 found in seen at index 0  

`Return [0, 1]`

---

## Dry Run Example 2

**Input:**  
`nums = [3, 2, 4]`  
`target = 6`  

**Steps:**  
i = 0, current_number = 3  
difference = 3  
3 not in seen  
Add 3 to seen with index 0  

i = 1, current_number = 2  
difference = 4  
4 not in seen  
Add 2 to seen with index 1  

i = 2, current_number = 4  
difference = 2  
2 found in seen at index 1  

`Return [1, 2]`

---

## Dry Run Example 3

**Input:**  
`nums = [3, 3]`  
`target = 6`  

**Steps:**  
i = 0, current_number = 3  
difference = 3  
3 not in seen  
Add 3 to seen with index 0  

i = 1, current_number = 3  
difference = 3  
3 found in seen at index 0  

`Return [0, 1]`
