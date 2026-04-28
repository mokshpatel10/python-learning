#Question 1
#Part 2
#Beginner

def sum_natural(n):
    if n <= 1:
        return n
    return n + sum_natural(n - 1)

print(sum_natural(5))   
print(sum_natural(10)) 
print(sum_natural(1))  

#Intermediate

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(1234))    
print(count_digits(987654321)) 
print(count_digits(5))    

#Advanced

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))                    
print(is_palindrome("hello"))                      
print(is_palindrome("a"))                          
print(is_palindrome("A man a plan a canal Panama")) 
print(is_palindrome("race a car"))      




#Part 4
#Beginner

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 5))  
print(power(3, 0))  
print(power(5, 3))         

#Intermediate

def generate_binary_strings(n):
    result = []

    def backtrack(current):
        if len(current) == n:
            result.append(current)
            return
        
        backtrack(current + '0')
        
        backtrack(current + '1')
    
    backtrack("")  
    return result    

print(generate_binary_strings(2))
print(generate_binary_strings(1))

#Advanced

def subset_sum(nums, target):
    def backtrack(index, current_sum):
        if current_sum == target:
            return True
        if index == len(nums):
            return False
        
        if backtrack(index + 1, current_sum + nums[index]):
            return True
        
        if backtrack(index + 1, current_sum):
            return True
        
        return False

    return backtrack(0, 0)
print(subset_sum([3, 34, 4, 12, 5, 2], 9))   
print(subset_sum([1, 2, 3, 4], 10))         
print(subset_sum([1, 2, 3], 7))             




#Part 5
#Beginner

def recursive_sum(arr, n):
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)
# Questions to answer:
# 1. Write the recurrence relation for time complexity
#Ans: T(0) = O(1)
# 2. What is the time complexity? O(?)
#Ans: O(n)
# 3. What is the space complexity? O(?)
#Ans: O(n)
# 4. Draw the recursion tree for recursive_sum([1,2,3,4], 4)
""" 
Ans: recursive_sum([1,2,3,4], 4)
├── 4 + recursive_sum([1,2,3,4], 3)
├── 3 + recursive_sum([1,2,3,4], 2)
├── 2 + recursive_sum([1,2,3,4], 1)
├── 1 + recursive_sum([1,2,3,4], 0)
└── 0 (base case)
"""

#Intermediate

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
    
    #Recursion Relation
    #Ans: O(1)
    #Time Complexity
    #Ans: n/2k=1⇒k=log2​n
    #     =O(log n)
    #Compare space complexity with iterative version
    """def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1
    """
    
#Advanced

def edit_distance(s1, s2):
    def helper(i, j):
        if i == 0:
            return j 
        if j == 0:
            return i 

        if s1[i-1] == s2[j-1]:
            return helper(i-1, j-1)
        
        insert = helper(i, j-1)
        delete = helper(i-1, j)
        replace = helper(i-1, j-1)
        
        return 1 + min(insert, delete, replace)
    
    return helper(len(s1), len(s2))

    # 2. Because of overlapping subproblems.
    # 3:
    
def edit_distance(s1, s2):
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base cases
        if i == 0:
            return j
        if j == 0:
            return i
        
        if s1[i-1] == s2[j-1]:
            memo[(i, j)] = helper(i-1, j-1)
        else:
            insert = helper(i, j-1)
            delete = helper(i-1, j)
            replace = helper(i-1, j-1)
            
            memo[(i, j)] = 1 + min(insert, delete, replace)
        
        return memo[(i, j)]
    
    return helper(len(s1), len(s2))

    # 4: Memo table: O(m x n)
    #    Recursion stack: O(m + n)
    
    
    
    
    
    
    
# Question 2

import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [random.randint(0, 10**6) for _ in range(10**6)]

sorted_arr = merge_sort(arr)

    # Complexity: Merge sort runs in O(n log n) time because it repeatedly divides the array into halves (which takes log n levels) and performs a linear-time merge (O(n)) at each level. This gives the recurrence T(n)=2T(n/2)+O(n), which solves to O(nlogn).
    
    #It is considered fast because it guarantees this performance even in the worst case, unlike some other sorting algorithms, and it processes elements in a structured, sequential way during merging, making it efficient and predictable for large datasets like 1,000,000 elements.
    
    