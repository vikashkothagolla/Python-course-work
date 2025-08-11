# main.py
import my_programs as mp

menu_options = {
    1: mp.reverse_string,
    2: mp.sswap_variables,
    3: mp.is_palindrome,
    4: mp.char_count,
    5: mp.factorial_iterative,
    6: mp.fibonacci,
    7: mp.are_anagrams,
    8: mp.remove_duplicates,
    9: mp.find_largest,
    10: mp.my_map,
}

def show_menu():
 print("\n------ FUNCTION MENU ------")
print("Reverse a string without using slicing")
print("Swap two variables without using a temporary variable")
print("Check if a string is a palindrome")
print("Count occurrences of each character in a string")
print("Factorial (iterative)")
print("Generate Fibonacci sequence up to n terms")
print("Check if two strings are anagrams")
print("Remove duplicates from a list without using set")
print("Find largest number in a list without using max() or min()")
print("Implement your own map() function")
print("0. Exit")
print("----------------------------")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 0:
            print("Exiting program. Goodbye!")
            break
        elif choice in menu_options:
            print()
            menu_options[choice]()
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Please enter a number between 0 and 15.")
