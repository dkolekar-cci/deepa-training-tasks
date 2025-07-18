# Task 7: ATM Simulation

## Pseudocode

**Step 1:** Initialize account balance  
`balance <- 10000`  

**Step 2:** Display menu until user chooses to exit  

**Step 3:** Prompt user to select an option (1 to 4)  

**Step 4:** Validate the menu choice  
If choice is not between 1 and 4:  
`Display "Invalid option. Please try again"`  
Then return back to Step 2  

**Step 5:** If choice is 1   
`Display current balance`   

**Step 6:** If choice is 2 then prompt user to enter deposit amount  
  If amount ≤ 0 
    `Display "Invalid amount. Please enter a positive number"`  
  Else balance <- balance + amount  
    `Display "Deposited successfully"`  
 
**Step 7:** If choice is 3 then prompt user to enter withdrawal amount  
  If amount ≤ 0 
   `Display "Invalid amount. Please enter a positive number"`  
  Else if amount > balance then 
   `display "Insufficient balance!"`  
  Else balance <- balance − amount  
    `Display "Withdrawal successful"`

**Step 8:** If choice is 4  
`Display "Thank you for using ATM"`

## Dry Run

### Example 1: Valid Operations

Step 1: balance <- 10000  

User selects: 1  
 Output: 
 `Current Balance: ₹10000.0`  

User selects 2  
 Enter amount: 2000  
  Valid amount is balance <- 10000 + 2000 = 12000  
 Output: 
 `Deposited successfully.`

User selects: 3  
Enter amount: 1500  
 balance <- 12000 − 1500 = 10500  
Output: 
`Withdrawal successful.`  

User selects: 1  
Output:
`Current Balance: ₹10500.0`  


### Example 2: Invalid Menu Choice

User selects: 9  
Output: 
`Invalid option. Please try again`  


### Example 3: Negative Deposit

User selects: 2  
Enter amount to deposit: −500  
Output: 
`Invalid amount. Please enter a positive number.`  


### Example 4: Withdraw More Than Balance

User selects: 3  
Enter amount to withdraw: 50000  
Output: 
`Insufficient balance!`
