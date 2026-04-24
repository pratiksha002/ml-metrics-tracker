# 📊 ML Evaluation & Metrics Tracking System

## 🚀 Overview

This project is a **production-style Machine Learning Evaluation and Tracking System** designed to monitor model performance, store experiment history, and identify the best-performing models over time.

Instead of just training models, this system focuses on **how models behave after training**, which is a critical aspect of real-world ML systems.

---

## 🧠 Key Features

* 📈 **Model Evaluation**

  * Computes MAE, RMSE, and R²
  * Provides realistic performance insights

* 🗂️ **Experiment Tracking**

  * Stores every run with unique ID
  * Tracks parameters, metrics, and timestamps

* 📝 **Logging System**

  * Logs metrics and predictions
  * Maintains historical records

* 🏆 **Best Model Selection**

  * Automatically selects best model based on chosen metric

* 📊 **Interactive Dashboard**

  * Built using Streamlit
  * View all experiments and best model visually

---

## 🏗️ Project Structure

```
ml-metrics-tracker/
│
├── data/
├── models/
├── logs/
│   ├── metrics.csv
│   ├── predictions.csv
│   └── experiments.json
│
├── src/
│   ├── train.py
│   ├── evaluate.py
│   ├── logger.py
│   └── tracker.py
│
├── dashboard/
│   └── app.py
│
├── config/
├── main.py
└── README.md
```

---

## ⚙️ How It Works

```
Train → Predict → Evaluate → Log → Track → Compare → Visualize
```

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Streamlit
* JSON / CSV for storage

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone <your-repo-link>
cd ml-metrics-tracker
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Pipeline

```
python main.py
```

### 4. Run Dashboard

```
streamlit run dashboard/app.py
```

---

## 📊 Example Output

* Metrics stored in `logs/metrics.csv`
* Predictions stored in `logs/predictions.csv`
* Experiments tracked in `logs/experiments.json`

---

## 💡 Why This Project?

In real-world ML systems, **training a model is only a small part**.
Tracking, monitoring, and evaluating models over time is what makes systems reliable.

This project demonstrates:

* MLOps fundamentals
* Experiment tracking
* Model evaluation systems
* Basic system design

---

## 🔮 Future Improvements

* Add multiple model comparison
* Integrate database instead of JSON
* Build API using FastAPI
* Add real-time monitoring system
* Deploy on cloud

---

## 👩‍💻 Author

Built as part of an advanced ML systems learning journey.
