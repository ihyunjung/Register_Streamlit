import streamlit as st
import snowflake.connector

st.markdown("<h1 style='text-align: center; color: white;'>P.Bees 회원가입</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>정보를 입력해주세요</p>", unsafe_allow_html=True)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
