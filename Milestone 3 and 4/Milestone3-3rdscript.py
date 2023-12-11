#Faith Siebert,Levonte Abercrombie, George Higginbotham
#12/5/2023
#Milestone3 Script 3
# Program connects to a database then preforms a select statement that returns all inventory items that are over 5 years old.
import mysql.connector
from mysql.connector import Error

config = {
    "user": "root",
    "password": "sesame",
    "host": "localhost",
    "database": "outland",
    "raise_on_warnings": True,
    "port": 3308

}
db = mysql.connector.connect(**config)
# Create a cursor object
cursor = db.cursor()

# Query 1: Select all the fields for the studio table
print("Displaying Records of Products that are 5 or more years older")

cursor.execute("SELECT p.product_name, p.year,p.unit_price,s.company_name FROM product p INNER JOIN supplier s ON p.supplier_id=s.supplier_id WHERE p.year <= CURRENT_DATE() -5")
products = cursor.fetchall()

for product in products:
    print("Product Name: {}\n Year: {}\n Price: {}\n Company Name: {}\n".format(product[0], product[1], product[2], product[3]))

cursor.close()
db.close()