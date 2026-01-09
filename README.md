# Product Management System

A **Streamlit-based web application** for managing products with **login/signup, CRUD operations, and metrics**.  
This project uses **MySQL** as the database and **hashed passwords** for security.

---

## Features

- **User Authentication:** Signup and login with hashed passwords
- **Add Product:** Add new products with name, quantity, price, and category
- **Edit Product:** Update quantity and category of existing products
- **View Product:** Search and display product information
- **Delete Product:** Remove products from the database
- **Basic Metrics:** Real Time Total products and total categories displayed

---

## Project Structure

product-management-system/
│
├─ app.py # Main Streamlit application
├─ login.py # Login functionality
├─ signup.py # Signup functionality
├─ DB.py # Database connection
├─ function.py # Utility functions (fetch products, metrics, validation)
├─ requirements.txt # Python dependencies
├─ mysql_code.sql # MySQL database and table setup
├─ .env.example # Environment variables example
└─ README.md # Project instructions


## Prerequisites

- Python 3.10+  
- MySQL 8+  
- Streamlit installed (`pip install streamlit`)  

---

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**  --- pip install -r requirements.txt
3. ### Environment Variables Setup

This project uses environment variables to store database credentials.

1. In the project root directory, you will find a file named `.env.example`
2. Rename `.env.example` to `.env`
3. Open the `.env` file and add your MySQL credentials:


4. Fill your MySQL credentials:
   HOST=localhost
   USER=root
   PASSWORD=your_password
   NAME=streamlit_auth_db
5. Create database and tables : mysql -u <username> -p < mysql_code.sql or copy the code of mysql_code.sql to your mysql workbench 
6. Running the App : streamlit run app.py


Usage

1.Login / Sign Up
    Create a new user or login with existing credentials

2.Product Management
    Choose a task from the dropdown: Add, Edit, View, or Delete Product

3.Metrics
     Real Time Total products and total categories shown in the dashboard


Notes

1.Passwords are stored as hashed values for security

2.Metrics update after each operation

3.Ensure MySQL server is running before starting the app

**Note on Metrics:**
- "Total Products" and "Total Categories" metrics update **after performing any CRUD operation**.
- Metrics **do not update on browser refresh**; they refresh only when Streamlit reruns (e.g., after adding, editing, or deleting a product).


