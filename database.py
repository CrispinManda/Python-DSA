import mysql.connector
print("MySQL Connector Imported Successfully!")


# Establish connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4242",
    database="sample_db"
)

# Create cursor
cursor = db.cursor()
print("Database connected successfully!")


