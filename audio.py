import streamlit as st
import pyttsx3

st.set_page_config(page_title="TTS", page_icon="🗣")
st.title(":green[Text to speech]🗣")
st.write("Transform your written text into spoken words effortlessly! This intuitive app allows you to convert text to speech with just a click. Choose between a male or female voice to read your text aloud, providing a personalized audio experience. Perfect for accessibility, presentations, or simply enjoying your written content in audio form. Start listening now!")

text = st.text_area(
    label="Write text here..............",
    height=200,
    placeholder="Start typing........",  
)

voice_choice = st.radio(
    label="Choose a voice",
    options=["Male", "Female"],
    index=0
)

button = st.button("🗣 start listening")

if button:
    engine = pyttsx3.init()
    
    
    voices = engine.getProperty('voices')
    if voice_choice == "Male":
        engine.setProperty('voice', voices[0].id)  
    else:
        engine.setProperty('voice', voices[1].id)  
    
    user_input = text
    if user_input:  
        engine.say(user_input)
        engine.runAndWait()
        st.balloons()
      