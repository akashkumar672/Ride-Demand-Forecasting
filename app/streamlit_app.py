# # import streamlit as st
# # import requests

# # st.title("Bike Demand Predictor")

# # datetime = st.text_input("Datetime (YYYY-MM-DD HH:MM:SS)")
# # season = st.selectbox("Season", [1,2,3,4])
# # holiday = st.selectbox("Holiday", [0,1])
# # workingday = st.selectbox("Working Day", [0,1])
# # weather = st.selectbox("Weather", [1,2,3,4])
# # temp = st.number_input("Temperature")
# # atemp = st.number_input("Feels Like Temp")
# # humidity = st.slider("Humidity", 0, 100)
# # windspeed = st.number_input("Wind Speed")

# # if st.button("Predict"):
# #     payload = {
# #         "datetime": datetime,
# #         "season": season,
# #         "holiday": holiday,
# #         "workingday": workingday,
# #         "weather": weather,
# #         "temp": temp,
# #         "atemp": atemp,
# #         "humidity": humidity,
# #         "windspeed": windspeed
# #     }

# #     response = requests.post("http://127.0.0.1:8000/predict", json=payload)

# #     if response.status_code == 200:
# #         st.success(f"Prediction: {response.json()['prediction']}")
# #     else:
# #         st.error("API error")

# import streamlit as st
# import pandas as pd
# import requests
# import os
# import seaborn as sns
# import matplotlib.pyplot as plt

# # ---- CONFIG ----
# API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

# st.set_page_config(page_title="Bike Demand Dashboard", layout="wide")

# # ---- LOAD DATA ----
# @st.cache_data
# def load_data():
#     return pd.read_csv(r"C:\Users\ag225\Desktop\project\akash\akash\bike-demand-ml\data\train.csv", parse_dates=["datetime"])

# df = load_data()

# # ---- SIDEBAR ----
# st.sidebar.title("🚲 Bike Demand App")
# page = st.sidebar.radio("Navigate", ["Dashboard", "Prediction"])

# # ---- DASHBOARD ----
# if page == "Dashboard":
#     st.title("📊 Bike Demand Dashboard")

#     # Filters
#     st.sidebar.subheader("Filters")
#     hour_range = st.sidebar.slider("Hour", 0, 23, (0, 23))

#     df['hour'] = df['datetime'].dt.hour
#     filtered_df = df[(df['hour'] >= hour_range[0]) & (df['hour'] <= hour_range[1])]

#     st.subheader("Dataset Preview")
#     st.dataframe(filtered_df.head(50))

#     # ---- Plots ----
#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("Demand by Hour")
#         fig, ax = plt.subplots()
#         sns.lineplot(x="hour", y="count", data=filtered_df, ax=ax)
#         st.pyplot(fig)

#         st.info("Peak demand during commute hours (8 AM & 6 PM)")

#     with col2:
#         st.subheader("Weather Impact")
#         fig2, ax2 = plt.subplots()
#         sns.boxplot(x="weather", y="count", data=filtered_df, ax=ax2)
#         st.pyplot(fig2)

#         st.info("Better weather → higher demand")

# # ---- PREDICTION ----
# else:
#     st.title("🔮 Predict Bike Demand")

#     with st.form("prediction_form"):
#         datetime = st.text_input("Datetime (YYYY-MM-DD HH:MM:SS)")

#         col1, col2 = st.columns(2)

#         with col1:
#             season = st.selectbox("Season", [1, 2, 3, 4])
#             holiday = st.selectbox("Holiday", [0, 1])
#             workingday = st.selectbox("Working Day", [0, 1])
#             weather = st.selectbox("Weather", [1, 2, 3, 4])
#             temp = st.slider("Temperature", 0.0, 50.0, 20.0)

#         with col2:
#             atemp = st.slider("Feels Like Temp", 0.0, 50.0, 20.0)
#             humidity = st.slider("Humidity", 0, 100, 50)
#             windspeed = st.slider("Wind Speed", 0.0, 50.0, 10.0)
#             casual = st.number_input("Casual Users", 0, 500, 10)
#             registered = st.number_input("Registered Users", 0, 1000, 50)

#         submit = st.form_submit_button("Predict")

#     if submit:
#         payload = {
#             "datetime": datetime,
#             "season": season,
#             "holiday": holiday,
#             "workingday": workingday,
#             "weather": weather,
#             "temp": temp,
#             "atemp": atemp,
#             "humidity": humidity,
#             "windspeed": windspeed,
#             "casual": casual,
#             "registered": registered
#         }

#         try:
#             with st.spinner("Calling API..."):
#                 res = requests.post(API_URL, json=payload, timeout=5)

#             if res.status_code == 200:
#                 prediction = res.json()["prediction"]
#                 st.success(f"🚲 Predicted Count: {prediction}")
#             else:
#                 st.error(f"API Error: {res.text}")

#         except requests.exceptions.RequestException:
#             st.error("❌ Unable to connect to API. Check deployment URL.")

import streamlit as st
import pandas as pd
import requests
import os
import seaborn as sns
import matplotlib.pyplot as plt

# ---- CONFIG ----
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")
st.set_page_config(page_title="Bike Demand Dashboard", layout="wide")

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\ag225\Desktop\project\akash\akash\bike-demand-ml\data\train.csv", parse_dates=["datetime"])

df = load_data()

# ---- FEATURE ENGINEERING ----
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month

# ---- SIDEBAR ----
st.sidebar.title("🚲 Bike Demand App")
page = st.sidebar.radio("Navigate", ["Dashboard", "Prediction"])

# ===============================
# 📊 DASHBOARD
# ===============================
if page == "Dashboard":
    st.title("📊 Bike Demand Analytics Dashboard")

    # ---- FILTERS ----
    st.sidebar.subheader("🔍 Advanced Filters")

    date_range = st.sidebar.date_input(
        "Date Range",
        [df['datetime'].min(), df['datetime'].max()]
    )

    hour_range = st.sidebar.slider("Hour", 0, 23, (0, 23))
    season_filter = st.sidebar.multiselect("Season", [1, 2, 3, 4], default=[1,2,3,4])
    weather_filter = st.sidebar.multiselect("Weather", [1, 2, 3, 4], default=[1,2,3,4])
    workingday_filter = st.sidebar.multiselect("Working Day", [0, 1], default=[0,1])

    # ---- APPLY FILTERS ----
    filtered_df = df[
        (df['datetime'].dt.date >= date_range[0]) &
        (df['datetime'].dt.date <= date_range[1]) &
        (df['hour'] >= hour_range[0]) &
        (df['hour'] <= hour_range[1]) &
        (df['season'].isin(season_filter)) &
        (df['weather'].isin(weather_filter)) &
        (df['workingday'].isin(workingday_filter))
    ]

    # ---- KPIs ----
    st.subheader("📌 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Demand", int(filtered_df["count"].sum()))
    col2.metric("Avg Demand", round(filtered_df["count"].mean(), 2))
    col3.metric("Max Demand", int(filtered_df["count"].max()))
    col4.metric("Min Demand", int(filtered_df["count"].min()))

    st.divider()

    # ---- DATA PREVIEW ----
    with st.expander("📂 Dataset Preview"):
        st.dataframe(filtered_df.head(100))

    # ---- VISUALIZATIONS ----
    st.subheader("📈 Insights & Trends")

    col1, col2 = st.columns(2)

    # Hourly Trend
    with col1:
        fig, ax = plt.subplots()
        sns.lineplot(x="hour", y="count", data=filtered_df, ax=ax)
        ax.set_title("Demand by Hour")
        st.pyplot(fig)
        st.info("🚀 Peak demand during commute hours (8 AM & 6 PM)")

    # Daily Trend
    with col2:
        fig2, ax2 = plt.subplots()
        sns.lineplot(x="day", y="count", data=filtered_df, ax=ax2)
        ax2.set_title("Demand by Day")
        st.pyplot(fig2)
        st.info("📅 Shows daily fluctuations")

    # Weather & Season
    col3, col4 = st.columns(2)

    with col3:
        fig3, ax3 = plt.subplots()
        sns.boxplot(x="weather", y="count", data=filtered_df, ax=ax3)
        ax3.set_title("Weather Impact")
        st.pyplot(fig3)
        st.info("🌤 Better weather → higher demand")

    with col4:
        fig4, ax4 = plt.subplots()
        sns.barplot(x="season", y="count", data=filtered_df, ax=ax4)
        ax4.set_title("Season vs Demand")
        st.pyplot(fig4)
        st.info("🍃 Seasonal variation in demand")

    # ---- CORRELATION ----
    st.subheader("🔥 Feature Correlation")

    fig5, ax5 = plt.subplots(figsize=(8,5))
    sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax5)
    st.pyplot(fig5)
    st.info("📊 Helps identify important features for ML model")

    # ---- DISTRIBUTION ----
    st.subheader("📊 Demand Distribution")

    fig6, ax6 = plt.subplots()
    sns.histplot(filtered_df["count"], bins=30, kde=True, ax=ax6)
    st.pyplot(fig6)
    st.info("📈 Distribution of demand values")

# ===============================
# 🔮 PREDICTION
# ===============================
else:
    st.title("🔮 Predict Bike Demand")

    with st.form("prediction_form"):
        datetime = st.text_input("Datetime (YYYY-MM-DD HH:MM:SS)")

        col1, col2 = st.columns(2)

        with col1:
            season = st.selectbox("Season", [1, 2, 3, 4])
            holiday = st.selectbox("Holiday", [0, 1])
            workingday = st.selectbox("Working Day", [0, 1])
            weather = st.selectbox("Weather", [1, 2, 3, 4])
            temp = st.slider("Temperature", 0.0, 50.0, 20.0)

        with col2:
            atemp = st.slider("Feels Like Temp", 0.0, 50.0, 20.0)
            humidity = st.slider("Humidity", 0, 100, 50)
            windspeed = st.slider("Wind Speed", 0.0, 50.0, 10.0)
            casual = st.number_input("Casual Users", 0, 500, 10)
            registered = st.number_input("Registered Users", 0, 1000, 50)

        submit = st.form_submit_button("Predict")

    if submit:
        payload = {
            "datetime": datetime,
            "season": season,
            "holiday": holiday,
            "workingday": workingday,
            "weather": weather,
            "temp": temp,
            "atemp": atemp,
            "humidity": humidity,
            "windspeed": windspeed,
            "casual": casual,
            "registered": registered
        }

        try:
            with st.spinner("Calling API..."):
                res = requests.post(API_URL, json=payload, timeout=5)

            if res.status_code == 200:
                prediction = res.json()["prediction"]
                st.success(f"🚲 Predicted Count: {prediction}")
            else:
                st.error(f"API Error: {res.text}")

        except requests.exceptions.RequestException:
            st.error("❌ Unable to connect to API. Check backend server.")