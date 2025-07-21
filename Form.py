import streamlit as st
import pandas

# Create a form using st.form
with st.form("user_form"):
    st.title("User Information Form")

    # Pre-filled input fields
    name = st.text_input("What is your name?", value="Aathif")
    age = st.number_input("What is your age?", min_value=0, max_value=120, step=1, value=12)
    gender = st.radio("What is your gender?", ("Male", "Female", "Other"), index=0)
    st.write("What are your interests?")
    st.write('List them down below')
    Interests1 = st.text_input("Interest 1")
    Interest2 = st.text_input("Interest 2")
    Interest3 = st.text_input("Interest 3")
    st.write("What are your interests?")
    st.write('List them down below')
    Dislike1 = st.text_input("Dislike 1")
    Dislike2 = st.text_input("Dislike 2")
    Dislike3 = st.text_input("Dislike 3")

    # Submit button
    submitted = st.form_submit_button("Submit")


if submitted:
    st.success("Form submitted successfully!")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")