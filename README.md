# 🩺 Diabetes Prediction Project

## 📌 Project Overview
This project aims to predict diabetes outcomes using machine learning models. The dataset includes clinical and demographic features such as Age, BMI, Glucose levels, Insulin, Pregnancies, and Diabetes Pedigree Function.  

Before training, the data was carefully handled for **missing values** and **outliers** to ensure high-quality input for the models.

---

## 🗂️ Dataset
- **Source:** Local dataset (e.g., Pima Indians Diabetes Dataset)  
- **Number of features:** 8 original features + engineered features  
- **Number of samples:** Variable (training/testing)  
- **Feature Handling:**  
  - ❌ Missing values were imputed  
  - ⚠️ Outliers were detected and treated  
  - 📏 Feature scaling (StandardScaler) and log transformation applied to skewed features  
  - 🛠️ Additional engineered features created:  
    - `Glucose_BMI = Glucose × BMI`  
    - `Pregnancy_per_Age = Pregnancies ÷ Age`  
    - `Glucose_Insulin_ratio = Glucose ÷ Insulin`  
  - 👶 Dummy encoding for age groups (Young, Middle, Old) and BMI groups (Underweight, Normal, Overweight, Obese)  

---

## 🚀 Project Steps

### 1️⃣ Data Preprocessing
- Imputed missing values  
- Detected and handled outliers  
- Applied **log transformation** to skewed features (`Pregnancies`, `Age`, `Insulin`, `DiabetesPedigreeFunction`)  
- Scaled all features using **StandardScaler**  
- Created engineered features and dummy variables as described above  

### 2️⃣ Train-Test Split
- Split dataset into training (80%) and testing (20%) sets  
- Stratified splitting to maintain class distribution  

### 3️⃣ Model Training
- **Models trained:**  
  - Logistic Regression  
  - SVM (RBF)  
  - Random Forest  
  - XGBoost  
- Hyperparameter tuning using `RandomizedSearchCV` or `GridSearchCV`  
- **SMOTE** used in pipelines to handle class imbalance  
- Pipelines include preprocessing steps to ensure transformations are applied consistently  

### 4️⃣ Model Evaluation
**Metrics computed:**  
- Accuracy  
- ROC-AUC  
- Precision, Recall, F1-score for each class  
- Train accuracy also checked to monitor overfitting  

| Model               | Train Accuracy | Test Accuracy | ROC-AUC |
|--------------------|----------------|----------------|---------|
| Logistic Regression | 0.839          | 0.779          | 0.869   |
| SVM (RBF)           | 0.896          | 0.864          | 0.912   |
| Random Forest       | 0.985          | 0.870          | 0.944   |
| XGBoost             | 0.928          | 0.883          | 0.955   |

---

### 5️⃣ Threshold Optimization (for XGBoost)
- Best **F1-score threshold** found: 0.64  
- Adjusted predictions improve balance between **Precision** and **Recall**  

| Class | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| 0     | 0.91      | 0.93   | 0.92     |
| 1     | 0.87      | 0.83   | 0.85     |

- Overall Accuracy: 0.90 ✅  

---

### 6️⃣ Model Deployment
- XGBoost model wrapped in a **custom class** to include threshold for predictions  
- Model saved with **pickle** for deployment in **Streamlit** or other applications  
- Streamlit app can take new patient data as input and output **predicted diabetes outcome** and **probability**


This project demonstrates the **end-to-end machine learning workflow** for healthcare predictions, including preprocessing, feature engineering, model training, evaluation, threshold optimization, and deployment.
