import streamlit as st
from DB import connection_to_db
from function import clean
from werkzeug.security import check_password_hash


def login():
    st.header("Login")
    username=st.text_input("username")
    password=st.text_input("password",type="password")

    if st.button("Login"):
        conn=connection_to_db()
        cursor=conn.cursor()
        cursor.execute("select password from users where username=%s",(username,))

        user=cursor.fetchone()
        conn.close()
        if user:
            stored_hash = str(user[0])
            if check_password_hash(stored_hash, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid password")
        else:
            st.error("Invalid Username or Password")
