# db_config.py

import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='your_host',
        user='your_user',
        password='your_password',
        database='your_database'
    )
    return connection

