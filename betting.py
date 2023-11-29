import requests

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLBettingOdds"

gameDate = input("Enter the date of the Game (YYYYMMDD): ")
homeTeam = input("Enter the home team: ")
awayTeam = input("Enter the away team: ")
homeTeam = homeTeam.upper()
awayTeam = awayTeam.upper()

gameid = gameDate + "_" + awayTeam + "@" + homeTeam

querystring = {"gameDate":gameDate}

headers = {
# Get an API Key from RapidAPI
	"X-RapidAPI-Key":
	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

jsonResponse = response.json()


choice = input("What would you like to see?\n1. Odds From A SportsBook\n2. Odds Comparison\n")

if choice == "1":
	sportsbook = input("Choose what SportsBook to view:\n1. Fanduel\n2. DraftKings\n3. MGM\n4. Bet365\n5. HardRock\n6. Unibet\n7. PointsBet\n8. BetRivers\n9. Caesars\n\nChoose the SportsBook to see the odds: ")
	if sportsbook == "1":
		fanduel = jsonResponse["body"][gameid]["fanduel"]
		for key, value in fanduel.items():
		   print(key, ":", value)
	elif sportsbook == "2":
		draftkings = jsonResponse["body"][gameid]["draftkings"]
		for key, value in draftkings.items():
			print(key, ":", value)
	elif sportsbook == "3":
		mgm = jsonResponse["body"][gameid]["betmgm"]
		for key, value in mgm.items():
			print(key, ":", value)
	elif sportsbook == "4":
		bet365 = jsonResponse["body"][gameid]["bet365"]
		for key, value in bet365.items():
			print(key, ":", value)
	elif sportsbook == "5":
		hardrock = jsonResponse["body"][gameid]["hardrock"]
		for key, value in hardrock.items():
			print(key, ":", value)
	elif sportsbook == "6":
		unibet = jsonResponse["body"][gameid]["unibet"]
		for key, value in unibet.items():
			print(key, ":", value)
	elif sportsbook == "7":
		pointsbet = jsonResponse["body"][gameid]["pointsbet"]
		for key, value in pointsbet.items():
			print(key, ":", value)
	elif sportsbook == "8":
		betrivers = jsonResponse["body"][gameid]["betrivers"]
		for key, value in betrivers.items():
			print(key, ":", value)
	elif sportsbook == "9":
		caesars_sportsbook = jsonResponse["body"][gameid]["caesars_sportsbook"]
		for key, value in caesars_sportsbook.items():
			print(key, ":", value)
	else:
		print("Please enter a valid selection.")

elif choice == "2":

	print("This will display all the odds from the various SportsBooks")


	odds_choice = input("What odds do you want to see?\n1.Moneyline\n2.Over\\Under\n3.Spreads\n")

	if odds_choice == "1":

		print("FanDuel Moneyline Odds:")
		fanduelhomeml = jsonResponse["body"][gameid]["fanduel"]["homeTeamMLOdds"]
		print(homeTeam + ": " + fanduelhomeml)
		fanduelawayml = jsonResponse["body"][gameid]["fanduel"]["awayTeamMLOdds"]
		print(awayTeam + ": " + fanduelawayml)

		print("DraftKings Moneyline Odds:")
		draftkingshomeml = jsonResponse["body"][gameid]["draftkings"]["homeTeamMLOdds"]
		print(homeTeam + ": " + draftkingshomeml)
		draftkingsawayml = jsonResponse["body"][gameid]["draftkings"]["awayTeamMLOdds"]
		print(awayTeam + ": " + draftkingsawayml)

		print("BetMGM Moneyline Odds:")
		betmgmhomeml = jsonResponse["body"][gameid]["betmgm"]["homeTeamMLOdds"]
		print(homeTeam + ": " + betmgmhomeml)
		betmgmawayml = jsonResponse["body"][gameid]["betmgm"]["awayTeamMLOdds"]
		print(awayTeam + ": " + betmgmawayml)

		print("Bet365 Moneyline Odds:")
		bet365homeml = jsonResponse["body"][gameid]["bet365"]["homeTeamMLOdds"]
		print(homeTeam + ": " + bet365homeml)
		bet365awayml = jsonResponse["body"][gameid]["bet365"]["awayTeamMLOdds"]
		print(awayTeam + ": " + bet365awayml)

		print("HardRock Moneyline Odds:")
		hardrockhomeml = jsonResponse["body"][gameid]["hardrock"]["homeTeamMLOdds"]
		print(homeTeam + ": " + hardrockhomeml)
		hardrockawayml = jsonResponse["body"][gameid]["hardrock"]["awayTeamMLOdds"]
		print(awayTeam + ": " + hardrockawayml)

		print("UniBet Moneyline Odds:")
		unibethomeml = jsonResponse["body"][gameid]["unibet"]["homeTeamMLOdds"]
		print(homeTeam + ": " + unibethomeml)
		unibetawayml = jsonResponse["body"][gameid]["unibet"]["awayTeamMLOdds"]
		print(awayTeam + ": " + unibetawayml)

		print("PointsBet Moneyline Odds:")
		pointsbethomeml = jsonResponse["body"][gameid]["pointsbet"]["homeTeamMLOdds"]
		print(homeTeam + ": " + pointsbethomeml)
		pointsbetawayml = jsonResponse["body"][gameid]["pointsbet"]["awayTeamMLOdds"]
		print(awayTeam + ": " + pointsbetawayml)

		print("BetRivers Moneyline Odds:")
		betrivershomeml = jsonResponse["body"][gameid]["betrivers"]["homeTeamMLOdds"]
		print(homeTeam + ": " + betrivershomeml)
		betriversawayml = jsonResponse["body"][gameid]["betrivers"]["awayTeamMLOdds"]
		print(awayTeam + ": " + betriversawayml)

		print("Caesars Moneyline Odds:")
		caesarshomeml = jsonResponse["body"][gameid]["caesars_sportsbook"]["homeTeamMLOdds"]
		print(homeTeam + ": " + caesarshomeml)
		caesarsawayml = jsonResponse["body"][gameid]["caesars_sportsbook"]["awayTeamMLOdds"]
		print(awayTeam + ": " + caesarsawayml)

	elif choice == "2":

		print("FanDuel Over\\Under Odds:")
		fanduelover = jsonResponse["body"][gameid]["fanduel"]["totalOver"]
		fandueloverodds = jsonResponse["body"][gameid]["fanduel"]["totalOverOdds"]
		fanduelunder = jsonResponse["body"][gameid]["fanduel"]["totalUnder"]
		fanduelunderodds = jsonResponse["body"][gameid]["fanduel"]["totalUnderOdds"]
		print("Over: " + fanduelover + " Odds: " + fandueloverodds)
		print("Under: " + fanduelunder + " Odds: " +fanduelunderodds)

		print("DraftKings Over\\Under Odds:")
		draftkingsover = jsonResponse["body"][gameid]["draftkings"]["totalOver"]
		draftkingsoverodds = jsonResponse["body"][gameid]["draftkings"]["totalOverOdds"]
		draftkingsunder = jsonResponse["body"][gameid]["draftkings"]["totalUnder"]
		draftkingsunderodds = jsonResponse["body"][gameid]["draftkings"]["totalUnderOdds"]
		print("Over: " + draftkingsover + " Odds: " + draftkingsoverodds)
		print("Under: " + draftkingsunder + " Odds: " + draftkingsunderodds)

		print("BetMGM Over\\Under Odds:")
		betmgmover = jsonResponse["body"][gameid]["betmgm"]["totalOver"]
		betmgmoverodds = jsonResponse["body"][gameid]["betmgm"]["totalOverOdds"]
		betmgmunder = jsonResponse["body"][gameid]["betmgm"]["totalUnder"]
		betmgmunderodds = jsonResponse["body"][gameid]["betmgm"]["totalUnderOdds"]
		print("Over: " + betmgmover + " Odds: " + betmgmoverodds)
		print("Under: " + betmgmunder + " Odds: " + betmgmunderodds)

		print("Bet365 Over\\Under Odds:")
		bet365over = jsonResponse["body"][gameid]["bet365"]["totalOver"]
		bet365overodds = jsonResponse["body"][gameid]["bet365"]["totalOverOdds"]
		bet365under = jsonResponse["body"][gameid]["bet365"]["totalUnder"]
		bet365underodds = jsonResponse["body"][gameid]["bet365"]["totalUnderOdds"]
		print("Over: " + bet365over + " Odds: " + bet365overodds)
		print("Under: " + bet365under + " Odds: " + bet365underodds )

		print("HardRock Over\\Under Odds:")
		hardrockover = jsonResponse["body"][gameid]["hardrock"]["totalOver"]
		hardrockoverodds = jsonResponse["body"][gameid]["hardrock"]["totalOverOdds"]
		hardrockunder = jsonResponse["body"][gameid]["hardrock"]["totalUnder"]
		hardrockunderodds = jsonResponse["body"][gameid]["hardrock"]["totalUnderOdds"]
		print("Over: " + hardrockover + " Odds: " + hardrockoverodds)
		print("Under: " + hardrockunder + " Odds: " + hardrockunderodds)

		print("UniBet Over\\Under Odds:")
		unibetover = jsonResponse["body"][gameid]["unibet"]["totalOver"]
		unibetoverodds = jsonResponse["body"][gameid]["unibet"]["totalOverOdds"]
		unibetunder = jsonResponse["body"][gameid]["unibet"]["totalUnder"]
		unibetunderodds = jsonResponse["body"][gameid]["unibet"]["totalUnderOdds"]
		print("Over: " + unibetover + " Odds: " + unibetoverodds)
		print("Under: " + unibetunder + " Odds: " + unibetunderodds)

		print("PointsBet Over\\Under Odds:")
		pointsbetover = jsonResponse["body"][gameid]["pointsbet"]["totalOver"]
		pointsbetoverodds = jsonResponse["body"][gameid]["pointsbet"]["totalOverOdds"]
		pointsbetunder = jsonResponse["body"][gameid]["pointsbet"]["totalUnder"]
		pointsbetunderodds = jsonResponse["body"][gameid]["pointsbet"]["totalUnderOdds"]
		print("Over: " + pointsbetover + " Odds: " + pointsbetoverodds)
		print("Under: " + pointsbetunder + " Odds: " + pointsbetunderodds)

		print("BetRivers Over\\Under Odds:")
		betriversover = jsonResponse["body"][gameid]["betrivers"]["totalOver"]
		betriversoverodds = jsonResponse["body"][gameid]["betrivers"]["totalOverOdds"]
		betriversunder = jsonResponse["body"][gameid]["betrivers"]["totalUnder"]
		betriversunderodds = jsonResponse["body"][gameid]["betrivers"]["totalUnderOdds"]
		print("Over: " + betriversover + " Odds: " + betriversoverodds)
		print("Under: " + betriversunder + " Odds: " + betriversunderodds)

		print("Caesars Over\\Under Odds:")
		caesarsover = jsonResponse["body"][gameid]["caesars_sportsbook"]["totalOver"]
		caesarsoverodds = jsonResponse["body"][gameid]["caesars_sportsbook"]["totalOverOdds"]
		caesarsunder = jsonResponse["body"][gameid]["caesars_sportsbook"]["totalUnder"]
		caesarsunderodds = jsonResponse["body"][gameid]["caesars_sportsbook"]["totalUnderOdds"]
		print("Over: " + caesarsover + " Odds: " + caesarsoverodds)
		print("Under: " + caesarsunder + " Odds: " + caesarsunderodds)

	elif choice == "3":

		print("FanDuel Spread Odds:")
		fanduelhomespread = jsonResponse["body"][gameid]["fanduel"]["homeTeamSpread"]
		fanduelhomespreadodds = jsonResponse["body"][gameid]["fanduel"]["homeTeamSpreadOdds"]
		fanduelawayspread = jsonResponse["body"][gameid]["fanduel"]["awayTeamSpread"]
		fanduelawayspreadodds = jsonResponse["body"][gameid]["fanduel"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + fanduelhomespread + " Odds: " + fanduelhomespreadodds)
		print(awayTeam + ": " + fanduelawayspread + " Odds: " + fanduelawayspreadodds)

		print("DraftKings Spread Odds:")
		draftkingshomespread = jsonResponse["body"][gameid]["draftkings"]["homeTeamSpread"]
		draftkingshomespreadodds = jsonResponse["body"][gameid]["draftkings"]["homeTeamSpreadOdds"]
		draftkingsawayspread = jsonResponse["body"][gameid]["draftkings"]["awayTeamSpread"]
		draftkingsawayspreadodds = jsonResponse["body"][gameid]["draftkings"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + draftkingshomespread + " Odds: " + draftkingshomespreadodds)
		print(awayTeam + ": " + draftkingsawayspread + " Odds: " + draftkingsawayspreadodds)

		print("BetMGM Spread Odds:")
		betmgmhomespread = jsonResponse["body"][gameid]["betmgm"]["homeTeamSpread"]
		betmgmhomespreadodds = jsonResponse["body"][gameid]["betmgm"]["homeTeamSpreadOdds"]
		betmgmawayspread = jsonResponse["body"][gameid]["betmgm"]["awayTeamSpread"]
		betmgmawayspreadodds = jsonResponse["body"][gameid]["betmgm"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + betmgmhomespread + " Odds: " + betmgmhomespreadodds)
		print(awayTeam + ": " + betmgmawayspread + " Odds: " + betmgmawayspreadodds)

		print("Bet365 Spread Odds:")
		bet365homespread = jsonResponse["body"][gameid]["bet365"]["homeTeamSpread"]
		bet365homespreadodds = jsonResponse["body"][gameid]["bet365"]["homeTeamSpreadOdds"]
		bet365awayspread = jsonResponse["body"][gameid]["bet365"]["awayTeamSpread"]
		bet365awayspreadodds = jsonResponse["body"][gameid]["bet365"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + bet365homespread + " Odds: " + bet365homespreadodds)
		print(awayTeam + ": " + bet365awayspread + " Odds: " + bet365awayspreadodds)

		print("HardRock Spread Odds:")
		hardrockhomespread = jsonResponse["body"][gameid]["hardrock"]["homeTeamSpread"]
		hardrockhomespreadodds = jsonResponse["body"][gameid]["hardrock"]["homeTeamSpreadOdds"]
		hardrockawayspread = jsonResponse["body"][gameid]["hardrock"]["awayTeamSpread"]
		hardrockawayspreadodds = jsonResponse["body"][gameid]["hardrock"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + hardrockhomespread + " Odds: " + hardrockhomespreadodds)
		print(awayTeam + ": " + hardrockawayspread + " Odds: " + hardrockawayspreadodds)

		print("UniBet Spread Odds:")
		unibethomespread = jsonResponse["body"][gameid]["unibet"]["homeTeamSpread"]
		unibethomespreadodds = jsonResponse["body"][gameid]["unibet"]["homeTeamSpreadOdds"]
		unibetawayspread = jsonResponse["body"][gameid]["unibet"]["awayTeamSpread"]
		unibetawayspreadodds = jsonResponse["body"][gameid]["unibet"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + unibethomespread + " Odds: " + unibethomespreadodds)
		print(awayTeam + ": " + unibetawayspread + " Odds: " + unibetawayspreadodds)

		print("PointsBet Spread Odds:")
		pointsbethomespread = jsonResponse["body"][gameid]["pointsbet"]["homeTeamSpread"]
		pointsbethomespreadodds = jsonResponse["body"][gameid]["pointsbet"]["homeTeamSpreadOdds"]
		pointsbetawayspread = jsonResponse["body"][gameid]["pointsbet"]["awayTeamSpread"]
		pointsbetawayspreadodds = jsonResponse["body"][gameid]["pointsbet"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + pointsbethomespread + " Odds: " + pointsbethomespreadodds)
		print(awayTeam + ": " + pointsbetawayspread + " Odds: " + pointsbetawayspreadodds)

		print("BetRivers Spread Odds:")
		betrivershomespread = jsonResponse["body"][gameid]["betrivers"]["homeTeamSpread"]
		betrivershomespreadodds = jsonResponse["body"][gameid]["betrivers"]["homeTeamSpreadOdds"]
		betriversawayspread = jsonResponse["body"][gameid]["betrivers"]["awayTeamSpread"]
		betriversawayspreadodds = jsonResponse["body"][gameid]["betrivers"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + betrivershomespread + " Odds: " + betrivershomespreadodds)
		print(awayTeam + ": " + betriversawayspread + " Odds: " + betriversawayspreadodds)

		print("Caesars Spread Odds:")
		caesarshomespread = jsonResponse["body"][gameid]["caesars_sportsbook"]["homeTeamSpread"]
		caesarshomespreadodds = jsonResponse["body"][gameid]["caesars_sportsbook"]["homeTeamSpreadOdds"]
		caesarsawayspread = jsonResponse["body"][gameid]["caesars_sportsbook"]["awayTeamSpread"]
		caesarsawayspreadodds = jsonResponse["body"][gameid]["caesars_sportsbook"]["awayTeamSpreadOdds"]
		print(homeTeam + ": " + caesarshomespread + " Odds: " + caesarshomespreadodds)
		print(awayTeam + ": " + caesarsawayspread + " Odds: " + caesarsawayspreadodds)
