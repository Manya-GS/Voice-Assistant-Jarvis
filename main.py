import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')

# Get available voices and set the voice to the first one
voices = engine.getProperty('voices')
# print(voices[0].id)  # Print the ID of the selected voice
engine.setProperty('voice', voices[0].id)  # Set the voice

# Define the speak function
def speak(audio):
    engine.say(audio)  # Pass the text to be spoken
    engine.runAndWait()  # Wait for the speech to be completed

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Hello Good Afternoon!")
    else:
        speak("Good to see you!")
    speak("I am Jarvis, please tell me how may I help you.")

def takeCommand():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube...")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google...")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stack Overflow...")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'exit' in query or 'stop' in query:
            speak("Have a nice day!")
            break  # Exit the loop
        else:
            print("Please say the command again.")
