# Task 2: Interchange First and Last Elements in a List

## Pseudocode

**Function:** `SwapFirstLast(list)`  
  **Step-1:** Store the first element in a temporary variable  
  `temp <- list[0]`

  **Step-2:** Assign the last element to the first position  
  `list[0] <- list[length of list - 1]`

  **Step-3:** Assign the temporary variable to the last position  
  `list[length of list - 1] <- temp`

  **Step-4:** Return list  
  `Return list`

---

## Dry Run Test 1

**Input:**  
`list = [12, 35, 9, 56, 24]`

**Step-1:**  
`temp <- 12`

**Step-2:**  
`list[0] <- 24 
list = [24, 35, 9, 56, 24]`

**Step-3:**  
`list[4] <- 12 
list = [24, 35, 9, 56, 12]`

**Output:**  
`[24, 35, 9, 56, 12]`

---

## Dry Run Test 2

**Input:**  
`list = [1, 2, 3]`

**Step-1:**  
`temp <- 1`

**Step-2:**  
`list[0] <- 3 
list = [3, 2, 3]`

**Step-3:**  
`list[2] <- 1 
list = [3, 2, 1]`

**Output:**  
`[3, 2, 1]`
