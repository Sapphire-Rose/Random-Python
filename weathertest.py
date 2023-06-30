# importing the requests library
import requests
#importing json
import json
#import regex
import re
#import exceptions
import time
#import sleep
from requests.exceptions import HTTPError

#variables
api_key = 'f4adc0ec01b0b796ad01f0b14b995da9'
api_url = 'https://api.openweathermap.org/'

#main function
def main():
    print('\nWeatherBot v1.0 is here to assist you.')
    while True:
        zipcity = gatherlocation()
        itiszip = isitzip(zipcity)
        weather_response = api_post(itiszip, zipcity)
        if weather_response[1]:
            continue
        data_ext(weather_response[0], zipcity)
        tryagain = input("\nWould you like to hack the satellites again Y/N? ")
        if tryagain.upper() != "Y":
            break
    #provide error response from site if given

#Gather user info
def gatherlocation():
    zipcity = input("Please input a city name or zipcode: ")
    return zipcity.title()

#check zipcode
def isitzip(zipcity):
    matched = re.match("^[0-9][0-9][0-9][0-9][0-9]", zipcity)
    is_match = bool(matched)
    return is_match

#return data based on zipcode or city
def api_post(itiszip, zipcity):
    errors = False
    if(itiszip):
        url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zipcity + "&appid=" + api_key + "&units=imperial"
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + zipcity + "&appid=" + api_key + "&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("")
        print("Hacking global weather satellites...")
        time.sleep(2)
        print("Connection successful. Readying display...")
        time.sleep(2)
        print("Displaying now...")
        time.sleep(2)
    except HTTPError as http_err:
        errors = True
        print("\nYour connection was not successful or you have tried an invalid input. Please try again.")
        #print(f'Error: {http_err}' + "\n")
    except Exception as err:
        errors = True
        print("\nYour connection was not successful you have tried an invalid input. Please try again.")
        #print(f'Error: {err}' + "\n")
    return [response, errors]

#json data extraction - you will be assimilated
def data_ext(weather_response, zipcity):
    jsonResponse = weather_response.json()
    temp_is = jsonResponse["main"]["temp"]
    #print("")
    #print("Hacking global weather satellites...")
    #time.sleep(2)
    #print("Connection successful. Readying display...")
    #time.sleep(2)
    #print("Displaying now...")
    #time.sleep(2)
    #your connection was successful/not successful
    print("")
    print(zipcity)
    print("Temperature: " + str(temp_is) + " degrees")
    print("Humidity: " + str(jsonResponse["main"]["humidity"]) + "%")
    print("Skies: " + jsonResponse["weather"][0]["description"].title())
    print("Windspeed: " + str(jsonResponse["wind"]["speed"]) + " mph")
    print("\nThank you for using WeatherBot v1.0. Have a wonderful day.")

#program
main()
