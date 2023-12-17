
import mysql.connector


config = {

    "user": "user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "outland",
    "raise_on_warnings": True

}

db = mysql.connector.connect(*config)
cursor = db.cursor()

cursor.execute("SELECT product_id, SUM( quantity (unit_price - discount)) AS product_sales "
               "FROM order_details "
               "GROUP BY product_id;")

product_sales = cursor.fetchall()
for sale in product_sales:
    print("Product ID: {}\nTotal Product Sales: {}\n".format(sale[0], sale[1]))

cursor.execute("SELECT SUM(quantity * (unit_price - discount)) AS total_sales FROM order_details;")
total_sales = cursor.fetchall()
for sale in total_sales:
    print("Total Overall Sales: {}".format(sale[0]))

cursor.execute("SELECT t1.product_id, t2.product_id "
               "FROM order_details t1 "
               "RIGHT JOIN product t2 "
               "ON t1.product_id = t2.product_id "
               " GROUP BY t2.product_id;")
table = cursor.fetchall()
for column in table:
    if column[0] is None:
        print(f"Product {column[1]} has no orders.")

cursor.close()
db.close()
