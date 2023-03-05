import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()

    # Set the rate and volume
    engine.setProperty('rate', 150)  # 150 words per minute
    engine.setProperty('volume', 0.7)  # 70% volume

    engine.say(text)

    # Run the Text-to-Speech engine
    engine.runAndWait()