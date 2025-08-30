import math
import ast

# ---------- Q1 ----------
def add_two_numbers():
    a, b = map(int, input("Enter two numbers: ").split())
    print("The sum is:", a + b)
add_two_numbers()
# ---------- Q2 ----------
def square_number():
    n = int(input("Enter a number: "))
    print("The square is:", n ** 2)
square_number()
# ---------- Q3 ----------
def area_of_circle():
    r = float(input("Enter radius: "))
    print("Area of circle is:", round(3.14 * r * r, 2))
area_of_circle()
# ---------- Q4 ----------
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
greet_user()    

# ---------- Q5 ----------
def celsius_to_fahrenheit():
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", (c * 9 / 5) + 32)
celsius_to_fahrenheit()
# ---------- Q6 ----------
def multiply_three_numbers():
    a, b, c = map(int, input("Enter three numbers: ").split())
    print("Product is:", a * b * c)
multiply_three_numbers()
# ---------- Q7 ----------
def simple_interest():
    p, r, t = map(float, input("Enter Principal, Rate, and Time: ").split())
    print("Simple Interest is:", (p * r * t) / 100)
simple_interest()
# ---------- Q8 ----------
def length_of_string():
    s = input("Enter a string: ")
    print("Length of string is:", len(s))
length_of_string()
# ---------- Q9 ----------
def append_to_list():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    elem = int(input("Enter element to append: "))
    lst.append(elem)
    print("Updated list:", lst)
append_to_list()
# ---------- Q10 ----------
def double_each_element():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Doubled list:", [x * 2 for x in lst])
double_each_element()
# ---------- Q11 ----------
def sort_list():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Sorted list:", sorted(lst))
sort_list()
# ---------- Q12 ----------
def clear_list():
    lst = list(map(int, input("Enter list elements: ").split()))
    lst.clear()
    print("Cleared list:", lst)
clear_list()
# ---------- Q13 ----------
def update_dictionary_value():
    d = ast.literal_eval(input("Enter dictionary: "))
    key = input("Enter key to update: ")
    val = ast.literal_eval(input("Enter new value: "))
    d[key] = val
    print("Updated dictionary:", d)
update_dictionary_value()
# ---------- Q14 ----------
def remove_element_by_value():
    lst = list(map(int, input("Enter list elements: ").split()))
    elem = int(input("Enter element to remove: "))
    if elem in lst:
        lst.remove(elem)
    print("Updated list:", lst)
remove_element_by_value()
# ---------- Q15 ----------
def add_key_to_dictionary():
    d = ast.literal_eval(input("Enter dictionary: "))
    key = input("Enter new key: ")
    val = ast.literal_eval(input("Enter new value: "))
    d[key] = val
    print("Updated dictionary:", d)
add_key_to_dictionary
# ---------- Q16 ----------
def increment_dict_values():
    d = ast.literal_eval(input("Enter dictionary: "))
    print("Updated dictionary:", {k: v + 1 for k, v in d.items()})
increment_dict_values()
# ---------- Q17 ----------
def factorial_number():
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)
    n = int(input("Enter a number: "))
    print("Factorial is:", factorial(n))
factorial_number()
# ---------- Q18 ----------
def fibonacci_nth():
    def fib(n):
        return n if n <= 1 else fib(n - 1) + fib(n - 2)
    n = int(input("Enter term number: "))
    print("Fibonacci number is:", fib(n))
fibonacci_nth()
# ---------- Q19 ----------
def sum_first_n_numbers():
    n = int(input("Enter a number: "))
    print("Sum is:", n * (n + 1) // 2)
sum_first_n_numbers()
# ---------- Q20 ----------
def reverse_string_recursion():
    def reverse(s):
        return s if len(s) <= 1 else reverse(s[1:]) + s[0]
    s = input("Enter a string: ")
    print("Reversed string is:", reverse(s))
reverse_string_recursion()
# ---------- Q21 ----------
def power_recursive():
    def power(a, b):
        return 1 if b == 0 else a * power(a, b - 1)
    a, b = map(int, input("Enter base and exponent: ").split())
    print("Result is:", power(a, b))
power_recursive()
# ---------- Q22 ----------
def sum_digits_recursion():
    def sum_digits(n):
        return 0 if n == 0 else n % 10 + sum_digits(n // 10)
    n = int(input("Enter a number: "))
    print("Sum of digits:", sum_digits(n))
sum_digits_recursion()
# ---------- Q23 ----------
def is_palindrome_recursion():
    def is_palindrome(s):
        return True if len(s) <= 1 else s[0] == s[-1] and is_palindrome(s[1:-1])
    s = input("Enter a string: ")
    print("Is palindrome:", is_palindrome(s))
is_palindrome_recursion
# ---------- Q24 ----------
def gcd_recursion():
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    a, b = map(int, input("Enter two numbers: ").split())
    print("GCD is:", gcd(a, b))
gcd_recursion()
# ---------- Q25 ----------
def max_of_three():
    a, b, c = map(int, input("Enter three numbers: ").split())
    print("Maximum is:", max(a, b, c))
max_of_three()
# ---------- Q26 ----------
def sort_list_again():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Sorted list:", sorted(lst))
sort_list_again()
# ---------- Q27 ----------
def sum_of_list():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Sum of list is:", sum(lst))
sum_of_list()
# ---------- Q28 ----------
def find_data_type():
    val = ast.literal_eval(input("Enter any value: "))
    print("Data type is:", type(val))
find_data_type()    

# ---------- Q29 ----------
def print_even_numbers():
    n = int(input("Enter a number: "))
    print("Even numbers:", *[i for i in range(0, n + 1, 2)])
print_even_numbers()
# ---------- Q30 ----------
def list_of_squares():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Squared list:", [x ** 2 for x in lst])
list_of_squares()
# ---------- Q31 ----------
def check_prime():
    n = int(input("Enter a number: "))
    if n < 2:
        print("Is prime:", False)
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print("Is prime:", False)
                return
        print("Is prime:", True)
check_prime()
# ---------- Q32 ----------
def count_vowels():
    s = input("Enter a string: ")
    print("Number of vowels:", sum(1 for ch in s.lower() if ch in 'aeiou'))
count_vowels()
# ---------- Q33 ----------
def multiply_by_2_lambda():
    n = int(input("Enter a number: "))
    print("Result:", (lambda x: x * 2)(n))
multiply_by_2_lambda()
# ---------- Q34 ----------
def square_list_lambda():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Squared list:", list(map(lambda x: x ** 2, lst)))
square_list_lambda()
# ---------- Q35 ----------
def filter_even_lambda():
    lst = list(map(int, input("Enter list elements: ").split()))
    print("Even numbers:", list(filter(lambda x: x % 2 == 0, lst)))
filter_even_lambda()
# ---------- Q36 ----------
def sort_tuples_by_second():
    lst = ast.literal_eval(input("Enter list of tuples: "))
    print("Sorted list:", sorted(lst, key=lambda x: x[1]))
sort_tuples_by_second()
# ---------- Q37 ----------
def access_global_var():
    global_var = "Hello"
    def func():
        return global_var
    print("Global variable value is:", func())
access_global_var()
# ---------- Q38 ----------
global_var = "Hello"
def modify_global_var():
    global global_var
    def func():
        global global_var
        global_var = "Changed"
    func()
    print("Modified global variable is:", global_var)
modify_global_var()
# ---------- Q39 ----------
def local_vs_global():
    x = "Global"
    def func():
        x = "Local"
        print("Inside function:", x)
    func()
    print("Outside function:", x)
local_vs_global()
# ---------- Q40 ----------
def compare_globals_and_locals():
    x = 10
    def func():
        x = 20
        print("Local x:", x)
    print("Global x:", x)
    func()
compare_globals_and_locals()