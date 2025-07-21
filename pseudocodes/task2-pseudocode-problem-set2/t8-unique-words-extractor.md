# Task 8: Unique Words Extractor (Set)

## Pseudocode

`Step 1:` Take input paragraph from user  
paragraph <- input  

`Step 2:` Remove punctuation (.,!?) from paragraph  

`Step 3:` Convert paragraph to lowercase  

`Step 4:` Split paragraph into list of words  
words_list <- paragraph.split()  

`Step 5:` Create a set from words_list to remove duplicates  
unique_words_set <- set(words_list)  

`Step 6:` Convert set to list and sort alphabetically  
sorted_unique_words <- sorted(list(unique_words_set))  

`Step 7:` Print sorted_unique_words  

---

## Dry Run Example

Input:  
`Hello world! Hello Python.`

Processing:  
Remove punctuation: Hello world Hello Python  
Convert to lowercase: hello world hello python  
Split into words: ['hello', 'world', 'hello', 'python']  
Convert to set: {'hello', 'world', 'python'}  
Sort alphabetically: ['hello', 'python', 'world']

Output:  
`Unique words: ['hello', 'python', 'world']`
