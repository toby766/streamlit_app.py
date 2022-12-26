import streamlit as st

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


# display the prediction
st.run()
