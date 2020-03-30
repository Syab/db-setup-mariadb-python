import time
import logging
import mysql.connector as mariadb
from mysql.connector import errorcode
from config import dbhost, dbuser, dbport, dbpw, dbname

start = time.time()
config = {
    'user': dbuser,
    'password': dbpw,
    'host': dbhost,
    'port': dbport,
    'database': dbname
}

cnx = mariadb.connect(**config)
cursor = cnx.cursor()
db_name = dbname

TABLES = {}
TABLES['url_store'] = (
    "CREATE TABLE `url_store` ("
    "_id int(11) AUTO_INCREMENT PRIMARY KEY,"
    "`long_url` text NOT NULL,"
    "`short_url` text NOT NULL,"
    "`time_created` datetime DEFAULT current_timestamp() NOT NULL"
    ");"
)

def check_db():
    try:
        cursor.execute("USE {}".format(db_name))
        print("Database {} exists.".format(db_name))
    except mariadb.Error as err:
        print("Database {} does not exist.".format(db_name))
        print(err)
        exit(1)

def create_tables():
    print("create table")
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        
        except mariadb.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("{} exists".format(table_name))
            else:
                print(err.msg)


check_db()
create_tables()

cursor.close()
cnx.close()
print("Total execution time {0:0.3f} seconds".format(time.time() - start))        