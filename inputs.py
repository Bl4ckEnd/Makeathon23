import streamlit as st
import openai


# create input fields for every language
# english
def english_inputs(audio: bool = False):
    st.title("Reporting Tool")
    st.write("This tool automates the process of creating reports for clients.")
    st.subheader("Data Input")
    st.write("Please document your work:")
    name = st.text_input("Name")
    date = st.date_input("Date of Report")
    location = st.text_input("Location")
    equipment = st.text_input("Equipment")
    task = st.text_input("Task")
    if audio:
        process = st.file_uploader("Upload Audio File", type=['wav', 'mp3'])
    else:
        process = st.text_area("Process (please describe every day individually)")
    return {"name": name, "date": date, "location": location, "equipment": equipment, "task": task, "process": process}

# spanish
def spanish_inputs(audio: bool = False):
    st.title("Herramienta de reporte")
    st.write("Esta herramienta automatiza el proceso de crear reportes para clientes.")
    st.subheader("Entrada de datos")
    st.write("Por favor documente su trabajo:")
    name = st.text_input("Nombre")
    date = st.date_input("Fecha de reporte")
    location = st.text_input("Ubicación")
    equipment = st.text_input("Equipo")
    task = st.text_input("Tarea")
    if audio:
        process = st.file_uploader("Subir archivo de audio", type=['wav', 'mp3'])
    else:
        process = st.text_area("Proceso (por favor describa cada día individualmente)")
    return {"name": name, "date": date, "location": location, "equipment": equipment, "task": task, "process": process}

# german
def german_inputs(audio: bool = False):
    st.title("Berichterstellungstool")
    st.write("Dieses Tool automatisiert den Prozess der Erstellung von Berichten für Kunden.")
    st.subheader("Dateneingabe")
    st.write("Bitte dokumentieren Sie Ihre Arbeit:")
    name = st.text_input("Name")
    date = st.date_input("Datum des Berichts")
    location = st.text_input("Ort")
    equipment = st.text_input("Ausrüstung")
    task = st.text_input("Aufgabe")
    if audio:
        process = st.file_uploader("Audio-Datei hochladen", type=['wav', 'mp3'])
    else:
        process = st.text_area("Prozess (Bitte beschreiben Sie jeden Tag einzeln)")
    return {"name": name, "date": date, "location": location, "equipment": equipment, "task": task, "process": process}