import streamlit as st
from inputs import english_inputs, spanish_inputs, german_inputs
from pdf_creation import create_pdf
from utils import translator, text_generator

# Create language selection dropdown
language = st.selectbox("Select a language", ["English", "Spanish", "German"])

# Create streamlit app that will run on localhost

# Data input fields: date of report, name, loation, equipment, Task, process,
# start and end date
if language == "English":
    inputs = english_inputs()

elif language == "Spanish":
    inputs = spanish_inputs()

elif language == "German":
    inputs = german_inputs()

# Create a button to submit the data
submit = st.button("Submit")

if submit:

    # translate equipment, task, and process
    inputs["equipment"] = translator(inputs["equipment"], language)
    inputs["task"] = translator(inputs["task"], language)
    inputs["process"] = translator(inputs["process"], language)

    # generate report text
    inputs["process"] = text_generator(inputs["process"])

    # Create a pdf file from the data
    create_pdf(**inputs)

    # Display a success message
    st.write("Your report has been created successfully.")

