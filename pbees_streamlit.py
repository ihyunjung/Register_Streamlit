import streamlit as st
import snowflake.connector
# from streamlit_modal import Modal


st.markdown("<h1 style='text-align: center;'>송이송이 눈꽃송이</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Snowflake 기능 체험하기</p>", unsafe_allow_html=True)


def insert_row_snowflake(name, phone, email, company):
  with my_cnx.cursor() as my_cur:
    query = "insert into customer (NAME, PHONE, EMAIL, COMPANY) values('{name}', '{phone}', '{email}', '{company}');".format(name = name, phone = phone, email = email, company = company)
    my_cur.execute(query)
    return " "


add_my_name = st.text_input('이름')
add_my_phone = st.text_input('핸드폰 번호 ( - 는 제외해주세요)')
add_my_email = st.text_input('이메일')
add_my_company = st.text_input('소속')


col1, col2, col3, col4, col5 = st.columns(5)
if col3.button('체험해 보세요'):
   if not add_my_name:
    st.error('이름을 입력해주세요')
   elif not add_my_phone:
    st.error('핸드폰번호를 입력해주세요')
   else:
      my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
      back_from_function = insert_row_snowflake(add_my_name, add_my_phone, add_my_email, add_my_company)
      st.text(back_from_function)
      st.snow()
      st.markdown("<h1 style='text-align: center;'>Thank you for Adding!</h1>", unsafe_allow_html=True)


