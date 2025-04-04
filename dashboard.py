import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Mapping label musim
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df_day['season'] = df_day['season'].map(season_labels)

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda 🚴‍♂️")

# Sidebar untuk filter interaktif
st.sidebar.header("📊 Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim:", df_day['season'].unique(), default=df_day['season'].unique())
date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [df_day['dteday'].min(), df_day['dteday'].max()])

# Filter data
filtered_data = df_day[
    (df_day['season'].isin(selected_season)) &
    (df_day['dteday'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))
]

# Statistik Deskriptif
st.subheader("📜 Statistik Deskriptif Data")
st.write(filtered_data.describe())

# Visualisasi: Tren Penyewaan Sepeda Harian
st.subheader("📈 Tren Penyewaan Sepeda Harian")
fig1, ax1 = plt.subplots()
ax1.plot(filtered_data['dteday'], filtered_data['cnt'], label="Total Rentals", color='blue')
ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Tren Harian Penyewaan Sepeda")
ax1.legend()
st.pyplot(fig1)

# Visualisasi: Rata-rata Penyewaan per Musim (Bar Chart)
st.subheader("🌦️ Rata-rata Penyewaan Sepeda per Musim")
avg_season = filtered_data.groupby("season")["cnt"].mean().sort_values()
fig2, ax2 = plt.subplots()
avg_season.plot(kind="bar", color="skyblue", ax=ax2)
ax2.set_ylabel("Rata-rata Jumlah Penyewaan")
ax2.set_title("Rata-rata Penyewaan Sepeda per Musim")
st.pyplot(fig2)

# Visualisasi: Penyewaan Berdasarkan Hari dalam Minggu
st.subheader("📅 Rata-rata Penyewaan per Hari dalam Minggu")
df_day["weekday"] = df_day['dteday'].dt.day_name()
avg_weekday = df_day.groupby("weekday")["cnt"].mean().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])
fig3, ax3 = plt.subplots()
avg_weekday.plot(kind="bar", color="salmon", ax=ax3)
ax3.set_ylabel("Rata-rata Jumlah Penyewaan")
ax3.set_title("Rata-rata Penyewaan Sepeda per Hari")
st.pyplot(fig3)

# Visualisasi: Penyewaan Sepeda Berdasarkan Jam (Line Chart)
st.subheader("⏰ Pola Penyewaan Sepeda Berdasarkan Jam")
avg_hour = df_hour.groupby("hr")["cnt"].mean()
fig4, ax4 = plt.subplots()
ax4.plot(avg_hour.index, avg_hour.values, color="green")
ax4.set_xlabel("Jam")
ax4.set_ylabel("Rata-rata Penyewaan")
ax4.set_title("Rata-rata Penyewaan Sepeda per Jam")
st.pyplot(fig4)

# Tampilkan Data jika Dicentang
if st.checkbox("Tampilkan Data Tabel"):
    st.write(filtered_data)