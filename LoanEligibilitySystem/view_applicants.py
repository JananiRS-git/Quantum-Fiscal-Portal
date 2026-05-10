import sqlite3

# Connect to the database
conn = sqlite3.connect("data/loan_applications.db")
cursor = conn.cursor()

# Fetch all applicant details
cursor.execute("SELECT * FROM applications")
rows = cursor.fetchall()

# Display results
if rows:
    print("Applicants Details:")
    for row in rows:
        print(row)
else:
    print("No applicants found.")

# Close connection
conn.close()
