
import streamlit as st
import joblib
import pandas as pd

preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("churn_model.pkl")

st.write("Model loaded:", model is not None)
st.write("Preprocessor loaded:", preprocessor is not None)


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    color: #f8fafc;
}

h1 {
    color: #a5b4fc !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #c4b5fd !important;
}

p, label {
    color: #e2e8f0 !important;
}

div.stButton > button {
    background: linear-gradient(90deg, #6366f1, #a855f7);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: bold;
    width: 100%;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border: 1px solid #c4b5fd;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #6366f1;
    border-radius: 10px;
}

div[data-testid="stSelectbox"],
div[data-testid="stNumberInput"] {
    background-color: rgba(255, 255, 255, 0.04);
    border-radius: 10px;
}

hr {
    border-color: #4338ca;
}
</style>
""", unsafe_allow_html=True)


st.title("Customer Churn Prediction")
st.write("Predict whether a customer is likely to leave the company.")


st.header("Customer Details")

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)


gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0,
    step=5.0
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)


payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

senior_citizen = st.selectbox(
    "Is the customer a Senior Citizen?",
    ["Yes", "No"]
)

partner = st.selectbox(
    "Does the customer have a partner?",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Does the customer have dependents?",
    ["Yes", "No"]
)

phone_service = st.selectbox(
    "Does the customer have phone service?",
    ["Yes", "No"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

st.header("Churn Prediction")


if st.button("Predict Churn"):
    customer = pd.DataFrame([{
        "customerID": "NEW_CUSTOMER",
        "gender": gender,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": str(tenure * monthly_charges)
    }])

    st.subheader("Customer Input")
    st.dataframe(customer)

    customer_encoded = preprocessor.transform(customer)
    prediction = model.predict(customer_encoded)

    st.subheader("Prediction Result")

    

    if prediction[0] == 1:
        st.markdown("""
        <div style="background-color:#451a1a; padding:25px;
        border-radius:15px; border:1px solid #ef4444;">
            <h2 style="color:#fca5a5;">⚠️ Churn Risk</h2>
            <p style="color:white; font-size:20px;">
            This customer is likely to leave.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background-color:#052e2b; padding:25px;
        border-radius:15px; border:1px solid #34d399;">
            <h2 style="color:#6ee7b7;">✅ Customer Retained</h2>
            <p style="color:white; font-size:20px;">
            This customer is likely to stay.
            </p>
        </div>
        """, unsafe_allow_html=True)



