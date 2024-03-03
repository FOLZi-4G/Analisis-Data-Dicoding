import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import aqi

sns.set_theme(style="white")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Dataset
df_airquality = pd.read_csv("https://raw.githubusercontent.com/FOLZi-4G/Analisis-Data-Dicoding/main/dashboard/main_data.csv")

# Min dan Max data
min_date = pd.to_datetime(pd.to_datetime(df_airquality["date"].min()).strftime("%Y-%m-%d"))
max_date = pd.to_datetime(pd.to_datetime(df_airquality["date"].max()).strftime("%Y-%m-%d"))

with st.sidebar:
    # Title di web
    st.title("Analisis AQI Beijing")
    # add Text
    st.header("Dengan Python 🐍")
    # add logo
    st.image("https://raw.githubusercontent.com/FOLZi-4G/Analisis-Data-Dicoding/main/Python_Meter.jpg")

    
    # Get start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Pilih rentang waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


# dataframe ini yang bersifat dinamis antar range data
main_df = df_airquality[(df_airquality["date"] >= str(start_date)) & 
                    (df_airquality["date"] <= str(end_date))]

# Pertanyaan 1 
st.header('Tingkat polusi udara di kota Beijing💨')
st.subheader("Tingkat perubahan rata-rata indeks AQI dari tahun ke tahun.")

# Dengan menggunakan formulai EQI calculations.dari library python-eqi kita dapat menarik rata-rata dari tiap stasiun dari tahun ke tahun
selected_columns = ['PM2.5','PM10']
mean_only = {col: ["mean"] for col in selected_columns}
station_list = main_df["station"].unique()

years = np.arange(main_df["year"].min(), main_df["year"].max()+1)
fig, axs = plt.subplots(len(station_list), 1, figsize=(12, 23), sharex=True)

for i, station in enumerate(station_list):
    ax = axs[i]
    aqi_values = []
    one_station_at_a_time = main_df.query("station == @station")
    for year in years:
        # hanya menggunakan rata-rata dari kadar senyawa yang terekam per tahun.
        year_frame = one_station_at_a_time.query("year == @year").agg(mean_only)
        yearly_aqi = aqi.to_aqi([ 
            (aqi.POLLUTANT_PM25, year_frame["PM2.5"].iloc[0]), #Dirty
            (aqi.POLLUTANT_PM10, year_frame["PM10"].iloc[0])
        ])
        aqi_values.append(yearly_aqi)
    
    # Plot nilai AQI
    sns.lineplot(x=years, y=aqi_values, ax=ax, color='red', marker='o')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Nilai AQI')
    ax.set_title('Perubahan AQI Stasiun {}'.format(station))
    print("Rata-rata untuk stasiun {} adalah {}".format(station, sum(aqi_values)/len(aqi_values)))

# Tampilkan plot
st.pyplot(fig)

# Pertanyaan 2
st.subheader("Perbedaan tingkat kadar polusi di udara saat hujan dengan tidak")

numerical_columns = main_df.select_dtypes(include=['float64', 'int64'])

rainy_days = main_df[main_df['RAIN'] > 0]
non_rainy_days = main_df[main_df['RAIN'] == 0]

rainy_means = rainy_days[numerical_columns.columns].mean()
non_rainy_means = non_rainy_days[numerical_columns.columns].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=rainy_means.index, y=rainy_means.values, color='blue', alpha=0.5, label='Hujan')
sns.barplot(x=non_rainy_means.index, y=non_rainy_means.values, color='red', alpha=0.5, label='Tidak Hujan')
plt.xlabel('Parameter Kualitas Udara')
plt.ylabel('Rata-rata Nilai')
plt.title('Perubahan Kualitas Udara saat Hujan vs Tidak Hujan')
plt.legend()
plt.xticks(rotation=45)
st.pyplot(plt)

# Pertanyaan 3
st.subheader("Korelasi antara tingkat derajat suhu dengan kadar polusi")
selected_columns = ['TEMP', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Hitung korelasi antara suhu udara dan parameter-parameter polusi udara
correlation_matrix = df_airquality[selected_columns].corr()

# Tampilkan matriks korelasi
print("Matrix Korelasi:")
print(correlation_matrix)

# Visualisasi heatmap untuk matriks korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap Korelasi antara Suhu Udara dan Parameter Polusi Udara')
st.pyplot(plt)

st.caption('Copyright © Bryan Yapdhika')