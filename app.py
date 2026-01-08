import streamlit as st
from login import login
from signup import signup

st.set_page_config(page_title="Secure Product Catalog",layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

st.title("Secure Product Catalog System")
if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        login()

    with tab2:
        signup()

else:
    st.sidebar.success(f"Logged in as {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.experimental_rerun()

    st.header("Dashboard")
    st.info("You can now manage products.")

