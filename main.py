import helper
import streamlit as st
import helper
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv('C:\\Users\\hajosh\\Documents\\ds_projects\\hotel_bookings_cleaned1.csv')
df = pd.read_csv('.\hotel_bookings_cleaned1.csv')

st.set_page_config("Hotel Demand Analysis",layout='wide',)
st.sidebar.title("Hotel Demand Analysis")
user_options = st.sidebar.radio(
    "Select One",
    ("Overall", "2015", "2016", "2017")
)


if st.sidebar.button("Analyze It"):
    bookings,hotel_type_city,hotel_type_resort,max_booked= helper.overall_stats(user_options,df)
    col1, col2, col3, col4= st.columns(4)

    with col1:
        st.write("Booking %")
        st.title(bookings)

    with col2:
        st.write("City hotel %")
        st.title(hotel_type_city)

    with col3:
        st.write("Resort hotel %")
        st.title(hotel_type_resort)
    with col4:
        st.write("Highly booked country")
        st.title(max_booked)


df = helper.custom_df(user_options,df=df)
fig, ax = plt.subplots(2,2,figsize=(12,9))
st.header("Distribution for " +user_options )
sns.countplot(x=df['hotel'], hue=df['is_canceled'],data=df,ax=ax[0,0]).set(ylabel="Number of bookings",title="Distribution of hotel types")
sns.countplot(x=df['meal'],data=df,ax=ax[0,1]).set(ylabel="Number of meals",title="Distribution of meal for")
sns.countplot(x=df['distribution_channel'],data=df,ax=ax[1,0],hue=df['is_canceled']).set(ylabel="Number of bookings",title="Distribution of channel")
sns.countplot(x=df["deposit_type"], palette="flare", ax=ax[1,1], hue=df["is_canceled"]).set(title="Deposite type", ylabel="Number of bookings")
st.pyplot(fig)

st.header("Avarage weely night stay Vs weekend night stays " +user_options )
fig, ax = plt.subplots()
sns.lineplot(data=df, x='arrival_date_month',y='stays_in_week_nights')
sns.lineplot(data=df, x='arrival_date_month',y='stays_in_weekend_nights')
plt.xticks(rotation=90)
plt.show()
st.pyplot(fig)

st.header("month-wise booking for "+user_options)
fig, ax = plt.subplots()
df.groupby(['arrival_date_month']).sum()['booked'].plot(kind='bar')
plt.show()
st.pyplot(fig)

st.header("customer-wise distribution for "+user_options)
col1, col2 = st.columns(2)
with col1:
    st.header("Pie chart")
    pie_data=(df['customer_type'].value_counts(normalize=True) * 100).reset_index().rename(columns = {'index':'customer_type', 'customer_type':'pecentage'})
    fig, ax = plt.subplots()
    plt.pie(x=pie_data['pecentage'],labels=pie_data['customer_type'],autopct="%.2f")
    plt.show()
    st.pyplot(fig)
with col2:
    st.header("DataFrame")
    st.dataframe(pie_data)

st.header("no.of adults per booking for year "+user_options)
fig, ax = plt.subplots()
df['adults'].value_counts().plot(kind='bar')
plt.show()
st.pyplot(fig)

