import sqlite3

def check_fraud(aadhar):
    conn = sqlite3.connect("data/loan_applications.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT fraud_alerts FROM applications WHERE aadhar = ?", (aadhar,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result and result[0]:
        return result[0]  # Fraud alert message
    return "No Fraud Detected"
