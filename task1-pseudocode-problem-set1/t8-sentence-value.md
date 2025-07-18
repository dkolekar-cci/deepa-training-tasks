# Task 8: Sentence Value

## Pseudocode

**Step-1:** Take input sentence from user  
`String sentence`  

**Step-2:** Convert entire sentence to lowercase  
`sentence <- lowercase(sentence)`  

**Step-3:** Initialize total_value to 0  
`Integer total_value <- 0`  

**Step-4:** For each character in the sentence  
For each character ch in sentence:  
  If ch is between 'a' to 'z':  
    position <- ASCII(ch) - ASCII('a') + 1  
    `total_value <- total_value + (position + 10)`  

**Step-5:** Return total value  
`Print "value of '", sentence, "' is ", total_value`

# Dry Run

## Example 1
**Input**  
sentence = "Test"  

**Convert to lowercase**  
sentence = "test"  

**Initialize**  
total_value = 0  

**Iteration over each character**  
ch = 't' position = 20 value = 30 total_value = 30  
ch = 'e' position = 5  value = 15 total_value = 45  
ch = 's' position = 19 value = 29 total_value = 74  
ch = 't' position = 20 value = 30 total_value = 104  

**Output**  
`value of 'Test' is 104`

## Example 2
**Input**  
sentence = "Hello World"  

**Convert to lowercase**  
sentence = "hello world"  

**Initialize**  
total_value = 0  

**Iteration over each character**  
ch = 'h' position = 8  value = 18 total_value = 18  
ch = 'e' position = 5  value = 15 total_value = 33  
ch = 'l' position = 12 value = 22 total_value = 55  
ch = 'l' position = 12 value = 22 total_value = 77  
ch = 'o' position = 15 value = 25 total_value = 102  
ch = ' ' skip  
ch = 'w' position = 23 value = 33 total_value = 135  
ch = 'o' position = 15 value = 25 total_value = 160  
ch = 'r' position = 18 value = 28 total_value = 188  
ch = 'l' position = 12 value = 22 total_value = 210  
ch = 'd' position = 4  value = 14 total_value = 224  

**Output**  
`value of 'Hello World' is 224`
