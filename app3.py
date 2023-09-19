import streamlit as st # pip install pandas
import pandas as pd # pip install streamlit
import plotly.express as px # pip install plotly

# Load your dataset
df = pd.read_csv('LGADemography.csv') 

# Fill missing values with the mean of available data
df.fillna(df.mean(), inplace=True)

# Streamlit App
st.title('Rivers State Census Data Analysis')
st.sidebar.title('Select Parameters')

# Sidebar: Select Local Government Area
selected_area = st.sidebar.selectbox('Select Local Government Area:', df['Local Government Area'])

# Sidebar: Select Year
selected_year = st.sidebar.selectbox('Select Year:', ('1991', '2006', '2022'))

# Filter data based on the selected area and year
filtered_data = df[df['Local Government Area'] == selected_area][f'{selected_year} Census'].values[0]

# Display the selected data
st.write(f'Selected Local Government Area: {selected_area}')
st.write(f'Selected Year: {selected_year}')
st.write(f'Census for {selected_year}: {filtered_data:.2f}')


# Plotting the Line Chart
fig = px.scatter(df, x="Local Government Area", y=[f'{selected_year} Census'],
                 title=f'{selected_year} Census by Local Government Area',
                 labels={'Local Government Area': 'Local Government Area', f'{selected_year} Census': 'Census'},
                 height=400)

# Update layout
fig.update_layout(
    xaxis=dict(tickangle=-60),  # Rotate x-axis labels to 60 degrees
    legend=dict(
        traceorder='normal',
        orientation='v',
        x=1.05,
        y=0.5,
        title=dict(text='Year'),
        itemsizing='constant'
    ),
    legend_title_text="Year",
    legend_traceorder='normal',
    legend_orientation='v',
    legend_itemsizing='constant',
    legend_itemclick=False,
    legend_itemdoubleclick=False
)

# Update the legend labels
fig.for_each_trace(lambda trace: trace.update(name=trace.name.replace('Census', '')))

# Show the Plotly chart
st.plotly_chart(fig)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)