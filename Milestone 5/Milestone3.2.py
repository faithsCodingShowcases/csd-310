import mysql.connector
from mysql.connector import Error

# Function to establish a database connection
def connect_to_database():
    try:
        config = {
            "user": "root",
            "password": "password",
            "host": "localhost",
            "database": "outland",
            "raise_on_warnings": True,
            "port": 3306
        }
        db = mysql.connector.connect(**config)
        return db
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to select the database and print countries, start dates, and end dates for trips to a specific country
def print_country_info(country_names, region_name):
    try:
        cursor = db.cursor()

        cursor.execute("USE outland")

        # Query to fetch countries, start dates, and end dates for specific countries
        query = f"""
            SELECT country, start_date, end_date
            FROM trip
            WHERE country IN ({', '.join([f"'{country}'" for country in country_names])})
        """
        cursor.execute(query)
        result = cursor.fetchall()

        # Organize the output with custom print statements
        print(f"\n Bookings for {region_name}")
        print("{:<15} {:<15} {:<15}".format("Country", "Start Date", "End Date"))
        print("-" * 45)
        for row in result:
            country = row[0]
            start_date = row[1].strftime("%Y-%m-%d") if row[1] else "N/A"
            end_date = row[2].strftime("%Y-%m-%d") if row[2] else "N/A"
            print("{:<15} {:<15} {:<15}".format(country, start_date, end_date))

    except Error as e:
        print(f"Error fetching data: {e}")

# Connect to the database
db = connect_to_database()

if db:
    # Print countries, start dates, and end dates for trips
    print_country_info(["South Africa"], "Africa")
    print_country_info(["China"], "Asia")
    print_country_info(["North Macedonia", "Bulgaria"], "Europe")

    db.close()
