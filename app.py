import streamlit as st
from predict import show_predict_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict"))

# if page == "Predict":
#     show_predict_page()