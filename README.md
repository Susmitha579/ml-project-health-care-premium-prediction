# 🏥 Health Care Premium Prediction

## 📌 Project Overview

Health Care Premium Prediction is a Machine Learning-based web application that predicts an individual's health insurance premium based on personal details, medical history, lifestyle, income, and insurance plan.

The project uses regression models to estimate insurance costs and provides an interactive user interface developed using **Streamlit**.

The application uses separate trained models for different age groups to improve prediction performance.

## 🎯 Objectives

- Predict health insurance premiums based on individual characteristics.
- Analyze the impact of medical history and lifestyle on insurance costs.
- Apply Machine Learning regression techniques to real-world insurance data.
- Develop an interactive and user-friendly web application.
- Provide quick and data-driven insurance cost estimations.

## 🚀 Features

- Interactive Streamlit web interface.
- Age-based prediction using separate trained models.
- User-friendly dropdowns for categorical features.
- Numeric inputs for personal and financial information.
- Medical risk score calculation based on medical history.
- Data preprocessing and feature encoding.
- Feature scaling before prediction.
- Instant insurance premium prediction.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Manipulation |
| NumPy | Numerical Operations |
| Scikit-learn | Data Preprocessing and Scaling |
| XGBoost | Machine Learning Regression |
| Joblib | Model Serialization |
| Streamlit | Web Application Development |
| Git & GitHub | Version Control |

## 📊 Input Features

The application accepts the following features:

| Feature | Description | Input Type |
|---|---|---|
| Age | Individual's age | Numeric |
| Gender | Male / Female | Dropdown |
| Region | Geographical region | Dropdown |
| Marital Status | Married / Unmarried | Dropdown |
| Number of Dependants | Number of dependent family members | Numeric |
| BMI Category | Body Mass Index category | Dropdown |
| Smoking Status | Smoking habits | Dropdown |
| Employment Status | Employment category | Dropdown |
| Income Level | Annual income category | Dropdown |
| Income in Lakhs | Annual income | Numeric |
| Medical History | Existing medical conditions | Dropdown |
| Insurance Plan | Bronze / Silver / Gold | Dropdown |
| Genetical Risk | Genetic risk factor | Numeric |

## 🤖 Machine Learning Approach

The project follows these steps:

1. **Data Collection:** Collect health insurance-related data.
2. **Data Cleaning:** Handle missing values, duplicates, and inconsistent data.
3. **Exploratory Data Analysis:** Analyze relationships between input variables and insurance premiums.
4. **Feature Engineering:** Create meaningful features such as normalized medical risk scores.
5. **Encoding:** Convert categorical variables into numerical representations.
6. **Feature Scaling:** Scale selected numerical features.
7. **Model Training:** Train separate regression models for different age groups.
8. **Prediction:** Use the appropriate trained model to estimate insurance costs.

### Age-Based Model Selection

The application uses two trained models:

- `model_young.joblib` – Used for individuals aged 25 or below.
- `model_rest.joblib` – Used for individuals above 25.

Corresponding scalers are used for preprocessing the input features.

## 📁 Project Structure

```text
ml-project-health-care-premium-prediction/
│
├── Artifacts/
│   ├── model_rest.joblib
│   ├── model_young.joblib
│   ├── scaler_rest.joblib
│   └── scaler_young.joblib
│
├── main.py
├── prediction_helper.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Susmitha579/ml-project-health-care-premium-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd ml-project-health-care-premium-prediction
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
python -m streamlit run main.py
```

The application will open automatically in your browser.

## 📈 Prediction Workflow

```text
        User Input
             |
             v
    Data Preprocessing
             |
             v
    Feature Engineering
             |
             v
    Medical Risk Calculation
             |
             v
      Feature Scaling
             |
             v
     Age-Based Model Selection
             |
        +----+----+
        |         |
        v         v
   Young Model  Rest Model
        |         |
        +----+----+
             |
             v
     Premium Prediction
             |
             v
      Display Result
```

## 📦 Requirements

The project dependencies are listed in `requirements.txt`.

Main libraries:

- pandas
- numpy
- scikit-learn
- xgboost
- joblib
- streamlit

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

General deployment steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the project repository.
5. Choose `main.py` as the application entry point.
6. Deploy the application.

## 🔮 Future Enhancements

- Improve prediction accuracy through advanced regression algorithms.
- Add interactive data visualizations.
- Provide personalized insurance recommendations.
- Integrate additional health-related parameters.
- Develop a comparison system for different insurance plans.
- Improve the user interface and overall user experience.

## 👨‍💻 Author

**Susmitha**

Computer Science and Engineering Student

### Connect with Me

- GitHub: https://github.com/Susmitha579
- LinkedIn: https://www.linkedin.com/in/susmitha-avuku-017a9b2b6

---

⭐ If you find this project interesting, consider giving it a star!

**Note:** The predicted insurance premium is an estimated value generated by a Machine Learning model and should not be considered an actual insurance quotation.# ml-project-health-care-premium-prediction
Codebasics ML Course Health Insurance Prediction Project
