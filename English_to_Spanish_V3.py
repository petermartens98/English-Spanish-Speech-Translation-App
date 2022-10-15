# English to Spanish Voice Translation App
# Version 3

# Python program that takes in microphone audio and then
# prints it back to the user in both English and Spanish.
# And then if user desires, program will recite text in spanish

# V3 allowed for user to either input/output english or spanish,
# also allowed user to specify voice gender and speaking rate

# Import necessary libraries
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Take user input for desired duration
dur = input("Desired Duration (Seconds)?\n")
dur = int(dur)

# Ask user for
src_lang = str(input("Desired input language (en-English, es-Spanish):\n").lower())
dst_lang = str(input("Desired output language (en-English, es-Spanish):\n").lower())

# For program output - easier for user to interpret
if src_lang == 'en':
    src_out = 'English'
elif src_lang == 'es':
    src_out = 'Spanish'

if dst_lang == 'en':
    dst_out = 'English'
elif dst_lang == 'es':
    dst_out = 'Spanish'

# Initialize recognizer
r = sr.Recognizer()

with sr.Microphone(0) as source:
    # Prompt user to speak src language
    print(f"Speak {src_out} for {str(dur)} seconds")

    # Read audio data from default microphone
    audio_data = r.record(source, duration=dur)

print(f"Recognizing {src_out} Speech...")
print("")

# Convert speech to text
text = r.recognize_google(audio_data)
text = str(text)

print(f"Voice to {src_out} Text:")
print(text)
print("")

# Initialize the Google API translator
translator = Translator()

# Translate text to spanish
print(f"{src_out} translated to {dst_out}:")
translated_text = translator.translate(text, src=src_lang, dest=dst_lang)
print(translated_text.text)

# Male and Female Voice IDs
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

print("")

# Ask user if they would like program to recite text in spanish
recite = input(f"Recite {dst_out} translation (Y/N)?\n")
recite = str(recite).upper()[0]
if recite == "Y":
    # Initialize and run Voice Engine
    engine = pyttsx3.init()
    # Allow user to specify a voice rate
    rate = int(input('Specify desired speaking rate (default = 200): \n'))
    # Set voice speaking rate ~ Default = 200
    engine.setProperty('rate', rate)
    # Set voice gender
    gender = str(input("Male(M) or Female(F) Voice?\n").upper())[0]
    if gender == 'M':
        engine.setProperty('voice', male_voice_id)
    elif gender == 'F':
        engine.setProperty('voice', female_voice_id)
    engine.say(translated_text.text)
    engine.runAndWait()

print("code completed")
