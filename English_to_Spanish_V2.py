# English to Spanish Voice Translation App
# Version 2

# Python program that takes in microphone audio and then
# prints it back to the user in both English and Spanish.
# And then if user desires, program will recite text in spanish

# Import necessary libraries
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Take user input for desired duration
dur = input("Desired Duration (Seconds)?")
dur = int(dur)

# Initialize recognizer
r = sr.Recognizer()

with sr.Microphone(0) as source:

    # Read audio data from default microphone
    print(f"Speak English for {str(dur)} seconds")
    audio_data = r.record(source, duration=dur)

    print("Recognizing Speech...")
    print("")

    # Convert speech to text
    text = r.recognize_google(audio_data)
    text=str(text)

    print("Voice to Text:")
    print(text)
    print("")

# Initialize the Google API translator
translator = Translator()

# Translate text to spanish
print("Text translated to Spanish:")
spanish_text = translator.translate(text, src='en',dest='es')
spansih_text = spanish_text.text
print(spanish_text.text)

# Initialize Voice Engine
engine = pyttsx3.init()

# Set voice speaking rate ~ Default = 200
engine.setProperty('rate', 120)

# Male and Female Voice IDs
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice', male_voice_id)

# Ask user if they would like program to recite text in spanish
print("")
recite = input("Recite spanish translation (Y/N)?")
recite = str(recite).upper()[0]
if recite == "Y":
    engine.say(spanish_text.text)
    engine.runAndWait()

print("code completed")
