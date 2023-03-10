import mysql.connector as mysql
from mysql.connector import Error
from dotenv import load_dotenv 
import os

load_dotenv()

DB_Password = os.getenv("DB_PASSWORD")
DB_user = os.getenv("DB_USER")

try:
    mydb = mysql.connect(
            host="localhost",
            user=DB_user,
            password=DB_Password,
            PORT=3306
        )   
    if mydb.is_connected():
        #Making MYSQL COnnection
        mycursor = mydb.cursor()
        #Creating MYSQL DB
        mycursor.excecute("CREATE DATABASE YT_DB")
        print('Database is created...')
except Error as e:
    #Error is connection was not made
    print("Error while connecting to MYSQL")