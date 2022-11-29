import pickle
import streamlit as st
import time

# Import pickle data 
pickle_in = open("model.pkl","rb")
export = pickle.load(pickle_in)
pickle_in.close()

# Variables
model_best = export['model']
scaler = export['scaler']
le_purchased = export['le_purchased']
X_col_names = export['X_col_names']

def prediction(age, salary):

    if age and salary:

        X = [[int(age), int(salary)]]
        # Mise à l'échelle
        X_scaled = scaler.transform(X)
        # Prédiction
        prediction_raw = model_best.predict(X_scaled)
        prediction = le_purchased.inverse_transform(prediction_raw)

        if prediction_raw == 0: 
            message = "This customer will not purchase the product."
        elif prediction_raw == 1:
            message = "This customer will purchase the product."
        else :
            message = "Bug"

    else : 
        message = "Please select your age and salary."

    # print("Prédiction : ", message) 
    return message


# Streamlit
st.set_page_config(
    page_title="Social Network Ads Prediction",
    page_icon=":globe_with_meridians:",
    #  layout="wide",
    initial_sidebar_state="expanded"
)

with st.container():
    st.title(':globe_with_meridians: Social Network Ads Prediction')
    st.subheader('Enter age and salary to get prediction')

with st.container():
    age = st.slider("Enter customer's age", 0, 100, 25)
    salary = st.slider("Please enter customer's salary", 0, 200000, 10000, 1000)
    if 'my_button' in st.session_state:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.header(prediction(age, salary))
            # st.success('Done!')
            # st.balloons()

# st.write(st.session_state) 
if 'my_button' not in st.session_state:
    st.session_state.my_button = True
