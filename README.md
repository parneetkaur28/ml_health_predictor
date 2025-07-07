# 🧠 ML Health Predictor

This is a Machine Learning-powered web application for predicting **Liver Cirrhosis** and **Chronic Kidney Disease (CKD)** based on user-input clinical parameters. 
Built with **Streamlit**, the app uses trained classification models to help with early risk detection

---

## 🛠 Features

- 🏥 Predicts Liver Cirrhosis and Chronic Kidney Disease
- 📊 Interactive UI with real-time prediction
- ⚙️ Pre-trained models loaded with `joblib`
- 📈 Uses **scikit-learn**, **pandas**, **matplotlib**, and more
- ✅ Easy to deploy with Streamlit Cloud, Render, or locally

---

## 🧪 Models Used

- Logistic Regression
- Decision Trees
- Random Forest
- SVM
- Gradient Boosting
- Stacking Ensemble

Models and scalers are stored in the `/models/` directory and loaded using `joblib`.

---

## 📁 Project Structure
ml_health_predictor/

├── Home.py # Main app landing page

├── pages/

│ ├── Liver Cirrhosis.py # Liver Cirrhosis prediction page

│ └── Chronic Kidney disease.py # CKD prediction page

├── models/

│ ├── cirrhosis_model.pkl

│ ├── ckd_model.pkl

│ ├── scaler.pkl

│ └── poly.pkl

├── requirements.txt

└── README.md



---

## ⚙️ Installation

### 🧑‍💻 Local Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/ml_health_predictor.git
cd ml_health_predictor

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Home.py


