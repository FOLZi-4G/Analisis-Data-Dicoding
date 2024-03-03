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
df_airquality = pd.read_csv("https://raw.githubusercontent.com/FOLZi-4G/Analisis-Data-Dicoding/main/dataset/combined_data/PRSA_Data_combine.csv")

# Nambah Kolom tanggal.
date_columns = ['year', 'month', 'day', 'hour']
df_airquality["date"] = pd.to_datetime(df_airquality[date_columns])
df_airquality.insert(0, 'date', df_airquality.pop('date'))
# Seakrang data tanggal sudah dibuat maka 4 kolom tanggal bisa dihapuskan
df_airquality.drop(date_columns, axis=1, inplace=True)

df_airquality.info()