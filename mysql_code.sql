CREATE DATABASE streamlit_auth_db;
USE streamlit_auth_db;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE products(
p_id int auto_increment primary key,
p_name varchar(100) not null,
p_quantity int  not null,
p_price float,
p_category varchar(100) not null);