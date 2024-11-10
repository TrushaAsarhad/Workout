import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import streamlit as st

# Load the dataset (replace with your actual file path)
df = pd.read_csv('data.csv')

# Data preprocessing
# Encode 'Gender' column (Male = 0, Female = 1)
df['Gender'] = df['Gender'].apply(lambda x: 1 if x == 'Female' else 0)

# Features: Weight, Height, Age, Gender
X = df[['Weight', 'Height', 'Age', 'Gender']]

# Target: BMI case categories (assuming 'BMIcase' is the column you want to predict)
y = df['BMIcase']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
st.write("Classification Report:")
st.write(classification_report(y_test, y_pred))

# Function to recommend exercises based on the predicted BMI category
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


# Streamlit app to take user input and recommend exercises
def app():
    st.title("BMI Prediction & Exercise Recommendation System")

    # User input for weight, height, age, gender
    st.subheader("Enter Your Details")
    weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)
    height = st.number_input("Height (m)", min_value=1.0, max_value=3.0, value=1.75)
    age = st.number_input("Age", min_value=10, max_value=120, value=25)
    gender = st.selectbox("Gender", options=["Male", "Female"])

    # Prepare the input for the model
    user_input = [[weight, height, age, 1 if gender == "Female" else 0]]
    user_input_scaled = scaler.transform(user_input)

    # Predict BMI category
    predicted_bmi_category = model.predict(user_input_scaled)[0]

    # Show the prediction and recommended exercises
    st.subheader(f"Predicted BMI Category: {predicted_bmi_category}")
    exercise_plan = recommend_exercise(predicted_bmi_category)
    st.subheader("Recommended Exercise Plan")
    st.write(exercise_plan)

# Run the app
if __name__ == "__main__":
    app()
