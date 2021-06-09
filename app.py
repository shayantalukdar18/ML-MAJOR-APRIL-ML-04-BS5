import streamlit as st
import joblib
model = joblib.load('imdb-pos-neg')
st.title('Sentiment Classifier')
ip = st.text_input("Enter the message [The result will be 0 or 1 where 0 = 'Negative' 1 = 'Positive']")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
