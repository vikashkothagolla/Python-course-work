# 1. Reverse a string without using slicing
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


# 2. Swap two variables without using a temporary variable
def swap_variables(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]


# 4. Count occurrences of each character in a string
def char_count(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict


# 5. Factorial (iterative)
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



# 6. Generate Fibonacci sequence up to n terms
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


# 7. Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


# 8. Remove duplicates from a list without using set
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# 9. Find largest number in a list without using max()
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest



# 10. Implement your own map() function
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
