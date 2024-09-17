## **Diabetes Prediction App**

### **Overview**

This **Diabetes Prediction App** is a web-based application built using **Streamlit** that predicts whether a person has diabetes based on key medical features. The app utilizes a fine-tuned **Logistic Regression** model, trained on the **Pima Indians Diabetes Database**, to make predictions. Users can input their medical information, such as glucose level, blood pressure, and age, and the app will output whether they are at risk of having diabetes.

### **Features**

- **User-friendly interface**: Allows users to input relevant medical details like glucose level, BMI, insulin levels, and more.
- **Logistic Regression model**: The app is powered by a fine-tuned Logistic Regression model, optimized using **GridSearchCV** for better accuracy.
- **Real-time predictions**: After providing the necessary input values, the app predicts whether the user has diabetes and displays the prediction instantly.
- **Model accuracy**: The app also shows the model's accuracy, indicating how well it performs based on training data.

### **How It Works**

Users input the following features:

- Number of pregnancies
- Glucose level
- Blood pressure
- Insulin level
- BMI (Body Mass Index)
- Diabetes pedigree function (genetic risk factor)
- Age

Upon clicking the **"Predict"** button, the app uses the Logistic Regression model to predict whether the user is likely to have diabetes.

### **The app then displays:**

- **Prediction**: Whether the user has diabetes ("Diabetes") or not ("No Diabetes").
- **Model Accuracy**: The accuracy of the Logistic Regression model, based on the cross-validation process during model training.

### **How to Run the App**

Clone this repository:

```bash
git clone https://github.com/your-username/diabetes-prediction-app.git

Navigate into the project directory:
```bash
cd diabetes-prediction-app

```bash
pip install -r requirements.txt

Run the Streamlit app:
```bash
streamlit run app.py
Open your browser at the displayed local URL to interact with the app.

## Requirements
Python 3.x
Streamlit
Scikit-learn
Numpy
Joblib
Model
The Logistic Regression model used in this app has been fine-tuned using GridSearchCV with the following parameters:

C: [0.1, 1, 10]
solver: ['liblinear', 'lbfgs']
The model has been trained on the Pima Indians Diabetes Dataset, which contains medical records of women with a family history of diabetes.
