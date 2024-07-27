#!/usr/bin/python3
# db_config.py

import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='your_host',
        user='root',
        password='',
        database='restaurant'
    )
    return connection
