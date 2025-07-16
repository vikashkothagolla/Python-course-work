# Pharmacy Management System - Medicine Entry

medicineid = int(input("Enter medicine ID: "))
medicinename = input("Enter medicine Name: ")
price= float(input("Enter medicine Price: "))
categories = input("Enter medicine Categories (comma-separated): ").split(",")
availablestock = int(input("Enter available Stock: "))
sold_items = int(input("Enter Sold Units: "))
stockdetails = (availablestock, sold_items)
discount = float(input("Enter discount percentage: "))
features_input = input("Enter medicine features: ")
medicinefeatures = set(features_input.split(","))

batchnumber = input("Enter batch number: ")
expirydate = input("Enter Expiry Date:")

suppliername = input("Enter Supplier Name: ")
suppliercontact = input("Enter Supplier Contact Number: ")
supplierlocation = input("Enter Supplier Location: ")

supplier_string = "{'Name': '%s', 'Contact': '%s', 'Location': '%s'}" % (
    suppliername, suppliercontact, supplierlocation)
supplierdetails = eval(supplier_string)

print("\n[Pharmacy Product Details using %% Operator Formatting]")
print("Medicine ID: %d" % medicineid)
print("Medicine Name: %s" % medicinename)
print("Price: ₹%.2f" % price)
print("Categories: %s" % str(categories))
print("Stock Details (Available, Sold): %s" % str(stockdetails))
print("Discount: %.2f%%" % discount)
print("Medicine Features: %s" % str(medicinefeatures))
print("Batch Number: %s" % batchnumber)
print("Expiry Date: %s" % expirydate)
print("Supplier Details: %s" % str(supplierdetails))
