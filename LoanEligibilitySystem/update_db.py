import sqlite3

# Connect to the database
db_path = "data/loan_applications.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ✅ Get existing columns
cursor.execute("PRAGMA table_info(applications)")
columns = [col[1] for col in cursor.fetchall()]

# ✅ Add 'age' column if not exists
if "age" not in columns:
    cursor.execute("ALTER TABLE applications ADD COLUMN age INTEGER;")
    print("✅ 'age' column added successfully.")
else:
    print("⚠️ 'age' column already exists.")

# ✅ Add 'timestamp' column (WITHOUT DEFAULT)
if "timestamp" not in columns:
    cursor.execute("ALTER TABLE applications ADD COLUMN timestamp DATETIME;")
    print("✅ 'timestamp' column added successfully.")

    # ✅ Update existing rows with the current timestamp
    cursor.execute("UPDATE applications SET timestamp = datetime('now') WHERE timestamp IS NULL;")
    print("✅ Existing records updated with timestamps.")
else:
    print("⚠️ 'timestamp' column already exists.")

# ✅ Commit changes & close
conn.commit()
conn.close()
print("🎉 Database updated successfully!")
