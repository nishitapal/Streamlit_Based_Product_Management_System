import streamlit as st
from DB import connection_to_db

def login():
    st.header("Login")
    username=st.text_input("username")
    password=st.text_input("password",type="password")

    if st.button("Login"):
        conn=connection_to_db()
        cursor=conn.cursor()
        cursor.execute("select * from users where username=%s and password=%s",(username,password))
        user=cursor.fetchone()
        conn.close()

        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
        else:
            st.error("Invalid Username or Password")
