# 🏥 Patient Insurance Prediction API

A lightweight **machine-learning inference API** built with **FastAPI** around a pre-trained **Random Forest** insurance prediction model.

The API accepts patient and lifestyle information, runs inference using the pre-built model, and returns the predicted insurance premium category along with confidence and class probabilities.

> **Note:** This project is intended as an ML/API demonstration and should not be used for real-world insurance or medical decisions.

---

## ✨ Features

* 🤖 Pre-trained Random Forest prediction model
* ⚡ Fast inference API using FastAPI
* 🧩 Pydantic-based request validation
* 📊 Prediction confidence and class probabilities
* ❤️ Health-check endpoint with model status
* 📦 Serialized model loading using Pickle
* 🔌 Simple REST API interface

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Pandas**
* **Scikit-learn**
* **Uvicorn**
* **Random Forest**

---

## 🏗️ System Design

```text
                 ┌──────────────────┐
                 │      Client      │
                 │ Web / Postman /  │
                 │      cURL        │
                 └────────┬─────────┘
                          │
                          │ POST /predict
                          ▼
                 ┌──────────────────┐
                 │     FastAPI      │
                 │    REST API      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Pydantic Schema  │
                 │ Input Validation  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Prediction Layer │
                 │   Pandas + ML    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Random Forest   │
                 │ Pre-trained Model│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Prediction +     │
                 │ Confidence +     │
                 │ Class Probabilities│
                 └──────────────────┘
```

---

## 📁 Project Structure

```text
patient-Insurance-prediction-api/
│
├── app.py
│
├── config/
│   └── ...
│
├── models/
│   ├── model.pkl
│   └── predict.py
│
├── schemas/
│   └── pydantic_model.py
│
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sick0M0de/patient-Insurance-prediction-api.git
cd patient-Insurance-prediction-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive documentation:

```text
http://localhost:8000/docs
```

---

## 📡 API Endpoints

### `GET /`

Returns a basic API status message.

### `GET /health`

Returns the API and model status.

Example:

```json
{
  "status": "OK",
  "version": "1.0.0",
  "model_loaded": true
}
```

### `POST /predict`

Predicts the insurance premium category based on the supplied patient information.

#### Input

```json
{
  "bmi": 27.5,
  "age_group": "adult",
  "lifestyle_risk": "low",
  "city_tier": "tier_1",
  "income_lpa": 8.5,
  "occupation": "private_job"
}
```

#### Response

```json
{
  "predicted premium is": {
    "predicted_category": "...",
    "confidence": 0.87,
    "class_probabilities": {
      "...": 0.87,
      "...": 0.13
    }
  }
}
```

The prediction layer uses the loaded model to generate the predicted class, confidence, and probability distribution across available classes.

---

## 🧠 How It Works

```text
Patient Input
     │
     ▼
Input Validation
     │
     ▼
Convert to DataFrame
     │
     ▼
Random Forest Model
     │
     ├── Predicted Category
     ├── Confidence
     └── Class Probabilities
             │
             ▼
          JSON Response
```

The trained model is loaded once when the prediction module is initialized, allowing the API to reuse the model for subsequent requests instead of loading it for every prediction.

---

## 🔮 Future Improvements

* [ ] Dockerize the application
* [ ] Add automated API tests
* [ ] Add model versioning
* [ ] Add structured logging
* [ ] Add authentication
* [ ] Add request/response monitoring
* [ ] Deploy with a production ASGI setup
* [ ] Add CI/CD with GitHub Actions

---

## 👨‍💻 Author

**Ayush** — [@Sick0M0de](https://github.com/Sick0M0de)
