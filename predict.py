import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

#Load the model
# Load the model
#model = pickle.load(open('saved_steps.pkl', 'rb'))
with open('saved_steps1.pkl', 'rb') as f:
    data = pickle.load(f)
    SVM = data["Model"]
    a = data["Gender"]
    s = data["Stream"]

# def show_predict_page():
st.title("College Placement Details for 2025 batch")

st.write("""### We need some information to predict the placement records""")

Gender = (
        "Male",
        "Female",
    )

Stream = (
        "Electronics And Communication",
        "Computer Science",
        "Information Technology",
        "Mechanical",
        "Electrical",
        "Civil",
    )

Gender = st.selectbox("Gender", Gender)
Stream = st.selectbox("Stream", Stream)

Internship = st.slider("Internship Experience", 0, 1, 2)
CGPA = st.slider("Marks scored", 8, 9, 10)

X = np.array([[Gender, Stream, Internship,CGPA]])

#X = np.array([[Gender, Stream, Internship,CGPA]])
a = LabelEncoder()
gender = ['Male','Female']
a.fit(gender)
s = LabelEncoder()
X[:, 1] = a.transform(X[:,1])
# Now, you can safely transform 'Education' values
X[:, 2] = s.transform(X[:, 2])

if st.button("Predict"):
    prediction = data.predict(X)
    if prediction[0] == 1:
        st.success("Congratulations! You have a high chance of getting placed.")
    else:
        st.error("Placement chances may be low. Consider improving your profile.")
