'''
Created on Apr 8, 2018

@author: SHADI MERHEJ
'''

import requests
import json
import csv


def main():
    global itWorked
    itWorked = False
    site = """http://www.nhl.com/stats/rest/goalies?isAggregate=false&reportType=goalie_basic&isGame=true&reportName=goaliesummary&sort=[{%22property%22:%22gameDate%22,%22direction%22:%22DESC%22}]&cayenneExp=gameDate%3E=%222017-10-04%22%20and%20gameDate%3C=%222018-04-08%22%20and%20gameTypeId=2"""
    
    # Requests the site info
    blob = requests.get(site).content

    # Converts that info from a string to readable json
    json_data = json.loads(blob)['data']

    # Opens a blank CSV file
    csv_file = csv.writer(open("NHLgoaliesScraped.csv","w"))

    # Writes our header row
    csv_file.writerow(["assists",
        "gameDate",    
        "gameId",
        "gamesPlayed",    
        "gamesStarted",    
        "goals",
        "goalsAgainst",    
        "goalsAgainstAverage",    
        "losses",    
        "opponentTeamAbbrev",   
        "otLosses",    
        "penaltyMinutes",        
        "playerBirthCountry", 
        "playerBirthDate",  
        "playerBirthStateProvince",    
        "playerDraftOverallPickNo",   
        "playerDraftRoundNo",    
        "playerDraftYear",    
        "playerFirstName",   
        "playerHeight",    
        "playerId",    
        "playerInHockeyHof",    
        "playerIsActive",    
        "playerLastName",    
        "playerName",    
        "playerNationality",    
        "playerPositionCode",  
        "playerShootsCatches",    
        "playerWeight",    
        "points", 
        "savePctg",    
        "saves",
        "shotsAgainst",    
        "shutouts", 
        "teamAbbrev",    
        "ties",  
        "timeOnIce",    
        "wins"])    

    # Writes each line one by one to the csv file
    for x in json_data:
        try:
                #if x["gameId"] == "2017020001":
                    #itWorked = True 
                csv_file.writerow([x["assists"],
                x["gameDate"],    
                x["gameId"],
                x["gamesPlayed"],    
                x["gamesStarted"],    
                x["goals"],
                x["goalsAgainst"],    
                x["goalsAgainstAverage"],    
                x["losses"],    
                x["opponentTeamAbbrev"],   
                x["otLosses"],    
                x["penaltyMinutes"],        
                x["playerBirthCountry"], 
                x["playerBirthDate"],  
                x["playerBirthStateProvince"],    
                x["playerDraftOverallPickNo"],   
                x["playerDraftRoundNo"],    
                x["playerDraftYear"],    
                x["playerFirstName"],   
                x["playerHeight"],    
                x["playerId"],    
                x["playerInHockeyHof"],    
                x["playerIsActive"],    
                x["playerLastName"],    
                x["playerName"],    
                x["playerNationality"],    
                x["playerPositionCode"],  
                x["playerShootsCatches"],    
                x["playerWeight"],    
                x["points"], 
                x["savePctg"],    
                x["saves"],
                x["shotsAgainst"],    
                x["shutouts"], 
                x["teamAbbrev"],    
                x["ties"],  
                x["timeOnIce"],    
                x["wins"]])  
                print(x["gameId"])
                #print(type(x["gameId"]))
                if x["gameId"]==2017020001:
                    print("Yes")
                else:
                    print("Nope")
      
        except UnicodeEncodeError:
            print(x["playerName"], x["playerLastName"], x["playerBirthCity"] )
            continue
main()
