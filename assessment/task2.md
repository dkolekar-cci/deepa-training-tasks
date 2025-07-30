# Validating brackets

create an empty list

for each char in thr string s:
  if char is an opening bracket like '(', '{' or '[':
   add to the list

  else if char is a closing bracket like ')', '}' or '[':
  Check if the last element in the list is matching with the closing part

  if it matches, remove the last open bracket
  else:
   return false

if list still contains the elements:
 return false
else:
 return true    