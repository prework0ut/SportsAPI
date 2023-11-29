# SportsAPI
This repository is a personal Python project aimed at getting various sports and betting data from a RapidAPI host.

# Requirements
- Python3
- An API token generated from https://rapidapi.com/tank01/api/tank01-nfl-live-in-game-real-time-statistics-nfl

# Overview
This project is currently being built out with various features aimed at gathering data related to NFL statistics and betting odds from various sportsbooks.

Currently, the betting.py script can be used to call the API and generate a listing of various odds on a particular NFL game that the user provides. There is also the opportunity to see the comparsion different Sportsbooks 
have for the game related to moneylines, spreads, and over/unders.

# Use
Running the betting.py script, it will first ask you for the date of the game, and the home/away teams. Date must be entered in YYYYMMDD format. Teams are to be entered in by the three letter city abbreviation. 

Example:

Enter the date of the Game (YYYYMMDD): 20231127

Enter the home team: min

Enter the away team: chi

