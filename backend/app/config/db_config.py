import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="3306",
        password="",
        database="bdjosemaria"
    )