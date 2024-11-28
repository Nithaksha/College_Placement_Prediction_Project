import streamlit as st
import sqlite3
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Connect to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('placement_data.db')
cursor = conn.cursor()

# Create the table to store placement data if it doesn't exist (removed 'age' column)
cursor.execute('''CREATE TABLE IF NOT EXISTS placement_data (
                    id INTEGER PRIMARY KEY,
                    gender TEXT,
                    stream TEXT,
                    internship INTEGER,
                    cgpa FLOAT
                    )''')

# Function to save data to the database
def save_to_db(gender, stream, internship, cgpa):
    cursor.execute('''INSERT INTO placement_data (gender, stream, internship, cgpa)
                      VALUES (?, ?, ?, ?)''', (gender, stream, internship, cgpa))
    conn.commit()

# Load the model and encoders
with open('saved_steps1.pkl', 'rb') as f:
    data = pickle.load(f)
    SVM = data["Model"]
    gender_encoder = data["Gender"]
    stream_encoder = data["Stream"]

# Streamlit App
st.title("College Placement Prediction for 2025 Batch")

st.write("### Please provide the following details for placement prediction")

# Input options
Gender = ("Male", "Female")
Stream = (
    "Electronics And Communication",
    "Computer Science",
    "Information Technology",
    "Mechanical",
    "Electrical",
    "Civil",
)

# Streamlit input widgets
gender_input = st.selectbox("Gender", Gender)
stream_input = st.selectbox("Stream", Stream)
internship_input = st.selectbox("Number of Internships", list(range(6)))
cgpa_input =st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)


# Preprocess inputs for prediction
X = np.array([[gender_input, stream_input, internship_input, cgpa_input]])

# Apply label encoding
X[:, 0] = gender_encoder.transform(X[:, 0])
X[:, 1] = stream_encoder.transform(X[:, 1])

# Convert data to float for prediction
X = X.astype(float)

# Empty container for buttons to align them to the right
button_container = st.empty()
# Place the "Submit" button in the same location as the "Predict" button (right corner)
with button_container:
    # Prediction
    if st.button("Predict"):
        prediction = SVM.predict(X)
        if prediction[0] == 1:
            st.success("Congratulations! You have a high chance of getting placed.")
        else:
            st.error("Placement chances may be low. Consider improving your profile.")

# Insert the data into the database
if st.button("Submit"):
    # Save data to the database
        save_to_db(gender_input, stream_input, internship_input, cgpa_input)
        
        st.write("Data has been saved to the database.")

# Display the stored records in the database
st.write("### View Stored Placement Data")

# Fetch all records from the database
cursor.execute('SELECT * FROM placement_data')
records = cursor.fetchall()

# If records are found, display them in a table
if records:
    df = pd.DataFrame(records, columns=["ID", "Gender", "Stream", "Internship", "CGPA"])
    st.write(df)
else:
    st.write("No records found.")

# Close the database connection after operations
conn.close()