product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
categories = input("Enter Categories (comma-separated): ").split(",")
available_stock = int(input("Enter Available Stock: "))
sold_items = int(input("Enter Sold Items: "))
stock_details = (available_stock, sold_items)
discount = float(input("Enter Discount Percentage: "))
features_input = input("Enter Product Features (comma-separated): ")
product_features = set(features_input.split(","))

# Collect supplier info
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

# Use eval to create a dictionary (use only in safe, controlled input environments)
supplier_string = "{'Name': '%s', 'Contact': '%s', 'Location': '%s'}" % (
    supplier_name, supplier_contact, supplier_location)
supplier_details = eval(supplier_string)

# Display using % formatting
print("\n[Using %% Operator Formatting]")
print("Product ID: %d" % product_id)
print("Product Name: %s" % product_name)
print("Price: %.2f" % price)
print("Categories: %s" % str(categories))
print("Stock Details: %s" % str(stock_details))
print("Discount: %.2f%%" % discount)
print("Product Features: %s" % str(product_features))
print("Supplier Details: %s" % str(supplier_details))
