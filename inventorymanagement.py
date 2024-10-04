# Define the stock as a list of dictionaries
stock = [
    {"SrNo": 1, "ProductName": "Perfume", "Brand": "FOGG", "productcount": 6, "productPrice": 250},
    {"SrNo": 2, "ProductName": "Shirts", "Brand": "Monty Carlo", "productcount": 7, "productPrice": 1500},
    {"SrNo": 3, "ProductName": "Girls Top", "Brand": "Zara", "productcount": 8, "productPrice": 1200},
    {"SrNo": 4, "ProductName": "Jeans", "Brand": "Tommy", "productcount": 9, "productPrice": 2000},
    {"SrNo": 5, "ProductName": "Shoes", "Brand": "Nike", "productcount": 10, "productPrice": 3000}
]

# Print the stock details

def print_stock():
    print( "| Sr.No | Product Name | Brand        | Productcount | ProductPrice\n"
           "|-------|--------------|--------------|--------------|--------------")

# Manually print each item
    print(f"| {stock[0]['SrNo']: <5} | {stock[0]['ProductName']: <12} | {stock[0]['Brand']: <12} | {stock[0]['productcount']: <12} | Rs. {stock[0]['productPrice']: <6}")
    print(f"| {stock[1]['SrNo']: <5} | {stock[1]['ProductName']: <12} | {stock[1]['Brand']: <12} | {stock[1]['productcount']: <12} | Rs. {stock[1]['productPrice']: <6}")
    print(f"| {stock[2]['SrNo']: <5} | {stock[2]['ProductName']: <12} | {stock[2]['Brand']: <12} | {stock[2]['productcount']: <12} | Rs. {stock[2]['productPrice']: <6}")
    print(f"| {stock[3]['SrNo']: <5} | {stock[3]['ProductName']: <12} | {stock[3]['Brand']: <12} | {stock[3]['productcount']: <12} | Rs. {stock[3]['productPrice']: <6}")
    print(f"| {stock[4]['SrNo']: <5} | {stock[4]['ProductName']: <12} | {stock[4]['Brand']: <12} | {stock[4]['productcount']: <12} | Rs. {stock[4]['productPrice']: <6}")


# code to run the admin section and update the stock:
def admin():
    global stock
    username=input("enter your name")
    password=(input("enter the pass"))
    confirm_pass=(input("enter the c_pass"))
    contact=int(input("enter your cont"))
    print(f"...admin block....")
    print(f"...username is :{username}") 
    print(f"...password is :{password}")
    print(f"...c_pass is :{confirm_pass}")
    print(f"...contact is:{contact}")
    if(password==confirm_pass):
        print("logged in")
        print("current stock")
        print_stock()

        addS = int(input("Enter the quantity of shirts to add: "))
        addP = int(input("Enter the quantity of jeans to add: "))
        addG = int(input("Enter the quantity of perfumes to add: "))
        addPR = int(input("Enter the quantity of girls' tops to add: "))
        addSH = int(input("Enter the quantity of shoes to add: "))

        stock[0]['productcount'] += addG
        stock[1]['productcount'] += addS
        stock[2]['productcount'] += addPR
        stock[3]['productcount'] += addP
        stock[4]['productcount'] += addSH
        
        print("....................UPDATED STOCK..........\n"
      "| Sr.No | Product Name | Brand        | Productcount | ProductPrice\n"
      "|-------|--------------|--------------|--------------|--------------")
        print_stock()
        
       
    else:
        print("wrong password ")    
          
       

# code to run the user section and buy products 

def user():
    global stock
    username = input("Enter your name: ")
    contact = input("Enter your contact: ")
    print(f"... Username is: {username}")
    print(f"... Contact is: {contact}")
    print_stock()

    print("......... Bill Payment ........")

    # Predefined product options with prices
    product_options = {
        "shirt": 1500,
        "girls top": 1200,
        "jeans": 2000,
        "perfume": 250,
        "shoes": 3000
    }

    # Initialize lists to store selected product details
    selected_products = []
    product_counts = []

    # Display available products
    print("Available Products:")
    for product, price in product_options.items():
        print(f"{product.title()} - Rs. {price}")

    while True:
        product_name = input("Enter the name of the product (or 'done' to finish): ").lower()
        if product_name == 'done':
            break
        if product_name in product_options:
            product_count = int(input(f"Enter the quantity for {product_name}: "))
            selected_products.append(product_name)
            product_counts.append(product_count)
        else:
            print("Invalid product name, please try again.")

    # Calculate total amount
    total_amount = sum(product_options[name] * count for name, count in zip(selected_products, product_counts))
    GST = 0.10
    gst_amount = total_amount * GST
    total_bill = total_amount + gst_amount


    print(f"... The total amount for all products is: {total_bill}")
    
   # Update stock based on selected products
    for i in range(len(selected_products)):
        name = selected_products[i]
        count = product_counts[i]

    # Find the index of the product in the stock
        index = list(product_options.keys()).index(name)
        stock[index]['productcount'] -= count

    print(".................... STOCK LEFT..........\n")
    print_stock()
   
    
#call the function :  
def login():   
    userdesignation =input("enter the userdesignation  admin or user : ")
    print(f"............the desegination of user is:{userdesignation}..............")
    if (userdesignation=="admin"):
      admin()
    elif (userdesignation=="user"):
      user()
    else:
        print("........no specific designation.......")  
login()    




