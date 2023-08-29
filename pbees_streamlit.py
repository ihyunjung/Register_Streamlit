import streamlit as st
import snowflake.connector

st.markdown("<h1 style='text-align: center; color: black;'>P.Bees 회원가입</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>정보를 입력해주세요</p>", unsafe_allow_html=True)

# my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from customer")
# # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# # st.text("Hello from Snowflake:")
# st.text("Customer list contains:")
# st.text(my_data_row)

def insert_row_snowflake(name, phone, email, company):
  with my_cnx.cursor() as my_cur:
    query = "insert into customer (NAME, PHONE, EMAIL, COMPANY) values('{name}', '{phone}', '{email}', '{company}');".format(name = name, phone = phone, email = email, company = company)
    my_cur.execute(query)
    return "Thanks for adding"


add_my_name = st.text_input('이름')
add_my_phone = st.text_input('핸드폰 번호')
add_my_email = st.text_input('이메일')
add_my_company = st.text_input('소속')

if st.button('회원가입'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_name, add_my_phone, add_my_email, add_my_company)
  st.text(back_from_function)
