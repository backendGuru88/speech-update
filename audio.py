import streamlit as st
import pyttsx3

# Page configuration
st.set_page_config(page_title="TTS", page_icon="🗣")
st.title(":green[Text to speech]🗣")
st.write("Transform your written text into spoken words effortlessly! This intuitive app allows you to convert text to speech with just a click. Choose between a male or female voice to read your text aloud, providing a personalized audio experience. Perfect for accessibility, presentations, or simply enjoying your written content in audio form. Start listening now!")

# Text input
text = st.text_area(
    label="Write text here..............",
    height=200,
    placeholder="Start typing........",  
)

# Voice choice
voice_choice = st.radio(
    label="Choose a voice",
    options=["Male", "Female"],
    index=0
)

# Button to trigger TTS
button = st.button("🗣 start listening")

# Function to initialize TTS engine
def initialize_tts():
    try:
        engine = pyttsx3.init(driverName='sapi5')
        return engine
    except Exception as e:
        st.error("An error occurred while initializing the TTS engine. Please make sure the necessary system dependencies are installed.")
        return None

if button and text:
    engine = initialize_tts()
    if engine:
        try:
            voices = engine.getProperty('voices')
            if voice_choice == "Male":
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)

            engine.say(text)
            engine.runAndWait()
            st.balloons()
        except Exception as e:
            st.error(f"An error occurred while processing the text to speech: {e}")
