import streamlit as st
import nltk
from nltk.corpus import stopwards
from nltk.tokenize import word_tokenize

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        response = "Please conuslt Doctor for accurate advise"
    elif "appointment" in user_input:
        response = "Would you like to schedule an appointment?"
    elif "medication" in user_input:
        response = "Its important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = model(user_input, max_length=500, num_return_sequences=1)
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
