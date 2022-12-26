import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import streamlit as st

# load the data
df = pd.read_csv("admissions_data.csv")

# split the data into training and test sets
X = df.drop("Chance of Admit", axis=1)
y = df["Chance of Admit"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train the model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions on the test set
y_pred = model.predict(X_test)

# evaluate the model's performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

# create the Streamlit app
st.title("Admission Prediction App")

# add a form for inputting data
input_data = st.empty()
gre_score = input_data.number_input("GRE Score (out of 340)", min_value=0, max_value=340)
toefl_score = input_data.number_input("TOEFL Score (out of 120)", min_value=0, max_value=120)
university_rating = input_data.number_input("University Rating (out of 5)", min_value=1, max_value=5)
sop_strength = input_data.number_input("Statement of Purpose (out of 5)", min_value=1, max_value=5)
lor_strength = input_data.number_input("Letter of Recommendation Strength (out of 5)", min_value=1, max_value=5)
undergraduate_gpa = input_data.number_input("Undergraduate GPA (out of 10)", min_value=0, max_value=10)
research_experience = input_data.radio("Research Experience", ("Yes", "No"))

#convert the research experience input to a binary value
if research_experience == "Yes":
  research_experience = 1
else:
  research_experience = 0

#create a prediction button
if input_data.button("Predict"):
# create a dictionary with the input data
data = {
"GRE Score": gre_score,
"TOEFL Score": toefl_score,
"University Rating": university_rating,
"SOP": sop_strength,
"LOR ": lor_strength,
"CGPA": undergraduate_gpa,
"Research": research_experience,
}

# make a prediction using the model
prediction = model.predict([data])

# display the prediction
st.write(f"Chance of Admit: {prediction[0]:.2f}")
st.run()
