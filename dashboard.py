import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

#Mapping label musim
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df_day['season'] = df_day['season'].map(season_labels)

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda 🚴‍♂️")


# Sidebar untuk filter interaktif
st.sidebar.header("📊 Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim:", df_day['season'].unique(), default=df_day['season'].unique())
date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [df_day['dteday'].min(), df_day['dteday'].max()])

# Filter data berdasarkan input user
filtered_data = df_day[(df_day['season'].isin(selected_season)) & 
                       (df_day['dteday'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))]

# Tampilkan Data
st.subheader("📜 Statistik Deskriptif Data")
st.write(filtered_data.describe())

# Visualisasi: Penyewaan Sepeda Berdasarkan Musim
st.subheader("📅 Pola Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.boxplot(x="season", y="cnt", data=filtered_data, ax=ax, palette="coolwarm")
st.pyplot(fig)

# Visualisasi: Tren Penyewaan Sepeda
st.subheader("📈 Tren Penyewaan Sepeda Harian")
fig, ax = plt.subplots()
ax.plot(filtered_data['dteday'], filtered_data['cnt'], label="Total Rentals", color='blue')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda Harian")
ax.legend()
st.pyplot(fig)

# Visualisasi: Penyewaan Sepeda Berdasarkan Jam
st.subheader("⏰ Jam Penyewaan Sepeda Tertinggi")
fig, ax = plt.subplots()
sns.boxplot(x="hr", y="cnt", data=df_hour, ax=ax, palette="coolwarm")
st.pyplot(fig)

# Tampilkan Data jika Dicentang
if st.checkbox("Tampilkan Data Tabel"):
    st.write(filtered_data)


# # Statistik Deskriptif
# st.subheader("📊 Statistik Data Harian")
# st.write(df_day.describe())

# # Visualisasi: Penyewaan Sepeda Berdasarkan Musim
# st.subheader("🚲 Penyewaan Sepeda Berdasarkan Musim")
# fig, ax = plt.subplots()
# sns.barplot(x="season", y="cnt", data=df_day, ax=ax)
# st.pyplot(fig)

# # Visualisasi: Penyewaan Sepeda Berdasarkan Jam
# st.subheader("🕒 Penyewaan Sepeda Berdasarkan Jam")
# fig, ax = plt.subplots()
# sns.boxplot(x="hr", y="cnt", data=df_hour, ax=ax)
# st.pyplot(fig)

# # Tambahkan widget interaktif (opsional)
# if st.checkbox("Tampilkan 5 Data Teratas"):
#     st.write(df_day.head())
