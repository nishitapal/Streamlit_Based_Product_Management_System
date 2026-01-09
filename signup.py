import streamlit as st
from DB import connection_to_db
from function import is_valid_email,clean

def signup():
    st.header("Create Account")
    username=clean(st.text_input("Username").strip())
    email=st.text_input("Email").strip()
    password=clean(st.text_input("Password",type="password").strip())
    confirm_password=clean(st.text_input("confirm_password",type="password").strip())

    if st.button("Signup"):
        if not username or not email or not password:
            st.error("All feilds are required")
            return
        if password!=confirm_password:
            st.error("Passwords do not match")
            return
        if len(password)<6:
            st.error("Password must be at least 6 characters")
            return
        if password.isdigit() or password.isalpha():
            st.error("Password must contain letters and numbers")
            return
        if not is_valid_email(email):
            st.error("Please enter a valid email address")
            return
        try:
            conn=connection_to_db()
            cursor=conn.cursor()

            cursor.execute( "select user_id from users where username=%s",(username,))
            if cursor.fetchone():
                st.error("username already exist")
                conn.close()
                return
            cursor.execute("insert into users (username,email,password) values (%s,%s,%s)",(username,email,password))
            conn.commit()
            st.success("signup successful , Please Login")
            conn.close()
        except Exception as e:
                st.error(str(e))

            






    