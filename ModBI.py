
import streamlit as st
import pandas as pd
import plotly.express as px


def sales():
    def get_df_from_excel():
        return pd.read_csv("data/supermarket_sales.csv")

    # --- Begin Data Frame Munging ---##
    df = get_df_from_excel()
    df = df.rename({'Invoice ID': 'InvoiceID', 'Customer type': 'Customertype', 'Product line': 'Productline',
                   'gross margin percentage': 'GMP', 'gross income': 'Grossincome', 'Tax 5%': 'Tax5P', 'Unit price': 'Unitprice'}, axis=1)

    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
    # --- End Data Frame Munging ---##

    # -- Begin Header Divs #
    city = st.sidebar.multiselect("Select Cities: ", options=[city for city in df['City'].unique(
    )], default=[city for city in df['City'].unique()])

    customertype = st.sidebar.multiselect("Select Customer Types: ", options=[one for one in df['Customertype'].unique(
    )], default=[one for one in df['Customertype'].unique()])

    productline = st.sidebar.multiselect("Select Product Line: ", options=[one for one in df['Productline'].unique(
    )], default=[one for one in df['Productline'].unique()])

    payment = st.sidebar.multiselect("Select Payment Type: ", options=[one for one in df['Payment'].unique(
    )], default=[one for one in df['Payment'].unique()])
    df_some = df.query(
        'City==@city and Customertype==@customertype and Productline==@productline and Payment==@payment'
    )
    st.markdown("---")

    # -- End Header Divs #

    lft, cen, rit = st.columns(3)

    total_sales = int(df_some["Total"].sum())
    avg_sales = round(df_some["Total"].mean(), 2)
    avg_rating = round(df_some["Rating"].mean(), 0)

    lft.write(f"<div class='bi-card'><span class='bi-hdr'>Total Sales</span><span class='bi-info'>US $ {total_sales:,}</span></div>",
              unsafe_allow_html=True)

    cen.write(f"<div class='bi-card'><span class='bi-hdr'>Average Rating</span><span class='bi-info'>{avg_rating} Stars</span></div>",
              unsafe_allow_html=True)

    rit.write(f"<div class='bi-card'><span class='bi-hdr'>Sales/Transaction</span><span class='bi-info'> US $ {avg_sales:,}</span></div>",
              unsafe_allow_html=True)
    st.markdown("---")
    df_groudp_PL_sales = df_some.groupby(by=['Productline']).sum(
        [['Total']]).sort_values(by=['Total'])

    # ---Begin Charts ---#
    df_groudp_PL_sales_chart = px.bar(
        df_groudp_PL_sales,
        x='Total',
        y=df_groudp_PL_sales.index,
        orientation='h',
        title='<b>Sales by Product Line</b>',
        template='plotly_white',
        color_discrete_sequence=[
            '#0083B8'] * len(df_groudp_PL_sales)
    )
    df_groudp_PL_hours = df_some.groupby(
        by=['Hour']).sum().sort_values(by='Total')

    df_groudp_PL_hours_chart = px.bar(
        df_groudp_PL_hours,
        title='<b>Total Sales By Hour</b>',
        y='Total',
        x=df_groudp_PL_hours.index,
        template='plotly_white',
        color_discrete_sequence=['#0083B8']*len(df_groudp_PL_hours)
    )
    ch1, ch2 = st.columns(2)
    ch1.plotly_chart(df_groudp_PL_sales_chart, use_container_width=True)
    ch2.plotly_chart(df_groudp_PL_hours_chart, use_container_width=True)

    # --- End Charts ---#
    # --- Begin Viewing Grid Data ---#

    if st.checkbox("All Data"):
        st.dataframe(df_some)

    if st.checkbox("View Product Grouping"):
        st.dataframe(df_groudp_PL_sales)

    if st.checkbox("View Hours Grouping"):
        st.dataframe(df_groudp_PL_hours)
    # --- End Viewing Grid Data ---#
