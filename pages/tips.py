import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import warnings
warnings.filterwarnings('ignore')

def tips_content():
    st.title('📊 Визуализация распределения чаевых')
    st.write('Этот раздел посвящен визуализации файла tips.csv.')

    # Функция для сохранения графика в байтовый поток и возврата данных для скачивания
    def save_plot_to_bytes(fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)  # Возвращаемся в начало потока
        return buf

    @st.cache_data
    def load_df_pd(file):
        return pd.read_csv(file)
    
    st.sidebar.subheader('Загрузите данные о чаевых')
    uploaded_file = st.sidebar.file_uploader('Загрузите ваш CSV файл', type='csv')

    if uploaded_file:
        tips = load_df_pd(uploaded_file)

        st.sidebar.subheader("Отображаемые данные")
        show_1 = st.sidebar.checkbox("DataFrame файла CSV")
        if show_1:
            st.subheader("Данные о чаевых")
            st.dataframe(tips)
        else:
            st.info('Для отображения нужной вам информации выберете необходимые данные в боковой панели.')

        show_2 = st.sidebar.checkbox("Плотность распределения общней суммы счета")
        if show_2:
            st.subheader('Плотность распределения общей суммы счета')
            fig, ax = plt.subplots()
            sns.histplot(tips['total_bill'], bins=20, kde=True)
            ax.set(xlabel='Счет', ylabel='Количество счетов с такой ссумой')
            ax.set_xticks(np.arange(0, 60, 5))
            st.pyplot(fig)

            buf = save_plot_to_bytes(fig)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr1.png', mime="image/png")

        show_3 = st.sidebar.checkbox("Распределение чаевых от суммы заказа")
        if show_3:
            st.subheader("Распределение чаевых от суммы заказа")
            fig, ax = plt.subplots()
            sns.set_theme(style='whitegrid', palette='muted')
            sns.scatterplot(data=tips, x='tip', y='total_bill')
            ax.set(xlabel='Чаевые', ylabel='Чек')
            st.pyplot(fig)

            buf = save_plot_to_bytes(fig)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr2.png', mime="image/png")

        show_4 = st.sidebar.checkbox("Распределение чаевых от суммы заказа по дням недели")
        if show_4:
            st.subheader("Распределение чаевых от суммы заказа по дням недели")
            sns.set_theme(style='whitegrid', palette='muted')
            gr = sns.relplot(kind='scatter', data=tips, x='tip', y='total_bill', row='day', height=4, aspect=2)
            gr.set_axis_labels('Чаевые', 'Сумма счёта')
            st.pyplot(gr.figure)

            buf = save_plot_to_bytes(gr.figure)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr3.png', mime="image/png")
        
        show_5 = st.sidebar.checkbox("Зависимость между суммой счета, чаевыми и размером столика")
        if show_5:
            st.subheader("Зависимость между суммой счета, чаевыми и размером столика")
            sns.set_theme(style='whitegrid', palette='muted')
            gr = sns.relplot(kind='scatter', data=tips, x='tip', y='total_bill', size='size', hue='size')
            gr.set_axis_labels('Чаевые', 'Сумма счёта')
            gr._legend.set_title("Размер столика")
            st.pyplot(gr.figure)

            buf = save_plot_to_bytes(gr.figure)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr4.png', mime="image/png")
        
        show_6 = st.sidebar.checkbox("Зависимость между днем недели и размером сета")
        if show_6:
            st.subheader("Зависимость между днем недели и размером сета")
            fig, ax = plt.subplots()
            sns.set_theme(style='whitegrid', palette='muted')
            sns.boxplot(data=tips, x='day', y='total_bill', palette='muted')
            ax.set_xlabel('День недели')
            ax.set_ylabel('Сумма счёта')
            st.pyplot(fig)

            buf = save_plot_to_bytes(fig)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr5.png', mime="image/png")

        show_7 = st.sidebar.checkbox("Зависимость между днем недели, чаевыми и полом посетителя")
        if show_7:
            st.subheader("Зависимость между днем недели, чаевыми и полом посетителя")
            sns.set_theme(style='whitegrid', palette='muted')
            gr = sns.relplot(kind='scatter', data=tips, x='tip', y='day', hue='sex')
            gr.set_axis_labels('День недели', 'Чаевые')
            gr._legend.set_title("Пол")
            st.pyplot(gr.figure)

            buf = save_plot_to_bytes(gr.figure)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr6.png', mime="image/png")

        show_8 = st.sidebar.checkbox("Распределение чаевых на обед и ланч")
        if show_8:
            st.subheader("Распределение чаевых на обед и ланч")
            sns.set_theme(style='whitegrid', palette='muted')
            gr = sns.displot(data=tips, x='tip', col='time')
            gr.set_axis_labels('Чаевые', 'Общее количество')
            st.pyplot(gr.figure)

            buf = save_plot_to_bytes(gr.figure)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr7.png', mime="image/png")

        show_9 = st.sidebar.checkbox("Зависимость чаевых от пола и курения")
        if show_9:
            st.subheader("Зависимость чаевых от пола и курения")
            sns.set_theme(style='whitegrid', palette='muted')
            gr = sns.relplot(kind='scatter', data=tips, x='tip', y='total_bill', col='sex', hue='smoker')
            gr.set_axis_labels('Чаевые', 'Общее количество')
            st.pyplot(gr.figure)

            buf = save_plot_to_bytes(gr.figure)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr8.png', mime="image/png")

        show_10 = st.sidebar.checkbox("Тепловая карта чаевых, размера столика, суммы счета")
        if show_10:
            st.subheader("Тепловая карта чаевых, размера столика, суммы счета")
            mat_cor = tips[['total_bill', 'tip', 'size']].corr()
            fig, ax = plt.subplots()
            sns.heatmap(data=mat_cor, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar=True)
            st.pyplot(fig)

            buf = save_plot_to_bytes(fig)
            st.download_button(label='📥 Скачать график', data=buf, file_name='gr9.png', mime="image/png")
