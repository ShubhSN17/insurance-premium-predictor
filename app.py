import streamlit as st
import pickle 
#st.title('Health Insurance Premium Prediction')
#age = st.number_input('Age:')
#bmi = st.number_input('BMI:')
#children = st.number_input('No. of Children:')
#gender = st.radio('Select Gender:',['Male','Female'])
#smoker = st.radio('Do you Smoke?',['Yes','No'])

# Custom Page Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏥 Premium Prediction</h1>", unsafe_allow_html=True)
st.write("Fill in your details below to predict your health insurance premium.")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age:", min_value=18, max_value=100, value=25)
    bmi = st.number_input("BMI:", min_value=10.0, max_value=50.0, value=25.0)

with col2:
    children = st.number_input("No. of Children:", min_value=0, max_value=10, value=0)
    gender = st.radio("Select Gender:", ["Male", "Female"])
    smoker = st.radio("Do you Smoke?", ["Yes", "No"])

# Load Model
model = pickle.load(open('model.pkl','rb'))

# Prediction button
if st.button('🔮 Predict'):
    gender_val = 0 if gender == 'Male' else 1
    smoker_val = 0 if smoker == 'No' else 1
    
    x_test = [[age, gender_val, bmi, children, smoker_val]]
    yp = round(model.predict(x_test)[0], 2)

    st.success(f"✅ Your Predicted Premium is: {yp}")

    st.info("ℹ️ This prediction is based on a trained ML model and may not reflect actual premiums.")

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        height: 50px;
        width: 220px;
    }
    .stRadio>div {
        flex-direction: row; /* horizontal radio buttons */
    }
    </style>
""", unsafe_allow_html=True)