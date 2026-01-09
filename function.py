import re 
from DB import connection_to_db

def is_valid_email(email):
    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern,email))


def clean(text):
    return re.sub(r'\s+', '', text)


def fetch_all_products():
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT p_id, p_name FROM products")
    products = cursor.fetchall()  # list of tuples [(1, 'Chocolate'), (2, 'Laptop')]
    cursor.close()
    conn.close()
    return products