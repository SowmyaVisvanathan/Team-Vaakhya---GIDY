import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Loan Assistant", layout="wide")

API_BASE_URL = "http://127.0.0.1:5000"

def predict_loan(user_data):
    response = requests.post(f"{API_BASE_URL}/predict", json=user_data)
    return response.json()

def track_progress(user_id):
    response = requests.get(f"{API_BASE_URL}/track_progress", params={'user_id': user_id})
    return response.json()

st.sidebar.title("Loan Application")

user_id = st.sidebar.text_input("User ID")
income = st.sidebar.number_input("Annual Income ($)", min_value=0)
credit_score = st.sidebar.slider("Credit Score", 300, 850, 700)
loan_amount = st.sidebar.number_input("Loan Amount ($)", min_value=1000)
loan_term = st.sidebar.slider("Loan Term (years)", 1, 30, 15)
debt_to_income = st.sidebar.slider("Debt-to-Income Ratio", 0.0, 1.0, 0.3)

if st.sidebar.button("Check Loan Eligibility"):
    user_data = {
        'user_id': user_id, 'income': income, 'credit_score': credit_score,
        'loan_amount': loan_amount, 'loan_term': loan_term, 'debt_to_income': debt_to_income
    }
    result = predict_loan(user_data)

    st.header("Loan Eligibility Results")
    if result['eligible']:
        st.success("You are eligible for the loan!")
    else:
        st.error("You are not eligible at this time.")

    st.metric("Approval Probability", f"{result['probability']*100:.1f}%")
    st.metric("Estimated Monthly Payment", f"${result['monthly_payment']:.2f}")

if st.sidebar.button("Track Application Status"):
    progress = track_progress(user_id)
    st.header("Application History")
    st.write(progress)
