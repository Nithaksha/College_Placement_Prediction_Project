# College_Placement_Prediction_Project
# College Placement Prediction Web Application

An interactive web application developed using **Streamlit** and a **Support Vector Machine (SVM)** model to predict college placement chances. This project allows users to input academic and personal metrics, providing real-time predictions about the likelihood of securing a placement.

---

## Features

- **User-Friendly Interface**: Built using Streamlit for an intuitive, browser-based user experience.
- **Real-Time Predictions**: Utilizes an SVM model to deliver predictions instantly based on user input.
- **Input Parameters**:
  - Stream
  - Gender
  - Internships
  - CGPA
- **Dynamic Data Encoding**: Encodes categorical inputs for seamless machine learning integration.
- **High Accuracy**: Model trained and tested to ensure reliable predictions.

---

## Installation and Setup

### Prerequisites

Ensure the following are installed on your system:
- Python (>=3.8)
- pip (Python package manager)
- Streamlit

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/College-Placement-Prediction-Web-Application/college-placement-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd college-placement-prediction
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to the URL displayed in the terminal (default: `http://localhost:8501`).

---

## How It Works

1. The user inputs their details, such as:
   - **Stream** (e.g., Electronics, Computer Science etc)
   - **Gender**
   - **Number of Internships**
   - **CGPA** (Cumulative Grade Point Average)

2. The app encodes categorical inputs dynamically and feeds the data into the SVM model.

3. The SVM model predicts the likelihood of the user securing a placement and displays the result on the interface.

---

## Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit
- **Machine Learning**: Support Vector Machine (SVM)

---

## Future Enhancements

- Incorporate additional input parameters for improved predictions.
- Provide visualizations of placement trends based on input data.
- Add support for more machine learning models for comparative analysis.
- Deploy the app online for broader accessibility.

---

## License

This project is licensed under the MIT License. Please take a look at the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Streamlit documentation and community for making UI development straightforward.
- Scikit-learn for the robust implementation of the SVM model.
