
inventory = {
    "laptop": 10,
    "phone": 0,
    "headphones": 2,
    "monitor": 5
}

# Input product name from user
product = input("Enter the product name: ").lower()

# Check product availability
if product in inventory:
    quantity = inventory[product]
    if quantity == 0:
        print("Product is out of stock.")
    elif quantity <= 3:
        print("Product is in limited quantity.")
    else:
        print("Product is available.")
else:
    print("Product not found in inventory.")

# Sample product and user data
product_in_stock = True
is_prime_member = True
has_discount_coupon = True

# Check all conditions
if product_in_stock:
    print("Product is in stock.")
    
    if is_prime_member and has_discount_coupon:
        print("You qualify for Prime shipping and a discount!")
    elif is_prime_member:
        print("You qualify for Prime shipping.")
    elif has_discount_coupon:
        print("You qualify for a discount.")
    else:
        print("No special offers apply.")
else:
    print("Product is out of stock.")

# +ve,-ve,0
n=int(input("Enter the number:"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("Zero")  
