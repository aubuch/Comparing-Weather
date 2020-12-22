import tkinter as tk
import requests
import time

#function to call data from API and manipulate
def WeatherInfo(canvas):
    city1,city2,function = UsrtxtFld.get().split(",")
    api1 = "https://api.openweathermap.org/data/2.5/weather?q="+city1+"&appid=4890d2e80ba06aaed510b42eb9ecc258"

    api2 = "https://api.openweathermap.org/data/2.5/weather?q="+city2+"&appid=4890d2e80ba06aaed510b42eb9ecc258"
    
    #Data for city1

    jsondat1 = requests.get(api1).json()
    condtype1 = jsondat1['weather'][0]['main']
    temp1 = int(jsondat1['main']['temp'] - 273.15)
    mintemp1 = int(jsondat1['main']['temp_min'] - 273.15)
    maxtemp1 = int(jsondat1['main']['temp_max'] - 273.15)
    pressure1 = jsondat1['main']['pressure']
    humidity1 = jsondat1['main']['humidity']
    wspeed1 = jsondat1['wind']['speed']
    sunrise1 = time.strftime('%I:%M:%S', time.gmtime(jsondat1['sys']['sunrise'] - 19800))
    sunset1 = time.strftime('%I:%M:%S', time.gmtime(jsondat1['sys']['sunset'] - 19800))

    #Data for city2

    jsondat2 = requests.get(api2).json()
    condtype2 = jsondat2['weather'][0]['main']
    temp2 = int(jsondat2['main']['temp'] - 273.15)
    mintemp2 = int(jsondat2['main']['temp_min'] - 273.15)
    maxtemp2 = int(jsondat2['main']['temp_max'] - 273.15)
    pressure2 = jsondat2['main']['pressure']
    humidity2 = jsondat2['main']['humidity']
    wspeed2 = jsondat2['wind']['speed']
    sunrise2 = time.strftime('%I:%M:%S', time.gmtime(jsondat2['sys']['sunrise'] - 19800))
    sunset2 = time.strftime('%I:%M:%S', time.gmtime(jsondat2['sys']['sunset'] - 19800))

    #Comparing according to the given function

    if function=="cold" or function=="Cold" or function=="COLD":
     if temp1>temp2:
      outputinfo = "Colder place:"+city2+"\n\n"+ condtype2 + "\n" + str(temp2) + "°C" 
      outputdata = "\n"+ "Min Temp: " + str(mintemp2) + "°C" + "\n" + "Max Temp: " + str(maxtemp2) + "°C" +"\n" + "Pressure: " + str(pressure2) + "\n" +"Humidity: " + str(humidity2) + "\n" +"Wind Speed: " + str(wspeed2) + "\n" + "Sunrise: " + sunrise2 + "\n" + "Sunset: " + sunset2
      label1.config(text = outputinfo)
      label2.config(text = outputdata)
     else:
      outputinfo = "Colder place:"+city1+"\n\n"+ condtype1 + "\n" + str(temp1) + "°C" 
      outputdata = "\n"+ "Min Temp: " + str(mintemp1) + "°C" + "\n" + "Max Temp: " + str(maxtemp1) + "°C" +"\n" + "Pressure: " + str(pressure1) + "\n" +"Humidity: " + str(humidity1) + "\n" +"Wind Speed: " + str(wspeed1) + "\n" + "Sunrise: " + sunrise1 + "\n" + "Sunset: " + sunset1
      label1.config(text = outputinfo)
      label2.config(text = outputdata)
    elif function=="warm" or function=="Warm" or function=="WARM":
     if temp2>temp1:
      outputinfo = "Warmer place:"+city2+"\n\n"+ condtype2 + "\n" + str(temp2) + "°C" 
      outputdata = "\n"+ "Min Temp: " + str(mintemp2) + "°C" + "\n" + "Max Temp: " + str(maxtemp2) + "°C" +"\n" + "Pressure: " + str(pressure2) + "\n" +"Humidity: " + str(humidity2) + "\n" +"Wind Speed: " + str(wspeed2) + "\n" + "Sunrise: " + sunrise2 + "\n" + "Sunset: " + sunset2
      label1.config(text = outputinfo)
      label2.config(text = outputdata)
     else:
      outputinfo = "Warmer place:"+city1+"\n\n"+ condtype1 + "\n" + str(temp1) + "°C" 
      outputdata = "\n"+ "Min Temp: " + str(mintemp1) + "°C" + "\n" + "Max Temp: " + str(maxtemp1) + "°C" +"\n" + "Pressure: " + str(pressure1) + "\n" +"Humidity: " + str(humidity1) + "\n" +"Wind Speed: " + str(wspeed1) + "\n" + "Sunrise: " + sunrise1 + "\n" + "Sunset: " + sunset1
      label1.config(text = outputinfo)
      label2.config(text = outputdata)

#Function over

#initiating user interface
canvas= tk.Tk()
canvas.geometry("750x750")
canvas.title("Comparing Weather of 2 Places")
canvas.configure(background="cyan")

#Displaying the required format of input

label=tk.Label(canvas,text="Enter in the following format:  CITY1,CITY2,CONDITION",font=("Langar",18))
label.pack()

#Defining input box for user to enter
UsrtxtFld = tk.Entry(canvas, justify='center', width = 20, font = ("Calligrapher",30))
UsrtxtFld.pack(pady = 20)
UsrtxtFld.focus()
UsrtxtFld.bind('<Return>', WeatherInfo)

#Pre-defining space and style for output (to be attatched from the function)
label1 = tk.Label(canvas, font=("Arial Black",35,"bold"))
label1.pack()
label2 = tk.Label(canvas, font=("Lobster",15))
label2.pack()
canvas.mainloop()