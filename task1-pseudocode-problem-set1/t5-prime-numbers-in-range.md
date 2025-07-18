# Task 5: Find Prime Numbers in a Given Range

## Pseudocode 

**Step 1:** Take input from the user  
`Integer start, end`

**Step 2:** Check if both numbers are positive  
If either start or end is less than 0  
  `Display a message: "Invalid input. Please enter positive numbers only."`  
   

**Step 3** Check if the start number is greater than the end number  
If start is greater than end  
  `Display a message: "Invalid range. Starting number must be less than or equal to ending number."`  
  

**Step 4:** Create an empty list to store prime numbers  
`list_primes <- []`

**Step 5:** Loop through each number from start to end
Skip numbers less than 2 (because 0 and 1 are not prime)
    `If number < 2:
        Continue to next number`

    Assume the current number is prime
    `is_prime <- true`

    Check if the number is divisible by any number from 2 to number -1
    If divisible then
     is_prime <- false
           
    If the number is not divisible then add it to list_primes
    
**Step 5:** After checking all numbers in the range  
`Return list_primes`


# Dry Run Example 1: Valid Input

**Input:**
start = 10  
end = 20

**Execution:**  
10 - Not prime  
11 - Prime  
12 - Not prime  
13 - Prime  
14 - Not prime  
15 - Not prime  
16 - Not prime  
17 - Prime  
18 - Not prime  
19 - Prime  
20 - Not prime

**Output:**  
list_primes: 11 13 17 19

# Dry Run Example 2: Invalid Range

**Input:**  
start = 50  
end = 30

**Execution:**  
Start is greater than end  

**Output:**  
Invalid range. Starting number must be less than or equal to ending number.
