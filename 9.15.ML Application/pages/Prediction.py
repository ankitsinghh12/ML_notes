import streamlit as st
import pickle
import numpy as np

st.title("Welcome to My Application for prediction of Diamond Price")
st.subheader("Enter the required detials about the diamond to predict the price in USD")

carat = st.number_input("Enter the carat of the diamond: ", min_value=0.2, max_value=5.01)

st.text("enter the cut details based on the data given below:")
st.text("Fair: 1, Good: 2, Very Good: 3, Premium: 4, Ideal: 5")

cut = st.number_input("Enter the cut details of the diamond:" , min_value= 1, max_value=5)

st.text("enter the color details based on the data given below:")
st.text("'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7")

color = st.number_input("Enter the color details of the diamond:" , min_value= 1, max_value= 7)

st.text("enter the clarity details based on the data given below:")
st.text("I1: 1, SI2: 2, SI1: 3, VS2: 4, VS1: 5, VVS2: 6, VVS1: 7, IF: 8")

clarity = st.number_input("Enter the clarity details of the diamond:" , min_value= 1, max_value= 8)

depth = st.number_input("enter the depth of the diamond: ", min_value= 43, max_value= 79)

table = st.number_input("Enter the table dimmension of the diamond: ", min_value= 43, max_value= 95)

x = st.number_input("Enter the x dimension of the diamond in mm: ", min_value= 0.0, max_value= 10.74)

y = st.number_input("Enter the y dimmensions of the diamond in mm: ", min_value= 0.0, max_value= 58.9)

z = st.number_input("Enter the z dimmensions of the diamond in mm: ", min_value= 0.0, max_value= 31.8)

click = st.button("Predict")

knn_model = pickle.load(open("models/random_forest_regression_model.pkl", "rb"))
standard_scaler = pickle.load(open("models/standard_scaler.pkl", "rb"))

if click == True:
    if carat and cut and color and clarity and depth and table and x and y and z:
        categorical_data = [[cut, color, clarity]]
        numerical_data = [[carat, depth, table, x, y, z]]
        standard_data = standard_scaler.transform(numerical_data)
        final_data = np.concatenate((standard_data, categorical_data), axis=1)
        prediction = knn_model.predict(final_data)
        st.success("The price of the diamond in USD  is: " + str(prediction[0]))
    else:
        st.error("Enter the values properly.")