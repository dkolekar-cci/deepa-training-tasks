# Task 1: Triplet sum

**Step-1:** First sort the input array numbers

**Step-2:** Then create an empty list to store the values

**Step-3:** Loop through the array

**Step-4:** For each i, set 2 index

left=i+1

right=len(nums)-1

**Step-5:** When left< right
Cal the sum as nums[i]+nums[left]+nums[right]

    if sum is 0 
    we then add the triplet to the result

    Then we move both left and right to skip the dups

    if sum<0 then we increase left 
    if sum>0 then decrease right one

**Step 6:** return the list    
