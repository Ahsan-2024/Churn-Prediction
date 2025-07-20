# 🔮 Customer Churn Prediction App

This project predicts whether a customer is likely to **churn** (leave a service) or **stay**, based on their usage and demographic data. It uses machine learning with a web-based interface built using **Streamlit**.

---

## 📌 Overview

**Customer churn** is a critical problem for subscription-based businesses like telecom, banking, SaaS, etc. By predicting churn, companies can take actions to retain customers and reduce revenue loss.

This project includes:
- End-to-end data analysis and model building
- Machine learning with `RandomForestClassifier`
- Web app deployment using `Streamlit`

---

## 📁 Project Structure

churn_project/
│
├── data/
│ └── churn.csv # Dataset file
│
├── model/
│ ├── churn_model.pkl # Trained ML model
│ └── columns.pkl # Feature columns used during training
│
├── churn_notebook.ipynb # Data exploration, model training
├── app.py # Streamlit web application
├── requirements.txt # Python dependencies
└── README.md # Project description


---

## 🧠 Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn (Random Forest Classifier)
- Streamlit (for frontend UI)
- Joblib (for saving model)

---

## 📊 Dataset

Dataset used: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- Features include: `tenure`, `contract type`, `payment method`, `monthly charges`, etc.  
- Target column: `Churn` (Yes/No)

---


