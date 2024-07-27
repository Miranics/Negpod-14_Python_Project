#!/usr/bin/python3
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # or the appropriate hostname
        user='root',
        password='miracity',
        database='restaurant'
    )
    return connection

