import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification
def getNotification():
    cityName = place.get()  
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  
    apiKey = 'd850f7f52bf19300a9eb4b0aa6b80f0d' 
    try:
        url = baseUrl + "appid=" + apiKey + "&q=" + cityName
        response = requests.get(url)  
        if response.status_code == 200:
            x = response.json()  
            y = x["main"]  

            temp = y["temp"]
            temp -= 273.15 

            
            pres = y["pressure"]

            
            hum = y["humidity"]

            z = x["weather"]

            weather_desc = z[0]["description"]

            info = (
                f"Here is the weather description of {cityName}:\n"
                f"Temperature = {temp:.2f}°C\n"
                f"Atmospheric pressure = {pres} hPa\n"
                f"Humidity = {hum}%\n"
                f"Description of the weather = {weather_desc}"
            )

            notification.notify(
                title="YOUR WEATHER REPORT",
                message=info,
                timeout=10
            )
        else:
            mb.showerror('Error', 'City not found or API request failed')

    except Exception as e:
        mb.showerror('Error', str(e))  

wn = Tk()
wn.title("Weather Desktop Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

Label(wn, text="Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification).place(relx=0.4, rely=0.75)

wn.mainloop()
