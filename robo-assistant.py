
import pyttsx3  #pip install pyttsx3
import datetime  #module
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  #inbuilt
import pyautogui
import psutil  #pip install psutil
import pyjokes  # pip install pyjokes
import requests, json  #inbuilt
import tkinter as tk
from tkinter import *
from PIL import *
import threading
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen 
import wolframalpha



root=tk.Tk()
root.title("robo_assistant")
root.geometry("800x800")
variable=tk.StringVar()
root.iconbitmap(r"C:\\Users\\alok Sharma\\desktop\\favicon.ico")
label=tk.Label(root,text="HOW MAY I HELP YOU ?",font="Algerian",bg="teal",fg="white")

label.pack()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
img = PhotoImage(file= r"C:\\Users\\alok Sharma\\desktop\\image.gif",format="gif -index 2")
canvas.create_image(20,20, anchor=NW, image=img)
image=PhotoImage(file= r"C:\\Users\\alok Sharma\\desktop\\mic.png")
photoImage=image.zoom(5)
photoImage = image.subsample(10)
root.configure(bg='teal')


engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)




#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)
    


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    
    speak(date)
    
    speak(month)
    
    speak(year)
    


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
            label.config(text="Good morning mam")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
                label.config(text="it's Good afternoon mam")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
                label.config(text="it's Good Evening mam")
            else:
                speak("it's Goodnight sir")
                label.config(text="it's Goodnight mam")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon mam")
            label.config(text="it's Good afternoon mam")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning mam")
                label.config(text="Good morning mam")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening mam")
                label.config(text="it's Good Evening mam")
            else:
                speak("it's Goodnight sir")
                label.config(text="it's Goodnight mam")
    else:
        speak("it's night mam!")
        label.config(text="it's night mam!")


#welcome function
def wishme():
    speak("Welcome Back")
    label.config(text="Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning mam!")
        label.config(text="Good Morning mam!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon mam")
        label.config(text="Good afternoon mam")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
        label.config(text="Good Evening mam")
    else:
        speak("Goodnight mam")
        label.config(text="Goodnight mam")

    speak("Robo at your service, Please tell me how can i help you?")
    
#exit function

def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning mam")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon mam")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    root.destroy()
    quit()
    


#command by user function
def takeCommand():

    # global label
    

    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
       
        print(label)
        print("Listing...")
        label.config(text="Listing...")

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        label.config(text="Recognizing...")
        
        
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        #print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        label.config(text="Say that again please...")

        return "None"

    return query


#sending email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("riasharma0130@gmail.com", "")
    server.sendmail("arnav1406sharma@gmail.com", to, content)
    server.close()


#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "C:\\Users\\alok Sharma\\desktop\\screenshots\\ss.png"
    )


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    label.config(text='CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))
    label.config(text="battery is at:" + str(battery.percent))


#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    label.config(text=(j))
    speak(j)


#weather condition
def weather():
    api_key = "44094d88d7e2efff1e2b99e015192a1f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        label.config(text=(r))
        speak(r)
    else:
        speak(" City Not Found ")
        label.config(text=" City Not Found ")

#personal information


def personal():
    speak(
        "I am robo, version 1.0, I am an AI assistent, I am developed by Ria Sharma on 5 july 2020 in INDIA"
    )
    label.config(text="I am robo, version 1.0, I am an AI assistent, I am developed by Ria Sharma on 5 july 2020 in INDIA"
    )
    speak("Now i hope you know me")
    label.config(text="Now i hope you know me")

def thr():
    th=threading.Thread(target=wish).start()


def wish():
    wishme()
  
    while (True):
        # variable.set("listening...")
        query = takeCommand().lower()
        print(query)

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

#news
        elif ('news' in query):
            speak("okay")
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    speak(news.title.text.encode('utf-8'))
                    print(news.title.text.encode('utf-8'))
                    label.config(text=news.title.text.encode('utf-8'))
            except Exception as e:
                    print(e)

#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)





        elif "calculate" in query:  
              
            app_id = "852L55-99T4P2TH4X" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  

#sending email

        elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content = takeCommand()
                to = 'arnav1406sharma@gmail.com'
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak(
                    "Unable to send email check the address of the recipient")
        elif ("search on google" in query or "open website" in query):
            speak("What should i search or open?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")



        elif ("how are you" in query): 
            speak("I am fine, Thank you") 
            speak("How are you, mam") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif ("how old are you" in query): 
            speak("i am less than a year old,but smart enough to do all your tasks") 
            speak("what can i do for you?") 
#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

#screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

#cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#weather
        elif ("weather" in query or "temperature" in query):
            weather()

 #features
        elif ("tell me your powers" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can read you the morning news
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            label.config(text=(features))

            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("robo", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")


        elif ('i am done' in query or 'bye bye robo' in query
              or 'go offline robo' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()
        


btn=tk.Button(root,text="click me",image=photoImage,command=thr)
btn.pack()


root.mainloop()
