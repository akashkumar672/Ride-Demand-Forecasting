# 🚴 Ride Demand Forecasting Using Machine Learning

## 📌 Project Overview
Ride Demand Forecasting is a Machine Learning project designed to predict bike ride demand based on historical data, weather conditions, seasonal patterns, and time-based features.

The project uses machine learning algorithms to analyze demand patterns and generate predictions to support better fleet management and resource planning.

## 🎯 Project Objectives
- Predict bike ride demand using historical data.
- Analyze the impact of weather and seasonal conditions.
- Identify peak ride-demand hours.
- Compare different Machine Learning algorithms.
- Provide real-time predictions through an API.
- Visualize demand patterns using an interactive dashboard.

## 📊 Dataset Information
- Dataset: Bike Sharing Demand Dataset
- Total Records: 17,379
- Time Period: 2011–2012
- Target Variable: Count

### Features
- Season
- Weather
- Temperature
- Humidity
- Holiday
- Working Day
- Date and Time

## ⚙️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- FastAPI
- Streamlit
- Git & GitHub

## 🔍 Data Preprocessing & Feature Engineering
- Checked missing values and duplicate records.
- Extracted Hour, Day, Month, and Year from datetime.
- Encoded categorical variables.
- Performed exploratory data analysis (EDA).
- Analyzed demand patterns and correlations.

## 🤖 Machine Learning Models
The following regression algorithms were evaluated:

1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regression

**Model Evaluation Metrics:**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Random Forest Regression was selected as the final model based on the reported evaluation results, with an R² score of approximately 0.93.

## 🏗️ Project Structure

```text
bike-demand-ml/
│
├── api/
│   └── app.py
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── preprocess.py
│   └── pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Installation & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/akashkumar672/Ride-Demand-Forecasting.git
```

### 2. Navigate to Project Directory

```bash
cd Ride-Demand-Forecasting
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Environment (Windows)

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run FastAPI Backend

```bash
uvicorn api.app:app --reload
```

### 7. Run Streamlit Dashboard

Open another terminal and execute:

```bash
streamlit run app/streamlit_app.py
```

## 📈 Key Analysis
- Hourly ride demand analysis.
- Seasonal demand patterns.
- Weather impact on ride demand.
- Working day vs holiday demand.
- Actual vs predicted demand comparison.

## 💡 Business Applications
- Fleet optimization.
- Resource allocation.
- Demand-based planning.
- Operational cost reduction.
- Improved customer experience.
## 🚀 FastAPI Swagger UI

The project provides API endpoints for bike demand prediction.

![FastAPI Swagger UI](screenshots/FastAPI%20Swagger%20UI.png)
## 👨‍💻 Author

**Akash Kumar**

B.Tech – Computer Science Engineering

GitHub: https://github.com/akashkumar672

---

⭐ If you find this project useful, consider giving it a star!
