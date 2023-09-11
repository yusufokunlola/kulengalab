import streamlit as st # pip install pandas
import pandas as pd # pip install streamlit

# Set title header
st.title("KulengaLab Data Dashboard")

# Sidebar for selecting which app to run
app_selection = st.sidebar.selectbox("Select App", ["Education", "Religion"])

if app_selection == "Education":
    # Load the education dataset
    data = pd.read_csv('education.csv')
    # Rest of the code for the education app

    # Sidebar for selecting category
    category = st.sidebar.selectbox("Select Category", data['Category'].unique())

    # Filter data based on selected category
    filtered_data = data[data['Category'] == category]

    # Search by name
    search_name = st.text_input("Search by Name")

    # Filter data based on the search_name
    if search_name:
        filtered_data = filtered_data[filtered_data['Name'].str.contains(search_name, case=False)]

    # Display phone number, website, and address
    if not filtered_data.empty:
        st.write("Matching Records (Education):")
        st.table(filtered_data[['Name', 'Address', 'Phone Number', 'Website']])
    else:
        st.write("No matching records found (Education)")

elif app_selection == "Religion":
    # Load the religion dataset
    data = pd.read_csv('religion.csv')
    # Rest of the code for the religion app

    # Sidebar for selecting category
    category = st.sidebar.selectbox("Select Category (Religion)", data['Category'].unique())

    # Filter data based on selected category
    filtered_data = data[data['Category'] == category]

    # Search by name
    search_name = st.text_input("Search by Name (Religion)")

    # Filter data based on the search_name
    if search_name:
        filtered_data = filtered_data[filtered_data['Name'].str.contains(search_name, case=False)]

    # Display phone number, website, and address
    if not filtered_data.empty:
        st.write("Matching Records (Religion):")
        st.table(filtered_data[['Name', 'Address', 'Phone Number', 'Website']])
    else:
        st.write("No matching records found (Religion)")
        

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)