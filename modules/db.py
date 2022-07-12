from os import error
import sqlite3
try:
    connection = sqlite3.connect('SikiZa.db')
    cursor = connection.cursor()
    
    query = """ CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL                       
    )"""
   
    
    cursor.execute(query)
    
except connection.Error as error:
    print("Error creating Table" , error)
finally:
    if connection:
        connection.close()