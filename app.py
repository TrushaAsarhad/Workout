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
def recommend_exercise(bmi_case):
    recommendations = {
        'Underweight': ('1. Squats: 3 sets of 12 reps\n2. Deadlifts: 3 sets of 8 reps\n3. Bench Press: 3 sets of 10 reps\n...'),
        'Normal': ('1. Running: 30 mins, 4 days/week\n2. Elliptical Machine: 25 mins, 1 day/week\n3. Jump Rope: 15 mins, 2 days/week\n...'),
        'Overweight': ('1. Brisk Walking: 45 mins, 5 days/week\n2. Cycling: 30 mins, 3 days/week\n3. Swimming: 45 mins, 2 days/week\n...'),
        'Obese': ('1. Walking (Moderate pace): 30-45 mins, 5 days/week\n2. Aqua Aerobics: 45 mins, 3 days/week\n...'),
        'Severely Obese': ('1. Water Walking: 30 mins, 4 days/week\n2. Stationary Cycling: 20-30 mins, 3 days/week\n...'),
        'Morbidly Obese': ('1. Walking with Support: 15 mins, 4-5 days/week\n2. Aquatic Therapy: 30 mins, 4 days/week\n...')
    }
    return recommendations.get(bmi_case, 'No recommendations available')

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
