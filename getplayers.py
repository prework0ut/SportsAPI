import requests
import pandas as pd
from pandas import json_normalize

# Overview: The goal of this script is to get an up to date list of NFL players and write the data out to a csv.
# This can be used to pull player ids and other information regarding the player themselves.

#Filename to write out to
filename = "playersdata.csv"

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerList"

headers = {
# Get an API Key from RapidAPI
	"X-RapidAPI-Key":
	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"

}

response = requests.get(url, headers=headers)

#Take json format of response
players = response.json()

# Normalize the body portion of the JSON Response from line 19
playersnormalize = json_normalize(players["body"])

# Write the JSON data out to a CSV file
playersnormalize.to_csv(filename, encoding='utf-8', index=False)
