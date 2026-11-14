import pandas as pd
from joblib import load

model_rest = load("Artifacts/model_rest.joblib")
model_young = load("Artifacts/model_young.joblib")

scaler_rest = load("Artifacts/scaler_rest.joblib")
scaler_young = load("Artifacts/scaler_young.joblib")


# Calculate normalized medical risk
def calculate_normalized_risk(medical_history):

    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    diseases = medical_history.lower().split(" & ")

    total_risk_score = sum(
        risk_scores.get(disease.strip(), 0)
        for disease in diseases
    )

    max_score = 14

    normalized_risk_score = total_risk_score / max_score

    return normalized_risk_score


# Preprocess input
def preprocess_input(input_dict):

    expected_columns = [
        'age',
        'number_of_dependants',
        'income_lakhs',
        'insurance_plan',
        'genetical_risk',
        'normalized_risk_score',
        'gender_Male',
        'region_Northwest',
        'region_Southeast',
        'region_Southwest',
        'marital_status_Unmarried',
        'bmi_category_Obesity',
        'bmi_category_Overweight',
        'bmi_category_Underweight',
        'smoking_status_Occasional',
        'smoking_status_Regular',
        'employment_status_Salaried',
        'employment_status_Self-Employed'
    ]

    insurance_plan_encoding = {
        "Bronze": 1,
        "Silver": 2,
        "Gold": 3
    }

    df = pd.DataFrame(
        0,
        columns=expected_columns,
        index=[0]
    )

    for key, value in input_dict.items():

        if key == 'Gender' and value == 'Male':
            df['gender_Male'] = 1

        elif key == 'Region':
            if value == 'Northwest':
                df['region_Northwest'] = 1
            elif value == 'Southeast':
                df['region_Southeast'] = 1
            elif value == 'Southwest':
                df['region_Southwest'] = 1

        elif key == 'Marital Status' and value == 'Unmarried':
            df['marital_status_Unmarried'] = 1

        elif key == 'BMI Category':
            if value == 'Obesity':
                df['bmi_category_Obesity'] = 1
            elif value == 'Overweight':
                df['bmi_category_Overweight'] = 1
            elif value == 'Underweight':
                df['bmi_category_Underweight'] = 1

        elif key == 'Smoking Status':
            if value == 'Occasional':
                df['smoking_status_Occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_Regular'] = 1

        elif key == 'Employment Status':
            if value == 'Salaried':
                df['employment_status_Salaried'] = 1
            elif value == 'Self-Employed':
                df['employment_status_Self-Employed'] = 1

        elif key == 'Insurance Plan':
            df['insurance_plan'] = insurance_plan_encoding.get(value, 1)

        elif key == 'Age':
            df['age'] = value

        elif key == 'Number of Dependants':
            df['number_of_dependants'] = value

        elif key == 'Income in Lakhs':
            df['income_lakhs'] = value

    # Calculate normalized medical risk
    df['normalized_risk_score'] = calculate_normalized_risk(
        input_dict['Medical History']
    )

    # Apply scaling
    df = handle_scaling(input_dict['Age'], df)

    return df


# Scaling
def handle_scaling(age, df):

    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = None

    df[cols_to_scale] = scaler.transform(
        df[cols_to_scale]
    )

    df.drop('income_level', axis=1, inplace=True)

    return df


# Prediction
def predict(input_dict):

    input_df = preprocess_input(input_dict)

    # Select model based on age
    if input_dict["Age"] <= 25:
        model = model_young
    else:
        model = model_rest

    # Get expected features
    expected_features = model.feature_names_in_

    # Match input columns with model features
    input_df = input_df.reindex(
        columns=expected_features,
        fill_value=0
    )

    # Predict
    prediction = model.predict(input_df)

    return round(float(prediction[0]), 2)