import sqlite3

def create_database():
    conn = sqlite3.connect('data/loan_applications.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            aadhar TEXT UNIQUE,
            mobile TEXT,
            gender TEXT,
            married TEXT,
            education TEXT,
            self_employed TEXT,
            applicant_income INTEGER,
            coapplicant_income INTEGER,
            loan_amount INTEGER,
            loan_term INTEGER,
            credit_history INTEGER,
            property_area TEXT,
            credit_score INTEGER,
            verified_income INTEGER,
            fraud_alerts TEXT,
            existing_loan_status TEXT,
            property_owned TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_application(data):
    conn = sqlite3.connect('data/loan_applications.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO applications 
        (name, aadhar, mobile, gender, married, education, self_employed,
         applicant_income, coapplicant_income, loan_amount, loan_term, credit_history,
         property_area, credit_score, verified_income, fraud_alerts, existing_loan_status, property_owned)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    conn.commit()
    conn.close()

# Run this script once to create the database
if __name__ == "__main__":
    create_database()
