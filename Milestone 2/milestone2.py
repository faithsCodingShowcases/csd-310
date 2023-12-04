# Faith Siebert, Levonte Abercrombie, George Higginbotham
# 12/3/2023
#Milestone 2
# Program creates tables, inserts records for each table, then shows them back to the user


import mysql.connector


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



cursor.execute("CREATE TABLE staff (staff_id int not null auto_increment PRIMARY KEY,first_name varchar(30) not null,last_name varchar(30) not null, title varchar(30) not null,  email varchar(50) not null, phone_number varchar(12) not null, address varchar(50) not null, city varchar(30) not null, state varchar(30) not null, zip int not null, country varchar(30) not null, birth_date DATE not null, hire_date DATE not null)")

cursor.execute("CREATE TABLE customer(customer_id int not null auto_increment PRIMARY KEY, first_name varchar(30), last_name varchar(30), email varchar(50), phone_number varchar(12), address varchar(50), city varchar(30), state varchar(30), zip int, country varchar(30), birth_date DATE)")

cursor.execute("CREATE TABLE supplier(supplier_id int not null auto_increment PRIMARY KEY, company_name varchar(30) not null, contact_name varchar(30), email varchar(50) not null, phone_number varchar(12) not null, address varchar(50) not null, city varchar(30) not null, state varchar(30) not null, zip int not null, country varchar(30) not null)")

cursor.execute("CREATE TABLE `order`(order_id int not null auto_increment PRIMARY KEY, customer_id int not null, ship_address varchar(50), ship_city varchar(30), ship_state varchar(30), ship_zip int, ship_country varchar(30), order_date DATE not null, shipped_date DATE, required_date DATE)")
cursor.execute("CREATE TABLE `order_details`(order_id int not null, product_id int not null , unit_price DECIMAL(10,2) not null, quantity int not null,discount DECIMAL(10,2) not null)")


cursor.execute("CREATE TABLE product(product_id int not null auto_increment PRIMARY KEY, supplier_id int not null, category_id int not null, product_name varchar(50) not null,year int not null, unit_price DECIMAL(10,2) not null, unit_stock int not null, discount DECIMAL(10,2) not null)")
cursor.execute("CREATE TABLE trip (trip_id int not null auto_increment PRIMARY KEY, staff_id int not null, customer_id int not null, address varchar(50) not null, city varchar(30) not null, state varchar(30), zip int not null, country varchar(30) not null, start_date DATE not null, end_date DATE not null)")


cursor.execute("CREATE TABLE category(category_id int not null auto_increment PRIMARY KEY, category_name varchar(30) not null, category_discription varchar(300) not null)")

# Adding foreign key constraints
cursor.execute("ALTER TABLE `order` ADD CONSTRAINT customer_id FOREIGN KEY (customer_id) REFERENCES customer (customer_id)")
cursor.execute("ALTER TABLE product ADD CONSTRAINT supplier_id FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id)")
cursor.execute("ALTER TABLE product ADD CONSTRAINT category_id FOREIGN KEY (category_id) REFERENCES category (category_id)")
cursor.execute("ALTER TABLE trip ADD CONSTRAINT staff_id FOREIGN KEY (staff_id) REFERENCES staff (staff_id)")
cursor.execute("ALTER TABLE trip ADD CONSTRAINT customer_id_fk FOREIGN KEY (customer_id) REFERENCES customer (customer_id)")


#inserts record for staff
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('John','MacNell','Guide','John12389@gmail.com','705-603-8788','955 East Cherry Street', 'Denver', 'Colorado', 80012,'United States','1980-12-17','2010-2-15')")
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('Duke','Marlin','Guide','duke777564@gmail.com','766-687-9876','877 Hopper Lane', 'Denver', 'Colorado', 80012,'United States','1990-10-17','2010-2-20')")
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('Anita','Gallegos','Marketing','Anita909786@gmail.com','705-603-7563','822 Road Drive', 'Denver', 'Colorado', 80012,'United States','1989-9-14','2010-3-8')")
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('Dimitrios','Stravopolus','Inventory','Dimitry54332@gmail.com','705-603-0043','908 Elm Street', 'Denver', 'Colorado', 80012,'United States','1993-4-6','2010-3-4')")
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('Blythe','Timmerson','Owner','BlyTim7382@outland.com','705-603-7438','745 Black Horse Yard', 'Denver', 'Colorado', 80012,'United States','1994-1-19','2023-11-25')")
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('Jim','Ford','Owner','JimFord732@outland.com','705-603-6654','722 Ferry Row', 'Denver', 'Colorado', 80012,'United States','1983-3-27','2010-1-4')")
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('Mei','Wong','Developer','Mei5738@gmail.com','705-603-9934','556 Harbor Row', 'Denver', 'Colorado', 80012,'United States','1979-4-18','2010-1-4')")

#inserts record for customer
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Sophie','Johnson','John12389@gmail.com','705-603-3342','778 East Carlton Street', 'Denver', 'Colorado', 80012,'United States','1998-5-20')")
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Maria','White', 'Maria83423@gmail.com','705-603-1123','554 Winter Way', 'Denver', 'Colorado', 80012,'United States','2001-4-26')")
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Cole','Vanwhite','coliscool43@gmail.com','705-603-6654','879 Long Avenue', 'Castle Rock', 'Colorado', 80104,'United States','1999-4-11')")
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Mathew','Harpper','mattHarp76@gmail.com','833-654-5767','124 Clown Street', 'Edgewater', 'Colorado', 80214,'United States','1970-1-30')")
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Dale','Diamante','Dale4thewin@gmail.com','967-777-2435','895 Fletcher Route', 'Broomfield', 'Colorado', 80020,'United States','1996-12-1')")
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Murphy','Douglas','murpgothup78@gmail.com','899-987-8948','666 Steam Lane', 'Commerce City', 'Colorado', 80022,'United States','1987-11-12')")

#inserts record for supplier
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('Mal & Co','Dean Striffer','deanStriff77@MalCo.com','765-780-5625','878 Silver Avenue', 'New York', 'New York', 10001,'United States')")
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('Mysterious Inc','Dani Blom','DaniBlom65@MysteriousInc.com','879-888-9654','999 Gilded Row', 'Orlando', 'Florida', 32801,'United States')")
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('Hike Corp','Carl Nork','CarlNork@HikeCorp.com','254-545-6874','201 Willow Way', 'Los Angeles', 'California', 90002,'United States')")
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('Mountain & Malis','Tiff Johnson','tiffJohnson@mountainMalis.com','874-654-8954','878 North Passage', 'Chicago', 'Illinos', 60601,'United States')")
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('REI Co-op','Clide Dickson','clidedickson76@reico.com','664-542-8865','354 Fermaon Street', 'Houston', 'Texas', 77001,'United States')")
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('Tent Express','Marrie Woods','mariewoods@tentexpress.com','954-555-6214','221 Quarry Passage', 'Bismark', 'North Dakota', 58501,'United States')")



#inserts record for category
cursor.execute("INSERT INTO category(category_name, category_discription) VALUES('Hiking','Includes all basic equipment needed for hiking on various landsapes.')")
cursor.execute("INSERT INTO category(category_name, category_discription) VALUES('Camping','Includes all basic equipment needed for camping on various landsapes.')")
cursor.execute("INSERT INTO category(category_name, category_discription) VALUES('Winter Appearal','Warm clothing best fitted for cold environments.')")
cursor.execute("INSERT INTO category(category_name, category_discription) VALUES('Summer Apperal','Cool clothing best fitted for warm environments')")
cursor.execute("INSERT INTO category(category_name, category_discription) VALUES('Hand Tool','Includes all basic hand tools for various tasks')")
cursor.execute("INSERT INTO category(category_name, category_discription) VALUES('Survival','Essential tools needed to survive in the wilderness for days at a time')")

#inserts record for product
cursor.execute("INSERT INTO product(supplier_id, category_id, product_name,year, unit_price, unit_stock, discount) VALUES(1, 2,'Large Four Person Tent',2010,355.87,10, 0.00)")
cursor.execute("INSERT INTO product(supplier_id, category_id, product_name,year, unit_price, unit_stock, discount) VALUES(2, 1,'Trekking Pole',2010,56.99,25, 3.00)")
cursor.execute("INSERT INTO product(supplier_id, category_id, product_name,year, unit_price, unit_stock, discount) VALUES(3, 4,'Lightweight Camo Tee',2018,24.99,24, 0.00)")
cursor.execute("INSERT INTO product(supplier_id, category_id, product_name,year, unit_price, unit_stock, discount) VALUES(4, 3,'Breathable Thermal Coat',2019,150.80,15, 20.00)")
cursor.execute("INSERT INTO product(supplier_id, category_id, product_name,year, unit_price, unit_stock, discount) VALUES(5, 5,'Pocket knife',2022,36.20,15, 0.00)")
cursor.execute("INSERT INTO product(supplier_id, category_id, product_name,year, unit_price, unit_stock, discount) VALUES(6, 6,'MRE',2020,10.65,30, 0.00)")

#inserts record for trip
cursor.execute("INSERT INTO trip (staff_id, customer_id, address, city, zip, country, start_date, end_date) VALUES(1, 4,'Lot 21 Mdoni Road', 'Mtubatuba', 3935,'South Africa','2011-5-10', '2011-5-20')")
cursor.execute("INSERT INTO trip (staff_id, customer_id, address, city, state, zip, country, start_date, end_date) VALUES(2, 6,'No.15, Pingxiliang 7th Alley', 'Urumqi', 'Xinjiang Uygur', 80012,'China','2011-5-20', '2011-5-30')")
cursor.execute("INSERT INTO trip (staff_id, customer_id, address, city, state, zip, country, start_date, end_date) VALUES(1, 3,'Farm bassora', 'Broederstroom', 'Bojanala', 0240,'South Africa','2013-7-10', '2013-7-20')")
cursor.execute("INSERT INTO trip (staff_id, customer_id, address, city, zip, country, start_date, end_date) VALUES(2, 4,'Youhao North Road 370 Haobei Goat Outdoor', 'Urumqi, Xinjiang', 5113,'China','2013-6-30', '2013-7-10')")
cursor.execute("INSERT INTO trip (staff_id, customer_id, address, city, state, zip, country, start_date, end_date) VALUES(1, 6,'Dame Gruev Steet', 'Demir Kapija', 'Demir Kapija Municipality', 1442,'North Macedonia','2015-7-14', '2015-7-24')")
cursor.execute("INSERT INTO trip (staff_id, customer_id, address, city, state, zip, country, start_date, end_date) VALUES(2, 4,'25 Ul. 19 Pazardzhik 4400 Dabravite', 'Denver', 'Pazardzhik', 2200,'Bulgaria','1998-8-14', '2015-8-24')")

#inserts record for order
cursor.execute("INSERT INTO `order`(customer_id, order_date) VALUES(1,'2018-4-20')")
cursor.execute("INSERT INTO `order`(customer_id, order_date) VALUES(2,'2022-1-10')")
cursor.execute("INSERT INTO `order`(customer_id, order_date) VALUES(3,'2010-7-15')")
cursor.execute("INSERT INTO `order`(customer_id, order_date) VALUES(4,'2015-5-13')")
cursor.execute("INSERT INTO `order`(customer_id, order_date) VALUES(5,'2018-9-16')")
cursor.execute("INSERT INTO `order`(customer_id, order_date) VALUES(6,'2022-12-21')")

#inserts record for order_details
cursor.execute("INSERT INTO order_details(order_id, product_id, unit_price, quantity ,discount) VALUES(1, 2, 56.99,1, 3.00)")
cursor.execute("INSERT INTO order_details(order_id, product_id, unit_price, quantity ,discount) VALUES(2, 4,150.80,30, 20.00)")
cursor.execute("INSERT INTO order_details(order_id, product_id, unit_price, quantity ,discount) VALUES(3, 6,10.65,5, 0.00)")
cursor.execute("INSERT INTO order_details(order_id, product_id, unit_price, quantity ,discount) VALUES(4, 1,355.87,1, 0.00)")
cursor.execute("INSERT INTO order_details(order_id, product_id, unit_price, quantity ,discount) VALUES(5, 6,10.65,3, 0.00)")
cursor.execute("INSERT INTO order_details(order_id, product_id, unit_price, quantity ,discount) VALUES(6, 4,150.80,1, 20.00)")




# Query 1: Select all the fields for the studio table
print("SHOWING ALL RECORDS FROM THE CUSTOMER TABLE")
cursor.execute("SELECT * FROM customer")
customers = cursor.fetchall()
for customer in customers:
    print("Customer ID: {}\n First Name: {}\n Last Name: {}\n Email: {}\n Phone Number: {}\n Address: {}\n City: {}\n State: {}\n Zip: {}\n Country: {}\n Birth Date: {}\n".format(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7], customer[8], customer[9], customer[10]))


print("SHOWING ALL RECORDS FROM THE STAFF TABLE")
cursor.execute("SELECT * FROM staff")
staffs = cursor.fetchall()
for staff in staffs:
    print("Staff ID: {}\n First Name: {}\n Last Name: {}\n Title: {}\n Email: {}\n Phone Number: {}\n Address: {}\n City: {}\n State: {}\n Zip: {}\n Country: {}\n Birth Date: {}\n Hire Date: {}\n".format(staff[0], staff[1], staff[2], staff[3], staff[4], staff[5], staff[6], staff[7], staff[8], staff[9], staff[10], staff[11], staff[12]))

print("SHOWING ALL RECORDS FROM THE SUPPLIER TABLE")
cursor.execute("SELECT * FROM supplier")
suppliers = cursor.fetchall()
for supplier in suppliers:
    print("Supplier ID: {}\n Company Name: {}\n Contact Name: {}\n Email: {}\n Phone Number: {}\n Address: {}\n City: {}\n State: {}\n Zip: {}\n Country: {}\n".format(supplier[0], supplier[1], supplier[2], supplier[3], supplier[4], supplier[5], supplier[6], supplier[7], supplier[8], supplier[9]))

print("SHOWING ALL RECORDS FROM THE CATEGORY TABLE")
cursor.execute("SELECT * FROM category")
categorys = cursor.fetchall()
for category in categorys:
    print("Category ID: {}\n Category Name: {}\n Category Description: {}\n".format(category[0], category[1], category[2]))

print("SHOWING ALL RECORDS FROM THE PRODUCT TABLE")
cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
for product in products:
    print("Product ID: {}\n Supplier ID: {}\n Category ID: {}\n Product Name: {}\n Year: {}\n Unit Price: {}\n Unit Stock: {}\n Discount: {}\n".format(product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7]))


print("SHOWING ALL RECORDS FROM THE TRIP TABLE")
cursor.execute("SELECT * FROM trip")
trips = cursor.fetchall()
for trip in trips:
    print("Trip ID: {}\n Staff ID: {}\n Customer ID: {}\n Address: {}\n City: {}\n State: {}\n Zip: {}\n Country: {}\n Start Date: {}\n End Date: {}\n".format(trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6], trip[7], trip[8], trip[9]))

print("SHOWING ALL RECORDS FROM THE ORDER TABLE")
cursor.execute("SELECT * FROM `order`")
orders = cursor.fetchall()
for order in orders:
    print("Order ID: {}\n Customer ID: {}\n Ship Address: {}\n Ship City: {}\n Ship State: {}\n Ship Zip: {}\n Ship Country: {}\n Order Date: {}\n Shipped Date: {}\n Required Date: {}\n".format(order[0], order[1], order[2], order[3], order[4], order[5], order[6], order[7], order[8], order[9]))

print("SHOWING ALL RECORDS FROM THE ORDER DETAILS TABLE")
cursor.execute("SELECT * FROM order_details")
details = cursor.fetchall()
for detail in details:
    print("Order ID: {}\n Product ID: {}\n Unit Price: {}\n Quantity: {}\n Discount: {}\n".format(detail[0], detail[1], detail[2], detail[3], detail[4]))
cursor.close()
db.close()





