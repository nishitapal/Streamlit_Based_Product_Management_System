import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv() 
def connection_to_db():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("NAME")
    )
