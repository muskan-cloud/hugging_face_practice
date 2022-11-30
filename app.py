import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# odd or even
""")

st.header('User Input Parameters')

number=st.number_input("number")
data = {'number': number }
features = pd.DataFrame(data, index=[0])

if number % 2 == 0:
  st.write('even')
else:
  st.write('odd')
