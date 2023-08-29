import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center; color: white;'>P.Bees 회원가입</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>정보를 입력해주세요</p>", unsafe_allow_html=True)
Pbees_character = Image.open('Pbees_Character.png')
image(Pbees_character)
