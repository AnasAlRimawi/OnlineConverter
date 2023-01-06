import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title='Online Converter', layout='centered')

st.title("Convert videos to high quality mp4, flv, webm, mkv, m4a, mp3 format.")

url = st.text_input('Enter Valid URL', '')

src = "https://convert2mp3s.com/api/widgetv2?url=" + url

components.iframe(src, width= 700, height=700)