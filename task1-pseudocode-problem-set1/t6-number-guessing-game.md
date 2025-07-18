# Task 6: Number Guessing Game (with Attempt Limit)

## Pseudocode

**Step 1:** Generate a random number between 1 and 100  
`secret_number <- random number between 1 and 100`  

**Step 2:** Initialize attempt count and maximum attempts  
`attempts <- 0`  
`max_attempts <- 7`  

**Step 3:** Repeat the following until the number is guessed or attempts reach 7  

    Step 3.1: Prompt user to enter a guess  

    Step 3.2: Validate if the input is an integer between 1 and 100  
     - If not valid:
        Display message: "Invalid input. Please enter an integer between 1 and 100" 
      

    Step 3.3: If valid:  
     - Increase attempts by 1  
     - If guess = secret_number - Display: "Correct" and stop  
     - If guess < secret_number - Display: "Too low"  
     - If guess > secret_number - Display: "Too high"  

**Step 4:** If all 7 valid attempts are used and number not guessed  
`Display: "You've used all attempts. The number was secret_number"`


## Dry Run

### Example 1 (secret_number = 45)

Step 1: secret_number is 45  
Step 2: attempts = 0  

Attempt 1: 30
`Output: Too low`  
Attempt 2: 60
`Output: Too high`  
Attempt 3: 45.
`Output: Correct! You guessed the number`  


### Example 2 (secret_number = 72)

Step 1: secret_number is 72  
Step 2: attempts = 0  

Attempt 1: 30  
 `Output: Too low`  
Attempt 2: 40  
 `Output: Too low`  
Attempt 3: 50  
 `Output: Too low`  
Attempt 4: 60  
 `Output: Too low`  
Attempt 5: 75  
 `Output: Too high`  
Attempt 6: 73  
 `Output: Too high`  
Attempt 7: 71  
 `Output: Too low`  

All attempts used. Output: The number was 72  

### Example 3 (secret_number = 72)

Step 1: secret_number is 72  
Step 2: attempts = 0  

Attempt 1: User enters "hello".
`Invalid input. Please enter an integer between 1 and 100` 

Attempt 1: User enters 105. Invalid input. 
`Invalid input. Please enter an integer between 1 and 100`

Attempt 1: User enters 50. 
`Output: Too low`  


