from re import S
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Welcome to My Application for prediction of Diamond Price")
st.image("https://audhiaprilliant.github.io/assets/images/21-0.jpg")

# import the dataset
df = pd.read_csv("diamonds.csv")

option = st.selectbox(
     'How would you like to be get about the data?',
     ('Head', 'Tail', 'Full'))

if option == 'Head':
    st.write(df.head())
elif option == 'Tail':
    st.write(df.tail())
else:
    st.write(df)

# make a split of numerical and categorical columns
numerical = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
categorical = df.loc[:, ~df.columns.isin(numerical)].columns
st.text("The Numerical Columns are: ")
for i in numerical:
    st.markdown("- " + i)
st.text("The Categorical Columns are: ")
for i in categorical:
    st.markdown("- " + i)

# The bar plot of some of the column are:

option = st.selectbox(
    "Select the count plot of categorical columns",
    ("cut", "clarity", "color"))
if option == "cut":
    st.bar_chart(df['cut'].value_counts())  
elif option == "clarity":
    st.bar_chart(df['clarity'].value_counts())
else:
    st.bar_chart(df['color'].value_counts())