import streamlit as st
import requests

st.title("TimeTrack Analytics")

try:
    response = requests.get("http://127.0.0.1:8000/")
    data = response.json()
    st.write("Ответ от backend:")
    st.write(data)
except Exception as e:
    st.error(f"Не удалось подключиться к backend: {e}")