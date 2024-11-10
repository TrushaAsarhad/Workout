import joblib
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the saved model and scaler
model = joblib.load('bmi_predictor_model.pkl')  # Adjust path as needed
scaler = joblib.load('scaler.pkl')  # Adjust path as needed

# Streamlit app title
st.title('BMI Exercise Recommendation System')

# User input fields
weight = st.number_input('Enter your weight (kg)', min_value=30.0, max_value=200.0, value=70.0, step=0.1)
height = st.number_input('Enter your height (m)', min_value=1.2, max_value=2.5, value=1.75, step=0.01)
age = st.number_input('Enter your age', min_value=18, max_value=100, value=30, step=1)
gender = st.radio('Select your gender', ['Male', 'Female'])

# Gender encoding
gender = 1 if gender == 'Female' else 0

# Prepare the input data
user_input = np.array([[weight, height, age, gender]])

# Scale the input data using the loaded scaler
user_input_scaled = scaler.transform(user_input)

# Make the prediction using the trained model
bmi_case = model.predict(user_input_scaled)

# Map BMI case to readable labels
bmi_labels = {
    0: 'Underweight',
    1: 'Normal',
    2: 'Overweight',
    3: 'Obese',
    4: 'Severely Obese',
    5: 'Morbidly Obese'
}

# Get the BMI category
bmi_category = bmi_labels.get(bmi_case[0], 'Unknown')

# Define a function to assign detailed exercise recommendations based on BMI category
def recommend_exercise(bmi_category):
    if bmi_category == 'Underweight':
        return ('1. Squats: 3 sets of 12 reps, 2 days/week\n'
                '2. Deadlifts: 3 sets of 8 reps, 2 days/week\n'
                '3. Bench Press: 3 sets of 10 reps, 2 days/week\n'
                '4. Pull-Ups/Assisted Pull-Ups: 2 sets of 8 reps, 2 days/week\n'
                '5. Leg Press: 3 sets of 12 reps, 1 day/week\n'
                '6. Dumbbell Shoulder Press: 3 sets of 10 reps, 2 days/week\n'
                '7. Cycling (Moderate pace): 20 mins, 2 days/week\n'
                '8. Light Jogging: 15 mins, 2 days/week\n'
                '9. Foam Rolling for Muscle Recovery: 15 mins, daily\n'
                '10. High-Protein Diet with supplements (as recommended by a nutritionist)')

    elif bmi_category == 'Normal':
        return ('1. Running: 30 mins, 4 days/week\n'
                '2. Elliptical Machine: 25 mins, 1 day/week\n'
                '3. Jump Rope: 15 mins, 2 days/week\n'
                '4. Bench Press: 3 sets of 10 reps, 2 days/week\n'
                '5. Squats: 3 sets of 15 reps, 2 days/week\n'
                '6. Lunges: 3 sets of 12 reps per leg, 2 days/week\n'
                '7. Yoga (Hatha or Vinyasa): 20 mins, 3 days/week\n'
                '8. Dynamic Stretching Routine: 10 mins, daily\n'
                '9. Planks: 3 sets of 30 seconds, 3 days/week\n'
                '10. Core Exercises (e.g., leg raises, Russian twists): 3 sets of 15 reps, 3 days/week')

    elif bmi_category == 'Overweight':
        return ('1. Brisk Walking: 45 mins, 5 days/week\n'
                '2. Cycling: 30 mins, 3 days/week\n'
                '3. Swimming: 45 mins, 2 days/week\n'
                '4. Resistance Band Squats: 3 sets of 12 reps, 3 days/week\n'
                '5. Dumbbell Rows: 3 sets of 10 reps, 3 days/week\n'
                '6. Leg Press: 3 sets of 15 reps, 2 days/week\n'
                '7. Yoga (e.g., Vinyasa Flow): 30 mins, 2 days/week\n'
                '8. Stretching Routine (e.g., hamstring and hip stretches): 15 mins, daily\n'
                '9. Calisthenics (e.g., push-ups, dips): 2 sets of 10 reps, 3 days/week\n'
                '10. Balanced Diet Plan with portion control and tracking calories')

    elif bmi_category == 'Obese':
        return ('1. Walking (Moderate pace): 30-45 mins, 5 days/week\n'
                '2. Aqua Aerobics: 45 mins, 3 days/week\n'
                '3. Recumbent Bike: 30 mins, 3 days/week\n'
                '4. Bodyweight Squats: 2 sets of 12 reps, 2 days/week\n'
                '5. Seated Leg Lifts: 2 sets of 10 reps, 3 days/week\n'
                '6. Chair Push-Ups: 2 sets of 8 reps, 3 days/week\n'
                '7. Wall Push-Ups: 2 sets of 10 reps, 3 days/week\n'
                '8. Tai Chi: 20 mins, 2 days/week\n'
                '9. Chair Yoga: 15 mins, 4 days/week\n'
                '10. Focus on a diet rich in vegetables, lean proteins, and whole grains with portion control')

    elif bmi_category == 'Severely Obese':
        return ('1. Water Walking: 30 mins, 4 days/week\n'
                '2. Stationary Cycling (Low resistance): 20-30 mins, 3 days/week\n'
                '3. Seated Leg Raises: 2 sets of 12 reps, 3 days/week\n'
                '4. Wall Push-Ups: 2 sets of 10 reps, 3 days/week\n'
                '5. Chair Squats: 2 sets of 8 reps, 2 days/week\n'
                '6. Seated Arm Circles: 2 sets of 15 reps, 3 days/week\n'
                '7. Stretching (e.g., neck and back stretches): 15 mins, daily\n'
                '8. Chair Yoga: 20 mins, 2 days/week\n'
                '9. Mindful Breathing Exercises: 10 mins, daily\n'
                '10. Consult a dietitian for a personalized, calorie-restricted nutrition plan')

    elif bmi_category == 'Morbidly Obese':
        return ('1. Walking with Support: 20 mins, 5 days/week\n'
                '2. Aquatic Therapy: 30 mins, 4 days/week\n'
                '3. Seated Marches: 2 sets of 15 reps, 3 days/week\n'
                '4. Leg Lifts (Seated): 2 sets of 10 reps, 3 days/week\n'
                '5. Arm Raises (Seated): 2 sets of 12 reps, 3 days/week\n'
                '6. Chair Push-Ups: 1 set of 8 reps, 2 days/week\n'
                '7. Breathing Exercises: 10 mins, daily\n'
                '8. Stretching Routine: 15 mins, daily\n'
                '9. Progressive Muscle Relaxation: 10 mins, 3 days/week\n'
                '10. Light Resistance Band Workouts: 2 sets of 8 reps, 2 days/week')

    else:
        return 'No recommendation available'

# Get the exercise recommendation based on BMI category
exercise_plan = recommend_exercise(bmi_category)

# Display results to the user
st.write(f'Your BMI category is: {bmi_category}')
st.write(f'Exercise Recommendation: {exercise_plan}')
