Project Overview
The Loan Eligibility Prediction System is a Machine Learning-based application developed using Python, Flask, SQLite, and Scikit-learn.
The system predicts whether a loan application will be Approved or Rejected based on applicant details such as income, education, credit history, employment status, and property area.

The project also includes:
Automated loan eligibility prediction
Fraud detection using duplicate Aadhar number checking
Applicant data storage using SQLite database
Database viewing system for stored applications

🎯 Objectives
Predict loan eligibility using Machine Learning
Reduce manual loan verification process
Detect duplicate applications using Aadhar number
Store applicant details securely in a database
Improve speed and accuracy of loan approval systems

🛠 Technologies Used
Programming Language
Python
Framework
Flask
Database
SQLite

Machine Learning
Scikit-learn
Random Forest Classifier
Frontend
HTML
CSS

Project structure:

LOAN_PREDICTION/
│
├── loan_app.py
├── train_model.py
├── database.py
├── view_database.py
├── scheme.sql
├── loan_dataset.csv
├── loan_model.pkl
├── label_encoders.pkl
├── loan_data.db
│
├── templates/
│   ├── index.html
│   └── view_database.html
│
└── README.md

⚙ Features
Loan approval prediction
Fraud detection using duplicate Aadhar number
Applicant information storage
Mobile number support
Database viewing page
User-friendly interface

🧠 Machine Learning Algorithm
Random Forest Classifier
The Random Forest algorithm is used to predict loan eligibility based on applicant details.
Input Features
Gender
Marital Status
Education
Self Employment
Applicant Income
Coapplicant Income
Loan Amount
Loan Term
Credit History
Property Area

Output
Loan Approved
Loan Rejected

🗄 Database Details
Database Name
loan_data.db
Table Name
applicants
Stored Information

Name
Aadhar Number
Mobile Number
Gender
Education
Income Details
Loan Amount
Credit History
Loan Status

▶ How to Run the Project
Step 1: Install Required Libraries
pip install flask numpy pandas scikit-learn
Step 2: Train the Model
python train_model.py
Step 3: Run the Loan Application
python loan_app.py
Step 4: View Stored Database Records
python view_database.py

📊 Dataset Information
The dataset contains loan applicant information used for training the Machine Learning model.
Dataset Attributes
Applicant Income
Coapplicant Income
Loan Amount
Education
Credit History
Property Area
Loan Status

🚨 Fraud Detection
The system checks whether an Aadhar number already exists in the database.
If a duplicate Aadhar number is found, the system displays a fraud alert message.

📈 Future Enhancements
Real-time bank verification
Aadhaar API integration
Credit score integration
Multi-language support
Cloud database support
Mobile application deployment

📚 References
Websites
https://flask.palletsprojects.com/
https://scikit-learn.org/
https://www.sqlite.org/
https://pandas.pydata.org/

Books
Hands-On Machine Learning with Scikit-Learn and TensorFlow — Aurélien Géron
Python Machine Learning — Sebastian Raschka
Flask Web Development — Miguel Grinberg

👩‍💻 Developed By
JananiFinal Year – Artificial Intelligence and Data Science
