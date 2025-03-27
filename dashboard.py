import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda 🚴‍♂️")

# Statistik Deskriptif
st.subheader("📊 Statistik Data Harian")
st.write(df_day.describe())

# Visualisasi: Penyewaan Sepeda Berdasarkan Musim
st.subheader("🚲 Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x="season", y="cnt", data=df_day, ax=ax)
st.pyplot(fig)

# Visualisasi: Penyewaan Sepeda Berdasarkan Jam
st.subheader("🕒 Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots()
sns.boxplot(x="hr", y="cnt", data=df_hour, ax=ax)
st.pyplot(fig)

# Tambahkan widget interaktif (opsional)
if st.checkbox("Tampilkan 5 Data Teratas"):
    st.write(df_day.head())

