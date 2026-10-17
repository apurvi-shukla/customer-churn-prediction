# Customer Churn Prediction Using Machine Learning

##  Project Overview

Customer Churn Prediction is a machine learning project that predicts whether a customer is likely to leave a telecom service provider.

This project uses **Logistic Regression** to classify customers as likely to churn or not churn. A **Streamlit web application** provides a user-friendly interface where users can enter customer details and get predictions.

The project demonstrates the complete workflow of a machine learning application, from data preprocessing and model training to saving trained artifacts and deploying an interactive interface.

##  Project Objectives

- Analyze customer data to understand churn-related patterns.
- Preprocess categorical and numerical features.
- Train a Logistic Regression classification model.
- Predict whether a customer is likely to leave the service.
- Build an interactive web interface using Streamlit.
- Integrate the trained model with the web application.

##  Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **Scikit-learn** — Data preprocessing and machine learning
- **Logistic Regression** — Classification algorithm
- **Joblib** — Saving and loading trained model artifacts
- **Streamlit** — Interactive web application
- **Jupyter Notebook** — Model development and experimentation
- **GitHub** — Version control and project hosting

##  Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── Customer_Churn_Prediction_Model (1).ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── churn_model.pkl
├── preprocessor.pkl
├── README.md
└── .gitignore
```

**Note:** The `.venv` virtual environment folder is kept locally and should not be uploaded to GitHub.

##  Dataset

This project uses the Telco Customer Churn dataset, which contains customer information such as:

- Customer demographics
- Tenure
- Internet and phone services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Churn status

The target column is `Churn`, which indicates whether a customer left the service.

##  Machine Learning Workflow

1. Load the dataset using Pandas.
2. Separate the input features (`X`) and target variable (`y`).
3. Split the data into training and testing sets.
4. Preprocess categorical features using OneHotEncoder and ColumnTransformer.
5. Train a Logistic Regression model.
6. Save the fitted preprocessing object and trained model using Joblib.
7. Load the saved artifacts into the Streamlit application.
8. Collect customer information and generate a churn prediction.

##  Streamlit Web Application

The Streamlit application connects the trained machine learning model to an interactive interface.

Users can enter customer details, submit the information, and view the model's churn prediction.

### Application Features

- Interactive customer input form
- Data preprocessing using the saved preprocessor
- Predictions using the trained Logistic Regression model
- Visual presentation of the prediction result

## To Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/apurvi-shukla/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the required libraries

```bash
pip install pandas scikit-learn streamlit joblib jupyter
```

### 5. Run the Streamlit application

Make sure `app.py`, `churn_model.pkl`, and `preprocessor.pkl` are in the project directory.

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in the terminal, usually `http://localhost:8501`.

##  Model Details

- **Problem Type:** Binary Classification
- **Algorithm:** Logistic Regression
- **Preprocessing:** ColumnTransformer and OneHotEncoder
- **Model Persistence:** Joblib
- **User Interface:** Streamlit

Model performance should be reported using actual evaluation results from the notebook. No accuracy score is claimed here because it has not been verified.

##  Learning Outcomes

Through this project, I practiced:

- Data preparation and feature handling
- Categorical feature encoding
- Training and using a classification model
- Saving and loading machine learning artifacts
- Integrating a trained model with a Streamlit interface
- Organizing a machine learning project for GitHub

##  Future Improvements

- Add model evaluation metrics such as precision, recall, F1-score, and confusion matrix.
- Improve the interface with additional visualizations.
- Add batch predictions for multiple customers.
- Deploy the Streamlit application online.
- Improve prediction quality through further experimentation and validation.

##  Author

**Apurvi Shukla**

GitHub: [apurvi-shukla](https://github.com/apurvi-shukla)

---

*This project was developed for learning and demonstrating a practical machine learning workflow.*


