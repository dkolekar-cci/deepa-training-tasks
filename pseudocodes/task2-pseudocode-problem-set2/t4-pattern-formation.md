# Task 4: Pattern Formation – Diamond


## Pseudocode

**Step-1:** Take input `n`  
  n <- input number

**Step-2:** Loop `i` from 1 to `n`  
  `spaces <- n - i`  
  `stars <- 2 * i - 1`  
  Display `spaces` number of space characters  
  Display `stars` number of asterisk characters

**Step-3:** Loop `i` from `n - 1` down to 1  
  `spaces <- n - i`  
  `stars <- 2 * i - 1`  
  Display `spaces` number of space characters  
  Display `stars` number of asterisk characters

---

## Dry Run Test

**Input:**  
`n <- 4`

**Upper Half Loop (i = 1 to 4):**

i = 1  
spaces = 3, stars = 1            
i = 2  
spaces = 2, stars = 3           
i = 3  
spaces = 1, stars = 5          
i = 4  
spaces = 0, stars = 7       

**Lower Half Loop (i = 3 to 1):**

i = 3  
spaces = 1, stars = 5         
i = 2  
spaces = 2, stars = 3         
i = 1  
spaces = 3, stars = 1       

**Output:**
        *
       ***
      *****
     *******
      *****
       ***
        *
