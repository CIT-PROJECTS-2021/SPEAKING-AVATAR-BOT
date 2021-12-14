'''
microphone_input
text2speech
greets
tell_me_date
'''
import random
import speech_recognition as sr
from gtts import gTTS
import datetime
import os
import warnings
import calendar
import wikipedia
import tkinter as Tk
window=Tk.Tk()
#from tkinter import Text


warnings.filterwarnings('ignore')#program must ignore any warnings that may arise when running
#activate microphone

def record_input_audio():
    #function for recording audio
    r = sr.Recognizer()#establishing recorgiser object
    #initialize microphone recording
    with sr.Microphone() as source:
        audio = r.listen(source)
        #use google speechrecogniser
    data = ''
    try:
        data = r.recognize_google(audio)
        label5=Tk.Label(window,text='you said:\n'+data,font='20').pack()
    except sr.UnknownValueError: #check for unknown errors
        label5=Tk.Label(window,text='\ngoogle cannot understand your audio').pack(padx=5,pady=10)
    except sr.RequestError as e:
        label5=Tk.Label(window,text='requst results from google service error'+str(e)).pack(padx=5,pady=10)

    return data
    #a function to get response from program
def sysresponse(Text):
    #convert text to audio
    myaudio = gTTS(text=Text, lang = 'en', slow=False)
    myaudio.save('sys_response.mp3')
    os.system('start sys_response.mp3')
def letstalk_word(Text):#a function to to wake the program so that it speaks
    syswakeword = ['hey','what'] #a list of words that wakes up the program
    Text = Text.lower() #converting text to lower case
    for phrase in syswakeword:
        if phrase in Text:
            return True
    return False#if letstalk_word not found in said sentence
def telldate():
    now=datetime.datetime.now()
    daytoday=datetime.datetime.today()
    weekday=calendar.day_name[daytoday.weekday()] # to get day of the week
    currentmonth=now.month
    daynow=now.day
    monthnames=['january','february','march','april','may','june','july','august',
                'september','october','november','december']
    daysofmonth=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                 '11th','12th','13th','14th','15th','16th','17th','18','19',
                 '20th','21st','22nd','23rd','24th','25th','26th','27','29th',
                 '30th','31st']
    return 'it is'+weekday+' '+daysofmonth[daynow-1]+' of '+monthnames[currentmonth-1]
def greeting(Text):#random greetings
    greeting_input = ['hey', 'hello', 'greetings']
    greeting_back = ['yes user', 'greetings']
    #if user says any greeting input word the program choses random response
    for word in Text.split():
        if word.lower() in greeting_input:
            return random.choice(greeting_back)+' ' +'I am here to reply your request'+'.'
    return " "
def search(Text):
    mysearch=Text.split()
    for i in range(0,len(mysearch)):
        if (i+3<=len(mysearch)-1) and (mysearch[i].lower()=='me') and (mysearch[i+1].lower()=='about'):
           find= mysearch[i+2]+' '+mysearch[i+3]
           wiki = wikipedia.summary(find, sentences=2)
           return wiki


def execute(input):
     while True:
        input = record_input_audio()
        response = ' '
        if (letstalk_word(input)) == True:
            response = response+greeting(input)
            if 'date' in input:
                tell_date = telldate()
                response = response+' '+tell_date
            if ('me about' in input):
                found = search(input)
                response = response+' '+found
            sysresponse(response)

window.title('SVB')
window.configure(bg='grey')
window.geometry("500x300+10+20")
label1=Tk.Label(window,text='SPEAKING AVATAR BOT',fg='white',bg='grey',font=60).pack(padx=10,pady=30)
label2=Tk.Label(window,text='click on speak out button bellow and \nspeak out on your mic for avatar to reply',bg='grey',font=50).pack(padx=5,pady=10)
button1=Tk.Button(window,text='speak out',font='20',command=lambda:record_input_audio()).pack(padx=10,pady=0)
button=Tk.Button(window,text='feedback',font='20',command=lambda:execute(Text)).pack(padx=5,pady=10)
window.mainloop()