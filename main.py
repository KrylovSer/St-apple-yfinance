import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

st.title('Добро пожаловать на главную страницу!')
st.write('Это веб-приложение на платформе **Streamlit**, которое позволяет визуализировать данные о котировках акций компании **Apple** с помощью библиотеки **yfinance** и исследование по чаевым на основе набора данных **tips.csv**. Приложение также включает функциональность для загрузки пользовательских CSV файлов и скачивания графиков.')
st.subheader('Для начала работы выберите нужную страницу в боковой панели.')
