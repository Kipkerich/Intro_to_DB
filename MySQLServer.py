import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="alx_book_store"
)
mycursor = mydb.cursor('CREATE DATABASE IF NOT EXISTS alx_book_store;')
print(f"Database alx_book_store created successfully!")