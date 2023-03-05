import streamlit as st
import pandas as pd
import numpy as np
import speech_to_text
from PIL import Image
import parsingorder
import webbrowser

st.title("🍴 Food Menu")
st.subheader("Check out our delicious food offerings!")

# Create a list of menu items
menu = [
    "Samosa Space",
    "Marsala Snacks",
    "Spice Station Chicken",
    "Chaat Corner Mars",
    "Cosmic Canapes",
    "Mars Morning Masala",
    "Spice Sunrise",
    "Red Planet Breakfast",
    "Cosmic Coffee",
    "Naan Nebula Breakfast",
    "Mars Mealtime",
    "Spice Shuttle Lunch",
    "Tandoori Trailblazers",
    "Naan Gravity Lunch",
    "Martian Midday",
    "Mars Meal Magic",
    "Red Planet Supper",
    "Tandoori Twilight",
    "Red Planet Supper",
    "Cosmic Cuisine by Night",
    "Red Planet Refreshers",
    "Tandoori Tea Time",
    "Martian Margarita",
    "Cosmic Coffee",
    "Interstellar Iced Tea"
]
# Display the menu as a DataFrame
rows = np.arange(1, len(menu) + 1)
st.table(pd.DataFrame(menu, columns=["Menu"], index=rows))

# Display the image and add a button-like behavior to it
if st.button("🎤", key="my_button"):
    a = speech_to_text.speech_to_text()
    b = parsingorder.detect_intent([a])
    # st.text(b)
    # print(" ".split(a)[:-1])

if st.button("Continue to payment"):
    webbrowser.open_new_tab("https://ptprashanttripathi.github.io/linkpe/?pa=9412605635@paytm&pn=Pranav&cu=INR&am=100")


# streamlit run c:/Users/ACER/OneDrive/Desktop/abc/main.py
