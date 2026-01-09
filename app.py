import streamlit as st
from login import login
from signup import signup
from DB import connection_to_db
import pandas as pd
from function import fetch_all_products,get_total_products,get_total_categories

conn = connection_to_db() 
cursor = conn.cursor()

st.set_page_config(page_title="Product Management System",layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

st.title("Product Management System")

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        login()

    with tab2:
        signup()

else:
    st.sidebar.success(f"Welcome {st.session_state.username}")



    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()
        

   
   
    st.subheader("Basic Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Products", get_total_products())

    with col2:
        st.metric("Total Categories", get_total_categories())

    st.success("Summary data reflects the latest records.")
    




    # st.info("You can now manage products.")

    selected_task= st.selectbox("Choose a Task",["Add a New Product","Edit Product Information","View Product Information","Delete a Product"])





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    if selected_task=="Add a New Product":
        st.header("Add a Product")
        p_name = st.text_input("Product Name")
        p_quantity = st.number_input("Quantity", min_value=0)
        p_price = st.number_input("Price", min_value=0.0)
        p_category = st.text_input("Category")

        if st.button("Add Product"):
            cursor.execute(
            "INSERT INTO products (p_name, p_quantity, p_price, p_category) VALUES (%s, %s, %s, %s)",
            (p_name, p_quantity, p_price, p_category)
        )
            conn.commit()
            st.success(f"Product '{p_name}' added successfully ")



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if selected_task == "Edit Product Information":
        st.subheader("Edit Product Information")
        products = fetch_all_products()

        if products:
            product_dict = {name: pid for pid, name in products}
            selected_name = st.selectbox("Select Product to Edit", list(product_dict.keys()))
            selected_id = product_dict[selected_name]

            new_quantity = st.number_input("Enter New Quantity", min_value=0)
            new_category = st.text_input("Enter New Category")

            if st.button("Update Product", key="edit_btn"):
                cursor.execute(
                "UPDATE products SET p_quantity=%s, p_category=%s WHERE p_id=%s",
                (new_quantity, new_category, selected_id)
            )
                conn.commit()
                st.success(f"Product '{selected_name}' updated successfully ✅")
        else:
            st.warning("No products available to edit.")

    
        


# ---------------------------------------------------------------------------------------------------------------------------------------------------
    if selected_task== "View Product Information":
        st.subheader("View Product Information")
        search_name = st.text_input("Enter Product Name")
        if st.button("Search"):
            cursor.execute(
            "SELECT p_name, p_quantity, p_price, p_category FROM products WHERE p_name=%s",
            (search_name,)
        )
            product = cursor.fetchall()
            if product:
            # Convert to DataFrame for table view
                df = pd.DataFrame(product, columns=["Name", "Quantity", "Price", "Category"])
                st.table(df)
            else:
                st.warning("No product found with that name.")






# -----------------------------------------------------------------------------------------------------------------------------
    elif selected_task== "Delete a Product":
        st.subheader("Delete Product")

        products = fetch_all_products() 
        if products:
            product_dict = {name: pid for pid, name in products}
            selected_name = st.selectbox("Select Product to Delete", list(product_dict.keys()))
            selected_id = product_dict[selected_name]


            if st.button("Delete Product", key="delete_btn"):
                cursor.execute(
                "DELETE FROM products WHERE p_id=%s",
                (selected_id,)
            )
                conn.commit()

                if cursor.rowcount > 0:
                    st.success(f"Product '{selected_name}' deleted successfully")
                else:
                    st.warning("Product could not be deleted")
        else:
            st.warning("No products available to delete.")

        


