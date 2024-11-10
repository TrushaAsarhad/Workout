import streamlit as st
import pandas as pd

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    elif 30 <= bmi < 34.9:
        return 'Obese'
    elif 35 <= bmi < 39.9:
        return 'Severely Obese'
    else:
        return 'Morbidly Obese'

# Function to get exercise recommendations based on BMI category
# Define a function to assign very detailed exercise recommendations based on BMI category
def recommend_exercise(bmi_case):
    if bmi_case == 'underweight':
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

    elif bmi_case == 'normal':
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

    elif bmi_case == 'over weight':
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

    elif bmi_case == 'obese':
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

    elif bmi_case == 'severe obese':
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

    elif bmi_case == 'morbidly obese':
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

    elif bmi_case == 'extremely obese':
        return ('1. Short-Distance Walking with Support: 15 mins, 4-5 days/week\n'
                '2. Chair-Based Cardio: 15-20 mins, 4 days/week\n'
                '3. Seated Leg Press (with light resistance): 2 sets of 8 reps, 2 days/week\n'
                '4. Resistance Band Rows (seated): 2 sets of 10 reps, 2 days/week\n'
                '5. Supported Squats: 1 set of 10 reps, 2 days/week\n'
                '6. Seated Side Bends: 15 mins, daily\n'
                '7. Breathing Exercises (e.g., diaphragmatic breathing): 10 mins, daily\n'
                '8. Gentle Stretching Routine: 10 mins, daily\n'
                '9. Progressive Muscle Relaxation: 10 mins, 3 days/week\n'
                '10. Consult with a physician for personalized guidance and safety')

    else:
        return 'No recommendation available'


# Streamlit app layout
def app():
    st.title("BMI-Based Exercise Recommendation System")
    
    # File upload widget (to upload data.csv)
    uploaded_file = st.file_uploader("Upload Your Dataset (CSV)", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())  # Show the first few rows of the dataset

    # User input for weight, height, age, gender
    st.subheader("Enter Your Details")
    weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)
    height = st.number_input("Height (m)", min_value=1.0, max_value=3.0, value=1.75)
    age = st.number_input("Age", min_value=10, max_value=120, value=25)
    gender = st.selectbox("Gender", options=["Male", "Female"])

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    # Display BMI and category
    st.subheader(f"Your BMI: {bmi:.2f}")
    st.subheader(f"Your BMI Category: {category}")

    # Get and display exercise recommendations based on BMI category
    exercise_plan = recommend_exercise(category)
    st.subheader("Recommended Exercise Plan")
    st.write(exercise_plan)

# Run the app
if __name__ == "__main__":
    app()
