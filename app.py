import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot = pipeline("text-generation", model="distilgpt-2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        response = "Please conuslt Doctor for accurate advise"
    elif "appointment" in user_input:
        response = "Would you like to schedule an appointment?"
    elif "medication" in user_input:
        response = "Its important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        st.write("User: ",user_input)
        response=healthcare_chatbot(user_input)
        st.write("Healthcare Assistant: ",response)
    else:
        st.write("Please enter a message to get a response.")

main()
