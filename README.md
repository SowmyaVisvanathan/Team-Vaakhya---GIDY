# AI-POWERED SMART LOAN AND FINANCIAL WELLNESS ASSISTANT

This project is an AI-powered loan assistant designed to help first-time borrowers by providing personalized loan guidance, financial planning, and loan eligibility predictions. The assistant leverages machine learning models to assess eligibility and offer tailored recommendations, empowering users to make informed decisions during the loan application process.

### Project Overview
The project consists of two main components:
1. **Backend** (Flask API & Machine Learning Model)
2. **Frontend** (Streamlit Web App)

### 1. Backend (Flask API & Machine Learning Model)
The backend is built using Flask to provide a REST API that handles user requests. It includes a machine learning model for loan eligibility prediction and an SQLite database for storing user loan applications.

- **Loan Eligibility Prediction**: A machine learning model predicts the eligibility of a loan application based on user data (e.g., income, credit score, loan amount).
- **Data Storage**: Loan applications are stored in an SQLite database for tracking and historical reference.
- **Chatbot Assistance**: A chatbot, powered by Rasa, assists users with financial queries and provides additional guidance.

#### Backend Workflow
1. The user submits financial details (income, credit score, loan amount, etc.).
2. The machine learning model evaluates the data and predicts loan approval or rejection.
3. The system calculates the monthly repayment amount.
4. Based on the data, personalized financial recommendations are provided.
5. The loan application details are saved in SQLite for tracking.

### 2. Frontend (Streamlit Web App)
The frontend is developed with Streamlit to provide a simple and interactive web interface where users can submit loan applications, receive instant eligibility results, view risk assessments, and interact with the chatbot.

#### Frontend Workflow
1. The user inputs loan details (income, credit score, loan amount, etc.) via the Streamlit UI.
2. Upon submitting, the details are sent to the Flask API for processing.
3. The system returns eligibility results, including loan approval probability and monthly payment estimates.
4. If rejected, the system offers suggestions for improving loan approval chances.
5. Users can interact with the AI assistant for additional financial guidance.
6. Loan history is available for users to view their past applications.

### Technologies Used
- **Backend**: Flask (API), SQLite (Database), Scikit-learn (Machine Learning), Rasa (Chatbot), Pickle (Model Serialization)
- **Frontend**: Streamlit (UI), Altair (Data Visualization), Custom CSS (UI Design)
### Website Preview:
![image](https://github.com/user-attachments/assets/7aa5b269-9c29-44f0-9ba1-53ce3c5ee3e1)


### How It Works
1. **User Inputs Loan Details**: The user provides necessary details such as income, credit score, loan type, and loan amount.
2. **Loan Eligibility Prediction**: The machine learning model (Random Forest Classifier) analyzes the data to predict whether the loan will be approved or rejected.
3. **Financial Guidance & Recommendations**: Personalized suggestions are provided to improve the user’s financial standing, based on the loan eligibility prediction.
4. **Application Tracking**: User loan applications are stored in an SQLite database for easy tracking.
5. **Chatbot Assistance**: The chatbot helps answer frequently asked questions and provides advice on loan options and financial planning.

### Real-World Use Cases
- **Banks & Fintech Companies**: Automates the loan approval process and provides AI-based customer support.
- **Personal Finance Management**: Helps users assess loan eligibility and make informed financial decisions.
- **Educational Purposes**: Demonstrates the application of AI in financial decision-making.

### Future Improvements
- **Model Enhancement**: Improving the machine learning model’s accuracy with more extensive and real-world banking datasets.
- **Chatbot Expansion**: Adding more features to the chatbot for personalized financial planning.
- **Deployment**: Hosting the backend on Heroku and the frontend on Streamlit Cloud for better accessibility.
- **User Authentication**: Integrating OAuth or Google Sign-In for secure user authentication.

---

