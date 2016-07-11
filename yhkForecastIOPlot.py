from forecastiopy import *
import csv
import pygmaps
import webbrowser
import os

APIKEY = ''
if "FORECASTIO_APIKEY" in os.environ:
    APIKEY = os.environ['FORECASTIO_APIKEY']

if APIKEY == '':
    print("Need to have APIKEY to run this program. Bye!!")
    exit()

mymap = pygmaps.pygmaps(18, 73, 8) # centralized to Pune, where-else?

f = open("locations.csv",'r')
currentweather = ''
# latitudes = []
# longitudes = []
try:
    reader = csv.reader(f)
    for row in reader:
        city = row[0]
        lat = row[1]
        lon = row[2]
        mobile = row[3]
        threshold = 180 # CHANGE
        bluecolor = "#0000FF"
        redcolor = "#ff0000"

        fio = ForecastIO.ForecastIO(APIKEY,
                                units=ForecastIO.ForecastIO.UNITS_SI,
                                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                latitude=lat, longitude=lon)  # TIME
        if fio.has_currently() is True:
            currently = FIOCurrently.FIOCurrently(fio)
            currentweather += 'Temp: ' + str(currently.temperature) + ',' + 'Humidity: ' + str(currently.humidity) + ' , Rain (mm/hr):' + str(currently.precipIntensity) + '\n'
        else:
            print('No Currently data')

        if fio.has_hourly() is True:
            hourly = FIOHourly.FIOHourly(fio)
            next_3hours_rain = hourly.hour_1_precipIntensity + hourly.hour_2_precipIntensity + hourly.hour_3_precipIntensity
            currentweather += '\tRainfall (mm) in next 3 hours =[' + str(next_3hours_rain) + ']\n'

        else:
            print('No Hourly data')

        if fio.has_daily() is True:
            daily = FIODaily.FIODaily(fio)
            next_3days_rain = daily.day_1_precipIntensity * 24 + daily.day_2_precipIntensity * 24 + daily.day_3_precipIntensity * 24
            display_string = "%.1f" % next_3days_rain
            currentweather += '\tRainfall (mm) for next 3 days =[' + display_string + ']\n'
        else:
            print('No Daily data')
        color = ""
        if next_3days_rain > threshold:
            color = redcolor
        else:
            color = bluecolor

        mymap.addpoint(float(lat),float(lon), color,display_string)
finally:
    f.close()

url = 'yhkLandslides.html'
mymap.draw(url)
webbrowser.open_new(url)
