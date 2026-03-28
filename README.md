# ⚡ Energy Consumption Prediction System

## 📌 Project Overview

This project predicts electricity consumption based on environmental and historical data such as temperature and humidity.

The goal is to build a real-world end-to-end Machine Learning pipeline including data analysis, model building, API development, and visualization.

---

## 🚀 Features

* Data preprocessing and cleaning using Pandas
* Exploratory Data Analysis (EDA)
* Machine Learning model for prediction
* REST API for real-time predictions
* Dashboard visualization using Power BI

---

## 🏗️ Project Architecture

Data Collection → Data Cleaning → Feature Engineering → Model Training → Model Saving → API → Dashboard

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Backend:** Flask / FastAPI
* **Database:** SQLite
* **Visualization:** Power BI
* **Tools:** Git, VS Code, Jupyter Notebook

---

## 📂 Project Structure

energy-consumption-prediction/
│
├── data/                # Raw and processed datasets
├── notebooks/           # Jupyter notebooks for EDA
├── src/                 # Source code
├── models/              # Trained model files
├── api/                 # API code
├── dashboard/           # Power BI files
├── requirements.txt     # Dependencies
└── README.md

---

## ⚙️ Installation & Setup

### Step 1: Clone the repository

git clone https://github.com/your-username/energy-consumption-prediction.git

### Step 2: Navigate to project folder

cd energy-consumption-prediction

### Step 3: Install dependencies

pip install -r requirements.txt

---

## ▶️ How to Run the Project

### Run Jupyter Notebook (EDA & Model Training)

jupyter notebook

### Run API

cd api
python app.py

---

## 🔌 API Usage

### Endpoint:

/predict

### Method:

POST

### Sample Input:

{
"temperature": 30,
"humidity": 60
}

### Sample Output:

{
"consumption": 245.67
}

---

## 📊 Model Performance

* Mean Absolute Error (MAE): XX
* Root Mean Square Error (RMSE): XX
* R² Score: XX

---

## 📸 Screenshots

(Add screenshots here: graphs, dashboard, API output)

---

## 📈 Future Improvements

* Add real-time data using APIs
* Deploy using cloud (AWS / Render)
* Improve model accuracy with advanced algorithms

---

## 👩‍💻 Author

Sugandha Parimala Ponnala
📧 [sugandhaps3@gmail.com](mailto:sugandhaps3@gmail.com)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
