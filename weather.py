import requests
import json
from tkinter import *
import time
import pprint


class GetWeather:
    Far = 0

    def __init__(self, location):
        self.location = location

    def toF(self, kelvin):
        self.Far = int((kelvin * (9 / 5)) - 459.67)
        return self.Far

    def getdata(self):
        global E1
        global window
        town = E1.get()
        print("The input data is ", town)

        key = '1aeab2a0dfe6b0d9ef6a9a7fc8aedf04'
        r = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + town + "&APPID=" + key)
        fore = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast?q=" + town + ",1&APPID=" + key)

        fore_resp = fore.text
        fore_parsed = json.loads(fore_resp)
        #print(json.dumps(fore_parsed, indent=2, sort_keys=True))
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

        forecast = Label(window, text="Forecast for " + town)
        forecast.pack()
        Current_Day = time.strftime("%A")
        Day_Position = days.index(Current_Day)

        count = 0
        while count != 5:
            farenheit = fore_parsed['list'][Day_Position]['main']['temp']
            test = self.toF(farenheit)
            fart = Label(window, text=days[
                         Day_Position] + ": " + str(test) + " with " + fore_parsed['list'][Day_Position]['weather'][0]['description'])
            fart.pack()
            if Day_Position == 6:
                Day_Position = -1
            Day_Position += 1
            count += 1

        response = r.text
        parsed = json.loads(response)

        norm = parsed['main']['temp']
        faren = self.toF(norm)

        top = Label(window, text=" \n\nCurrent weather for " + town)
        top.pack()
        temp = Label(window, text="Temperature: " + str(faren))
        temp.pack()
        weath = Label(window, text="Weather: " +
                      parsed['weather'][0]['description'])
        weath.pack()


window = Tk()
window.title("Get shitty weather")

city = Label(window, text="City")
city.pack()
E1 = Entry()
E1.pack()
test = GetWeather(E1)  # instantiates the class
Button(window, text='submit', command=test.getdata).pack()


window.mainloop()
