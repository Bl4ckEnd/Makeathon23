import streamlit as st
from inputs import english_inputs, spanish_inputs, german_inputs
from utils import translator, text_generator
from latex_file import create_latex_pdf
import yaml
import openai

# read api key from keys.yaml
with open("keys.yaml", "r") as f:
    keys = yaml.load(f, Loader=yaml.FullLoader)
    openai.api_key = keys["key"]

# Create language selection dropdown
language = st.selectbox("Select a language", ["English", "Spanish", "German"])

# Create streamlit app that will run on localhost

# Data input fields: date of report, name, loation, equipment, Task, process,
# start and end date

# ask if there is an audio file


if language == "English":
    include_audio = st.checkbox("Do you have an audio file?")
    if include_audio:
        inputs = english_inputs(audio=True)
    else:
        inputs = english_inputs()

elif language == "Spanish":
    include_audio = st.checkbox("¿Tiene un archivo de audio?")
    if include_audio:
        inputs = spanish_inputs(audio=True)
    else:
        inputs = spanish_inputs()

elif language == "German":
    include_audio = st.checkbox("Haben Sie eine Audiodatei?")
    if include_audio:
        inputs = german_inputs(audio=True)
    else:
        inputs = german_inputs()

# Create a button to submit the data
submit = st.button("Submit")

if submit:

    if include_audio:
        # transcript audio
        inputs["process"] = openai.Audio.transcribe("whisper-1", inputs["process"], api_key=openai.api_key)['text']

    # translate equipment, task, and process
    inputs["equipment"] = translator(inputs["equipment"], language)
    inputs["task"] = translator(inputs["task"], language)
    inputs["process"] = translator(inputs["process"], language)

    # generate report text
    inputs["process"] = text_generator(inputs["process"])
    # TODO: add validation step

    # Create a pdf file from the data
    create_latex_pdf(**inputs)
    report_created = True
    # Display a success message
    if report_created:
        if language == "English":
            st.write("Your report has been created successfully.")
            with open("documents/report.pdf", "rb") as f:
                st.download_button("Download Report", f, file_name="Report.pdf")
        elif language == "Spanish":
            st.write("Su informe se ha creado correctamente.")
            with open("documents/report.pdf", "rb") as f:
                st.download_button("Descargar informe", f, file_name="Informe.pdf")
        elif language == "German":
            st.write("Ihr Bericht wurde erfolgreich erstellt.")
            with open("documents/report.pdf", "rb") as f:
                st.download_button("Bericht herunterladen", f, file_name="Bericht.pdf")
