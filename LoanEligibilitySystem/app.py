from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key_for_session"  # Needed for session management

# Function to insert application data into the database
def insert_application(data):
    conn = sqlite3.connect("data/loan_applications.db")
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

# ✅ Route for Language Selection Page
@app.route("/", methods=["GET", "POST"])
def select_language():
    if request.method == "POST":
        selected_language = request.form.get("language")
        session["language"] = selected_language  # Store the language in session
        return redirect(url_for("home"))  # Redirect to the main form page
    
    return render_template("language.html")

# ✅ Route for Main Form (Language-based)
@app.route("/form", methods=["GET", "POST"])
def home():
    language = session.get("language", "english")  # Get the selected language, default is English

    if request.method == "POST":
        name = request.form.get("name", "Not Provided")
        aadhar = request.form.get("aadhar", "Not Provided")
        mobile = request.form.get("mobile", "Not Provided")
        gender = request.form.get("gender", "Not Provided")
        married = request.form.get("married", "Not Provided")
        education = request.form.get("education", "Not Provided")
        self_employed = request.form.get("self_employed", "Not Provided")
        applicant_income = request.form.get("applicant_income", "0")
        coapplicant_income = request.form.get("coapplicant_income", "0")
        loan_amount = request.form.get("loan_amount", "0")
        loan_term = request.form.get("loan_term", "0")
        credit_history = request.form.get("credit_history", "0")
        property_area = request.form.get("property_area", "Not Provided")
        credit_score = request.form.get("credit_score", "0")
        verified_income = request.form.get("verified_income", "0")
        fraud_alerts = request.form.get("fraud_alerts", "None")
        existing_loan_status = request.form.get("existing_loan_status", "Unknown")
        property_owned = request.form.get("property_owned", "None")

        application_data = (
            name, aadhar, mobile, gender, married, education, self_employed,
            int(applicant_income), int(coapplicant_income), int(loan_amount), int(loan_term), int(credit_history),
            property_area, int(credit_score), int(verified_income), fraud_alerts, existing_loan_status, property_owned
        )

        insert_application(application_data)

        return "Application submitted successfully!"

    return render_template(f"form_{language}.html")  # Load form based on selected language

# ✅ Route to View Data
@app.route("/view")
def view_data():
    conn = sqlite3.connect("data/loan_applications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()
    conn.close()
    return render_template("view.html", applications=applications)

if __name__ == "__main__":
    app.run(debug=True)
