import mysql.connector
from dotenv import load_dotenv 
import os

load_dotenv()

DB_Password = os.getenv("DB_PASSWORD")
DB_user = os.getenv("DB_USER")

mydb = mysql.connector.connect(
    host="localhost",
    user=DB_user,
    password=DB_Password,
    PORT=3306
)

mycursor = mydb.cursor()

mycursor.excecute("CREATE DATABASE YT_DB")