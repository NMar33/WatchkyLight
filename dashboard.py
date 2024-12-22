import streamlit as st
from pgs.eda_page import render_page as eda_page
from pgs.qoe_page import render_page as qoe_page

# Настройка приложения
st.set_page_config(
    page_title="QoE Analyzer",
    page_icon="📊",
    layout="wide"
)

# Сайдбар для выбора страницы
st.sidebar.title("Навигация")
page = st.sidebar.radio("Выберите страницу", ["Настройка QoE", "EDA"])

# Рендеринг выбранной страницы
if page == "EDA":
    eda_page()
elif page == "Настройка QoE":
    qoe_page()
