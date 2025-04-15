import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def Apple_content():
    st.title('📈 Котировки акций Apple (AAPL)')
    st.write('Этот раздел посвящен отображению котировок акций компании Apple с помощью библиотеки yfinance.')

    @st.cache_data
    def load_df_yf(ticker, start, end):
        return yf.download(ticker, start=start, end=end)

    start_date = st.sidebar.date_input('Дата начала', pd.to_datetime('2023-01-01'))
    end_date = st.sidebar.date_input('Дата конца', pd.to_datetime('today'))

    if start_date >= end_date:
        st.error('Дата начала не может быть позже или равна дате конца. Пожалуйста, выберите правильный период.')
    else:
        ticker = 'AAPL'
        df = load_df_yf(ticker, start_date, end_date)

    if df.empty:
        st.warning('Нет данных за указанный период. Попробуйте изменить даты.')
    else:
        st.subheader('📊 Таблица котировок')
        st.dataframe(df)
        st.subheader("📉 График цены закрытия")
        st.line_chart(df["Close"])