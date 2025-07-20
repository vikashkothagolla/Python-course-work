'''
n=5
for i in range(n):
    print(' ' * (n - i - 1) + ' * ' * ( i+1))
for i in range(n-2-i-1):
     print(' ' * (n - i - 1) + ' * ' * ( i+1))
'''
# TESTBOOK APPLICATION
product_id = int(input("Enter Product ID (Course/Test Series ID): "))
product_name = input("Enter Product Name (Course/Test Series Name): ")
price = float(input("Enter Price: "))
categories = input("Enter Categories (subjects or exams): ")
categories = [cat.strip() for cat in categories]  
available_seats = int(input("Enter Available Seats: "))
enrolled = int(input("Enter Enrolled: "))
stock_details = (available_seats, enrolled)
discount_percentage = float(input("Enter Discount Percentage: "))
features = input("Enter Product Features (Live Classes, PDFs): ")
product_features = set(feat.strip() for feat in features.split(","))  
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}
print("\n--- Product Details ---")
print(f"Product ID : {product_id}")
print(f"Product Name : {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Categories: {', '.join(categories)}")
print(f"Stock Details: Available - {stock_details[0]}, Enrolled - {stock_details[1]}")
print(f"Discount (%): {discount_percentage}%")
print(f"Product Features: {', '.join(product_features)}")
print(f"Supplier Name : {supplier_details['name']}")
print(f"Supplier Contact: {supplier_details['contact']}")
print(f"Supplier Location: {supplier_details['location']}")