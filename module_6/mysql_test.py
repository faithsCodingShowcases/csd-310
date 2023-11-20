import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "root",
    "password": "sesame",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True,
    "port": 3308

}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue....")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        PRINT(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database doesnt exist")

    else:
        print(err)
    db.close()
