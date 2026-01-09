CREATE DATABASE streamlit_auth_db;
USE streamlit_auth_db;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE products(
p_id INT auto_increment PRIMARY KEY,
p_name VARCHAR(100) NOT NULL,
p_quantity INT NOT NULL,
p_price FLOAT,
p_category VARCHAR(100) NOT NULL);