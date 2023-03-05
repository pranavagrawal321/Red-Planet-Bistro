import speech_recognition as sr
import streamlit as st

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.text("Say something!")
        audio = r.listen(source)
        print("Time over, thanks!")
        try:
            text = r.recognize_google(audio)
            st.text("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry could not recognize what you said")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))