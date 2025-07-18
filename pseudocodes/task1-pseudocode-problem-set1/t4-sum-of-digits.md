# Task 4 : Sum of Digits

## Pseudocode

**Step-1:** Take input from the user  
`String num`  

**Step-2:** Initialize sum to 0  
`Integer sum <- 0`  

**Step-3:** For each digit in num, convert digit to integer and add to sum  
`sum <- sum + Integer(digit)`  

**Step-4:** Return sum                 
`Print "Sum of digits:", sum`

## Dry Run Test

### Example 1  
**Input:**  
num = "123"  

**Step-1**
num = "123"  

**Step-2**  
sum = 0  

**Step-3**  
digit = '1'so Integer('1') = 1 
 sum = 0 + 1 = 1  
digit = '2'so Integer('2') = 2 
 sum = 1 + 2 = 3  
digit = '3'so Integer('3') = 3 
 sum = 3 + 3 = 6  

**Step-4**  
Print "Sum of digits: 6"  

### Example 2  
**Input:**  
num = "428"  

**Dry Run:**  
**Step-1**  
num = "428"  

**Step-2** 
sum = 0  

**Step-3**  
digit = '4' so Integer('4') = 4 
 sum = 0 + 4 = 4  
digit = '2' so Integer('2') = 2 
 sum = 4 + 2 = 6  
digit = '8' so Integer('8') = 8 
 sum = 6 + 8 = 14  

**Step-4** 
Print "Sum of digits: 14"
