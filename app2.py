import streamlit as st # pip install pandas
import pandas as pd # pip install streamlit

# Set title header
# st.set_page_config(page_title="Education Dashboard")

st.title("Education Dashboard")

# Load your dataset
data = pd.read_csv('education.csv') 

# data columns = ['Name', 'Category', 'Address', 'Phone Number', 'Website']


# Sidebar for selecting category
category = st.sidebar.selectbox("Select Category", data['Category'].unique())

# Filter data based on selected category
filtered_data = data[data['Category'] == category]

# Search by name
search_name = st.text_input("Search by Name")

# Filter data based on the search_name
if search_name:
    filtered_data = filtered_data[filtered_data['Name'].str.contains(search_name, case=False)]
    

# Display phone number, website and address
if not filtered_data.empty:
    st.write("Matching Records:")
    st.table(filtered_data[['Name', 'Address', 'Phone Number', 'Website']])
else:
    st.write("No matching records found.")


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)