#가져오기
import streamlit as st
#사이드 바와 선택 박스
# page = st.sidebar.selectbox(‘Choose your page’, [‘INPUT FORM’, ‘RESULT’])
#정보 입력 후 함수
def update_page():
  st.balloons()
  st.markdown('# Thank you for information')
  st.json(customer_information)
#혹시 선택 박스에서선택한 페이지가INPUT FORM이라면
# if page == ‘INPUT FORM’:
  st.title('INPUT FORMATION')
#각종 입력 폼
with st.form(key='customer'):
  customer_name: str = st.text_input('NAME', max_chars=15)
  customer_mobile: str = st.text_input('MOBILE', max_chars=13)
  # customer_gender = st.radio(“GENDER”,(‘MEN’, ‘Women’))
  # customer_address = st.selectbox(‘COUNTRY’,
  # (‘Hokkaido’, ‘Tohoku’, ‘Kanto’, ‘Chubu’, ‘Kinki’, ‘Kansai’, ‘Chugoku’, ‘Shikoku’, ‘Kyusyu’, ‘Okinawa’))
  customer_company: str = st.text_input('Company', max_chars = 20)
  customer_mail: str = st.text_input('Mail Address', max_chars = 30)
  #폼에 입력 결과를 정리
  customer_information = {
  'customer_name': customer_name,
  'customer_mobile' : customer_mobile,
  'customer_company': customer_company,
  'customer_mail': customer_mail
  }
#폼에 입력 결과를 송신
submit_button = st.form_submit_button(label='Send')
#submit_button가 송신 되면 함수를 실행
if submit_button:
  update_page()

# ====================

# import streamlit as st
# import pandas as pd
# import requests
# import snowflake.connector
# from urllib.error import URLError

# st.title('P.Bees')

# st.header('고객용 회원가입')
# st.text('🥣 Omega 3 & Blueberry Oatmeal')
# st.text('🥗 Kale, Spinach & Rocket Smoothie')
# st.text('🐔 Hard-Boiled Free-Range Egg')
# st.text('🥑🍞 Avocado Toast')

# st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# # st.dataframe(my_fruit_list)
# my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# # set_index (0,1,2..가 아니라 Fruit열을 인덱스로 만들어줘)
# my_fruit_list = my_fruit_list.set_index('Fruit') 
# # DataFrame.set_index(keys, drop=True, append=False, inplace=False)
# # drop: 인덱스로 세팅한 열을 DataFrame 내에서 삭제할지 여부 결정(option)
# # append: 기존에 존재하던 인덱스 삭제 여부 결정(option)
# # inplace: 원본 객체 변경 여부 결정(option)


# # Let's put a pick list here so they can pick the fruit they want to include
# fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

# # display the table on the page
# st.dataframe(fruits_to_show)

# # create the repeatable code block (called a function)
# def get_fruityvice_data(this_fruit_choice):
#   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
#   fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#   return fruityvice_normalized

# # New Section to display fruityvice api response
# st.header('Fruityvice Fruit Advice!')
# try:
#   fruit_choice = st.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     st.error("Please select a fruit to get information.")
#   else:
#     back_from_function = get_fruityvice_data(fruit_choice)
#     st.dataframe(back_from_function)
# except URLError as e:
#   st.error()
  

# st.header("View Our Fruit List - Add Your Favorities")
# # Snowflake-related functions
# def get_fruit_load_list():
#   with my_cnx.cursor() as my_cur:
#     my_cur.execute("select * from fruit_load_list")
#     return my_cur.fetchall()

# # #  Add a button to load the fruit
# # if st.button('Get Fruit List'):
# #   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# #   my_data_rows = get_fruit_load_list()
# #   my_cnx.close()
# #   st.dataframe(my_data_rows)
 

# # Allow the end user to add a fruit to the list
# def insert_row_snowflake(new_fruit):
#   with my_cnx.cursor() as my_cur:
#     my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")
#     return "Thanks for adding " + new_fruit

# add_my_fruit = st.text_input('What fruit would you like to add?')
# # if st.button('Add a Fruit to the List'):
# #   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# #   back_from_function = insert_row_snowflake(add_my_fruit)
# #   st.text(back_from_function)

# if st.button('Get Fruit List'):
#   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#   st.write(insert_row_snowflake(add_my_fruit))
#   my_data_rows = get_fruit_load_list()
#   my_cnx.close()
#   st.dataframe(my_data_rows)
