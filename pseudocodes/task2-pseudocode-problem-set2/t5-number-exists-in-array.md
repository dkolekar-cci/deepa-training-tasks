# Task 5: Number Exists in Array

## Pseudocode

**Step-1:** Take inputs  
  `array_one <- [1, 5, 8, 9, 10]`  
  `array_two <- [5, 8, 9, 10, 12, 20, 40, 60, 70]`  
  `input_number <- <number to search>`

**Step-2:** Initialize two boolean variables  
  `found_in_array_one <- False`  
  `found_in_array_two <- False`

**Step-3:** For each element in array_one  
    If element = input_number  
      `found_in_array_one <- True`

**Step-4:** For each element in array_two  
    If element = input_number  
      `found_in_array_two <- True`

**Step-5:** 

 If found_in_array_one = True and found_in_array_two = True  
    Return `"number input_number found in both arrays"`  
 Else if found_in_array_one = True  
    Return `"number input_number found in array_one"`  
 Else if found_in_array_two = True  
    Return `"number input_number found in array_two"`  
 Else  
    Return `"number input_number not found in any array"`

---

## Dry Run Test 1

**Input:**  
`array_one <- [1, 5, 8, 9, 10]`  
`array_two <-  [5, 8, 9, 10, 12, 20, 40, 60, 70]`  
`input_number <- 10`

**Steps:**  
found_in_array_one <- True  
found_in_array_two <- True  
Both True then Return `"number 10 found in both arrays"`

**Output:**  
`number 10 found in both arrays`

---

## Dry Run Test 2

**Input:**  
`input_number <- 70`

**Steps:**  
found_in_array_one <- False  
found_in_array_two <- True  
Return `"number 70 found in array_two"`

**Output:**  
`number 70 found in array_two`

---

## Dry Run Test 3

**Input:**  
`input_number <- 1`

**Steps:**  
found_in_array_one <- True  
found_in_array_two <- False  
Return `"number 1 found in array_one"`

**Output:**  
`number 1 found in array_one`

---

## Dry Run Test 4

**Input:**  
`input_number <- 99`

**Steps:**  
found_in_array_one <- False  
found_in_array_two <- False  
Return `"number 99 not found in any array"`

**Output:**  
`number 99 not found in any array`
