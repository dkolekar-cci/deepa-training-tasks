# Task 3: Reversing a String

## Pseudocode

**Step 1:** Take input for the string  
`string_input`  

**Step 2:** Initialize an empty string to store the reversed version  
`reversed_string <- ""`  

**Step 3:** Loop through the input string from the last character to the first  
add it to `reversed_string`  
**Step 4:** Return `reversed_string`  

## Dry Run

### Example 1: `string_input = "hello"`  

**Step 1:**  
Input: `hello`

**Step 2:**  
Start with `reversed_string = ""`

**Step 3:**   
 Add 'o'  `reversed_string = "o"`  
 Add 'l'  `reversed_string = "ol"`  
 Add 'l'  `reversed_string = "oll"`  
 Add 'e'  `reversed_string = "olle"`  
 Add 'h'  `reversed_string = "olleh"`

**Step 4:**  
Output: `olleh`

### Example 2: `string_input = "goa"`  

**Step 1:**  
Input= `goa`

**Step 2:**  
Start with `reversed_string = ""`

**Step 3:**  
 Add 'a'  `reversed_string = "a"`  
 Add 'o'  `reversed_string = "ao"`  
 Add 'g'  `reversed_string = "aog"`

**Step 4:**  
Output= `aog`

### Example 3: `string_input = "India"`  

**Step 1:**  
Input= `India`

**Step 2:**  
Start with `reversed_string = ""`

**Step 3:**  
 Add 'a'  `reversed_string = "a"`  
 Add 'i'  `reversed_string = "ai"`  
 Add 'd'  `reversed_string = "aid"`  
 Add 'n'  `reversed_string = "aidn"`  
 Add 'I'  `reversed_string = "aidnI"`

**Step 4:**  
Output= `aidnI`
