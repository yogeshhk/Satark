# Satark
Script to predict Landslides

## Requirements:
* Problem Statement: Predicting susceptibility of Landslides
*	Locations.csv has list of susceptible locations. It has name, latitude, longitude and source as columns. For now, first three columns are useful
*	Program calls rainfall forecast for each location using ForecastIO free APIs
*	Location are marked on Google map using pygmaps.
*	If a threshold rainfall is crossed at a particular location, it is marked red else blue
## Dependencies:
*	Needs Python 2.7
*	ForecastIO: https://github.com/ZeevG/python-forecast.io 
*	pygmaps: https://code.google.com/archive/p/pygmaps/downloads
## How to Run:
*	Open account at ForecastIO and get the API key. 
*	Put it in environment variable FORECASTIO_APIKEY
*	Run the yhkForecastIOPlot.py
*	It creates yhkLandslides.html and opens it in a browser
## Disclaimer:
*	Author (yogeshkulkarni@yahoo.com) gives no guarantee of the results of the program. It is just a fun script. So, don’t depend on it at all.

