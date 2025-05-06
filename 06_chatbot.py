import streamlit as st

bot_name = "College Buddy"

knowledge_base = {
    "what is your name?": [
        f"My name is {bot_name}! \nHappy to help you out with your College enquiries!"
    ],
    "hello": [
        f"Hello my name is {bot_name}! \nHappy to help you out with your College enquiries!"
    ],
    "what are the best colleges from pune?": [
        "COEP", "PICT", "VIT", "CUMMINS", "PCCOE"
    ],
    "which are the best engineering branches?": [
        "Computer Engineering", "IT Engineering", "ENTC Engineering"
    ],
    "what are the top branch cut-offs for coep?": [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2 percentile"
    ],
    "what are the top branch cut-offs for pict?": [
        "Computer Engineering : 99.4 percentile",
        "IT Engineering : 98.6 percentile",
        "ENTC Engineering: 97.2 percentile"
    ],
    "what are the top branch cut-offs for vit?": [
        "Computer Engineering : 99.8 percentile",
        "IT Engineering: 97.1 percentile",
        "ENTC Engineering: 96.2 percentile"
    ],
    "what are the top branch cut-offs for cummins?": [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2"
    ],
    "what are the top branch cut-offs for pccoe?": [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2"
    ],
    "when do college admissions start?": [
        "Admissions generally start around August"
    ],
}

st.header("College Enquiry Rule-Based Chatbot")

user_input = st.text_input("Enter a query here-").lower()

col1, col2 = st.columns([1, 0.1])
with col1:
    ask = st.button("Ask")
with col2:
    quit = st.button("Quit")

if ask and user_input:
    if user_input in knowledge_base:
        for response in knowledge_base[user_input]:
            st.write(response)
    else:
        st.warning("Sorry, I don't know the answer to that question.")

if quit:
    st.write("Thank you for using the Chatbot.")

#python -m venv myenv
#>> myenv\Scripts\activate
#(myenv) PS C:\Users\samar\Downloads\SPPU-COMP-2019-PRACTICALS\AI> pip install streamlit pandas