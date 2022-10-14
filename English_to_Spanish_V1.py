# Speech Translation App
# Version 1

# Python program that takes in microphone audio and then
# prints it back to the user in both English and Spanish.

# Import necessary libraries
import speech_recognition as sr
from googletrans import Translator
from pprint import pprint

# Initialize recognizer
r = sr.Recognizer()

with sr.Microphone() as source:

    # Read audio data from default microphone
    dur = 5 # Set duration in seconds
    print(f"Speak English for {str(dur)} seconds")
    audio_data = r.record(source, duration=dur)
    print("Recognizing Speech...")

    # Convert speech to text
    text = r.recognize_google(audio_data)
    text=str(text)
    print(text)
    print("")

# Initialize the Google API translator
translator = Translator()

# Translate text to spanish
print("Text translated to Spanish:")
spanish_text = translator.translate(text, src='en',dest='es')
print(spanish_text.text)

print("code completed")
