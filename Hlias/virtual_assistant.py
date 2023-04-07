#import wikipedia
import datetime
import pyttsx3
import requests
from pprint import pprint
import pywhatkit
import webbrowser

engine = pyttsx3.init()

#Making the voice of virtual assistant
voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[0].id)
engine.say("Hello my dear")

def talk(audio):
    #CREATING VIRTUAL ASSISTANT
    engine.say(audio)
    engine.runAndWait()


def play_song():
    song=input("Enter a song: ")
    pywhatkit.playonyt(song)

def gps():
    address = input("give me an address: ")
    url = "https://www.google.com/maps/place/" +"".join(address)
    webbrowser.open(url)

def find_weather():
    cities = input("Give me a town: ")
    API_KEY = "3704649e48a4eb5adb45952ad836da87"

    url = "https://api.openweathermap.org/data/2.5/weather?q={cities}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        wind_direction = data["wind"]["deg"]
    
        print(f"Current weather in {cities}:")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
        print(f"Wind direction: {wind_direction}°")
    else:
        print(f"Error: {response.status_code}")

def start():
    commands = {"weather": find_weather,"song": play_song,"gps" : gps }
    give_command =  input("give a command: ")
    if give_command == "weather":
        find_weather()
    elif give_command == "song":
        play_song()
    elif give_command == "gps":
        gps()
start()