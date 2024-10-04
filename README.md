# inventorymanagementpython
Inventory  Management System:😊

This Python script implements a simple stock management system that allows both admin and user functionalities. It features a list of products represented as dictionaries, enabling easy updates and purchases.

Features:

Stock Representation: The stock is maintained as a list of dictionaries, with each dictionary containing details like serial number, product name, brand, quantity, and price.

Admin Functionality: Admin users can log in, view current stock, and update product quantities. They are prompted to enter their credentials and can add stock quantities for various products.

User Functionality: Regular users can log in, view the available products, and make purchases. The total amount is calculated, including a 10% GST on the total price of selected products.

Dynamic Updates: After a user makes a purchase, the stock is updated to reflect the new quantities available.


Code Structure:

Stock Data: Defined as a list of dictionaries, each representing a product.

Print Stock: A function to display the current stock in a formatted table.

Admin Function: Handles the admin login and stock updates.

User Function: Manages user login, product selection, and purchase processing.

Login Function: Determines whether to direct the user to the admin or user function based on their designation.


How to Use:

Run the script and log in as either an admin or a user.

Admins can add quantities to the existing stock.

Users can select products to purchase and receive a total bill including GST.


Future Improvements:

Implement user authentication with hashed passwords for security.

Add persistence using a database or file storage to save stock data across sessions.

Enhance user experience with a graphical user interface (GUI). 

