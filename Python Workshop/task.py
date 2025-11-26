mobile_Name="Mi Note 8 pro"
price=19999.00
isAvaiable=True
print(f"Mobile Name is :{mobile_Name}  Price:{price}")
print(type(mobile_Name))

mobile_Name="Mi Note 10 pro"
price=22999.00
isAvaiable=True
print(f"Mobile Name is :{mobile_Name}  Price:{price}")
print(type(mobile_Name))

product_Name="Laptop Bag"
price=320.00
isAvaiable=True
print(f"product name is :{product_Name}  Price:{price}")
print(type(product_Name))

product_Name="Rolex watch"
price=3200.00
isAvaiable=True
print(f"product name is :{product_Name}  Price:{price}")
print(type(product_Name))

product_Name="Laptop Bag"
price=320.00
isAvaiable=True
print(f"product name is :{product_Name}  Price:{price}")
print(type(product_Name))

product_Name="Men’s Sports Shoes"
price=1200.00
isAvaiable=True
print(f"product name is :{product_Name}  Price:{price}")
print(type(product_Name))

print("-----------------")

products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
            "Mouse", "Monitor", "Printer", "Charger", "Camera"]

print("Initial Products List:")
print(products)


products.append("Smartwatch")
print("\nAfter Appending 'Smartwatch':")
print(products)


products.remove("Tablet")
print("\nAfter Removing 'Tablet':")
print(products)


products[3] = "Bluetooth Headphones"  
print("\nAfter Updating 'Headphones' to 'Bluetooth Headphones':")
print(products)
