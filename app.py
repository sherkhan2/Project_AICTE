import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initialize the text-generation pipeline
chatbot = pipeline("text-generation", model="distilgpt-2")

def healthcare_chatbot(user_input):
    # Tokenize and remove stopwords (if needed)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(user_input)
    filtered_input = ' '.join([word for word in word_tokens if word.lower() not in stop_words])
    
    # Respond based on keywords
    if "symptom" in filtered_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in filtered_input:
        return "Would you like to schedule an appointment?"
    elif "medication" in filtered_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(filtered_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    st.write("Welcome! I am here to assist you with your healthcare needs.")
    user_input = st.text_input("How can I assist you today?")
    
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a message to get a response.")

main()
