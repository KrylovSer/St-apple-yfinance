import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


st.sidebar.title("Навигация")
page = st.sidebar.radio("Перейти на страницу", ["Главная", "📈 Котировки акций Apple", "📊 Визуализация распределения чаевых"])

if page == "Главная":
    st.write("Добро пожаловать на главную страницу!")
elif page == "📈 Котировки акций Apple":
    # Импортируем и отображаем первую страницу
    from pages.Apple import Apple_content
    Apple_content()
elif page == "📊 Визуализация распределения чаевых":
    # Импортируем и отображаем вторую страницу
    from pages.tips import tips_content
    tips_content()