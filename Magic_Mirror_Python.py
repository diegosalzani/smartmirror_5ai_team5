# -*- coding: utf-8 -*-
import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
import requests

startupscreen = tk.Tk()
startupscreen.title('Magic Mirror: Python Mod')
welcometext = tk.Label(startupscreen, font = ('caviar dreams',40), bg='black', fg='white')
startupscreen.configure(background='black')
startupscreen.overrideredirect(True)
welcometext.config(text='Welcome to Smart Mirror')
welcometext.pack(side=LEFT, padx= 20, pady=80) 
# Gets the requested values of the height and widht.
windowWidth = startupscreen.winfo_reqwidth()
windowHeight = startupscreen.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(startupscreen.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(startupscreen.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
startupscreen.geometry("+{}+{}".format(positionRight, positionDown))
startupscreen.update()

import time
from newsapi import NewsApiClient
import os
import urllib
import json
from datetime import datetime


decrypt = list()
global iteration
global timecount
global repull
global sleep
iteration = 0
timecount = 0
repull = 0
sleep = 0
class_url = "http://apps.marconivr.it/orario/api.php?class=5AI"
apod_dict = requests.get(class_url).json()

weather_api = "https://api.darksky.net/forecast/6a2ba186a06ba8fb057332df4772e297/45.4424784,10.98576024"
apod_dict_weather = requests.get(weather_api).json()
  
  
while True:

    def tick(time1=''):
        time2 = time.strftime("%H")
        if time2 != time1:
            time1 = time2
            clock_frame.config(text=time2)
        clock_frame.after(200, tick)

    def tickk(time3=''):
        time4 = time.strftime(":%M:%S")
        if time4 != time3:
            time3 = time4
            clock_frame2.config(text=time4)
        clock_frame2.after(200, tickk)


    #This function waits for a certain amount of 'tocks' and then initiates 'newsheader' -function
    def tock():
        global timecount
        global repull
        global sleep
        global decrypt
        newstitle.after(200, tock)
        if timecount < 20:
            timecount +=1
        else:
            timecount = 0
            newsheader()
        if repull < 200:
            repull +=1
        else:
            repull = 0
            headlines = api.get_top_headlines()
            payload = headlines
            decrypt = (payload['articles'])
            maxrange = len(decrypt)
        if sleep < 800:
            sleep+=1
        else:
            sleep = 0
            motiondetector()

    api = NewsApiClient(api_key='6d4c874d106d4e91942e31e617897de5')

    #This sequence decrypts the info feed for the script
    #headlines = api.get_top_headlines(sources='skytg24')
    headlines = api.get_top_headlines(language='it', country='it')
    #print(headlines)
    payload = headlines
    decrypt = (payload['articles'])
    maxrange = len(decrypt)

    #This function iterates over the news headlines. Iteration is the news number, 'itemlist' brings out only the title.
    def newsheader():
        global iteration
        global decrypt
        itemlist = decrypt[iteration]
        #print(itemlist['title'])
        newstitle.config(text=itemlist['title'])
        #source.config(text=itemlist['source']['name'])
        if iteration < 9:
            iteration +=1
        else:
            iteration = 0
    def spaziatore():
         class_label = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
         class_label.config(text="──────────────")
         class_label.place(x=775, y=25 + 50 + t)
        
    def class_shedule():
         ora = 1
         global t
         t = 0
         class_label = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
         class_label.config(text="Orario di oggi")
         class_label.place(x=800, y=35 + t)
         now = datetime.now()
         day = now.strftime("%w")
         spaziatore()
         for i in range(1, 42):
             if(apod_dict[i]['giorno'] == day and apod_dict[i]['prof'] != "BILEDDO ANTONINO" and apod_dict[i]['prof'] != "SALVATORINI MARCO"):
                 class_label = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
                 class_label.config(text= str(ora) + 'a    '+ apod_dict[i]['materia'])
                 ora += 1
                 class_label.pack(anchor=CENTER)
                 class_label.place(x=825, y=25 + 100 + t)
                 t += 50
                 
                 
    def date_frame():
        now = datetime.now()
        day_m = now.strftime("%B")
        day_n = now.strftime("%-d")
        year = now.strftime("%Y")
        date_frame = tk.Label(root, font = ('caviar dreams', 25), bg='black', fg='white')
        date_frame.place(x=25, y=150)
        date_frame.config(text= day_n + ' ' + day_m + ' '+ year)
    
    def weather_frame():
        weather_label = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
        weather_label.config(text= apod_dict_weather['currently']['summary'])
        weather_label.pack(anchor=CENTER)
        weather_label.place(x=25, y=550)
        #weather_label.pack(side=BOTTOM, anchor=W, fill=X)
        F = int(apod_dict_weather['currently']['temperature'])
        weather_temperature = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
        weather_temperature.config(text= str(round((F-32)/1.8,1)) + '°')
        weather_temperature.pack(anchor=CENTER)
        weather_temperature.place(x=25, y=600)
        
    def image(root):
        c = Canvas(root, width=100, height=100)
        c.pack()
        path= '1.png'
        # path= '/home/pi/Desktop/Magic-Mirror-Python-master/1.png'
        my_image = PhotoImage(master = c, file = "/home/pi/Desktop/Magic-Mirror-Python-master/1.png")
        c.create_image(0,0, image= my_image, anchor= NW)
        
       # root = Tk()
 
       # canvas = Canvas(root,  width=400, height=400)
       # canvas.pack() 
 
       # img = PhotoImage(file="osa_lightning.png")
       # canvas.create_image(10, 10, anchor=NW, image=img)
 

            


    root = tk.Tk()
    root.title('Mirror')

    masterclock = tk.Label(root)
    #masterclock.pack(anchor=NW, fill=X, padx=45)
    masterclock.configure(background='black')
    clock_frame = tk.Label(root, font = ('caviar dreams', 100), bg='black', fg='white')
    clock_frame.place(x=10, y=10)
    #clock_frame.pack(in_=masterclock, side=LEFT)
    clock_frame2 = tk.Label(root, font = ('caviar dreams', 40), bg='black', fg='white')
    #clock_frame2.pack(in_=masterclock, side=LEFT, anchor = N, ipady=15)
    clock_frame2.place(x=180, y=25)
    date_frame()
    newstitle = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
    newstitle.pack(side=BOTTOM, anchor=W, fill=X)
    source = tk.Label(root, font = ('caviar dreams', 10), bg='black', fg='white')
    source.config(text='LATEST NEWS')
    source.pack(side=BOTTOM, anchor=W, fill=X)
    
    class_shedule()
    weather_frame()
    image(root)
    
    newsheader()
    tick()
    tickk()
    tock()

    root.attributes("-fullscreen", True)
    root.configure(background='black')
    startupscreen.destroy()
    root.mainloop()
