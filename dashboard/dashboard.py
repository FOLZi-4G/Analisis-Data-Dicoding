import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime 
import numpy as np
import aqi

sns.set(style="dark")
st.set_option('deprecation.showPyplotGlobalUse', False)


# Title di web
st.title("Polusi di distrik Beijing")

# Dataset
data = pd.read_excel('dataset/combined_data/PRSA_Data_combine.csv')
return data
