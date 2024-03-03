import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime 
import numpy as np
import aqi

sns.set_theme(style="white")
st.set_option('deprecation.showPyplotGlobalUse', False)


# Title di web
st.title("Polusi di distrik Beijing")

# Dataset
df_airquality = pd.read_csv("https://raw.githubusercontent.com/FOLZi-4G/Analisis-Data-Dicoding/main/dashboard/main_data.csv")

# Min dan Max data
min_date = df_airquality["date"].min().date()
max_date = df_airquality["date"].max().date()

with st.sidebar:
    # add Text
    st.header("Air Quality")
    # add logo
    st.image("https://st2.depositphotos.com/4520249/7571/v/950/depositphotos_75718829-stock-illustration-blowing-wind-icon.jpg")
    
    # Get start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

