'''
Created on Apr 21, 2018

@author: mac
'''
'''
Created on Apr 8, 2018

@author: SHADI MERHEJ
'''

import requests
import json
import csv


def main():

    site = "http://www.nhl.com/stats/rest/team?isAggregate=false&reportType=basic&isGame=true&reportName=teamsummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22wins%22,%22direction%22:%22DESC%22}]&cayenneExp=gameDate%3E=%222017-10-04%22%20and%20gameDate%3C=%222018-04-09%22%20and%20gameTypeId=2"    
    # Requests the site info
    blob = requests.get(site).content

    # Converts that info from a string to readable json
    json_data = json.loads(blob)['data']

    # Opens a blank CSV file
    csv_file = csv.writer(open("NHLTEAMSUMMARIES_DATA.csv","w"))

    # Writes our header row
    csv_file.writerow(["faceoffWinPctg",
                        "faceoffsLost",
                        "faceoffsWon",
                        "gameDate",
                        "gameId",
                        "gameLocationCode",
                        "gamesPlayed",
                        "goalsAgainst",
                        "goalsFor",
                        "losses",
                        "opponentTeamAbbrev",
                        "otLosses",
                        "penaltyKillPctg",
                        "points",
                        "ppGoalsAgainst",
                        "ppGoalsFor",
                        "ppOpportunities",
                        "ppPctg",
                        "shNumTimes",
                        "shootoutGamesLost",
                        "shootoutGamesWon",
                        "shotsAgainst",
                        "shotsFor",
                        "teamAbbrev",
                        "teamId",
                        "ties",
                        "wins"])    

    # Writes each line one by one to the csv file
    for x in json_data:
        csv_file.writerow([x["faceoffWinPctg"],
                        x["faceoffsLost"],
                        x["faceoffsWon"],
                        x["gameDate"],
                        x["gameId"],
                        x["gameLocationCode"],
                        x["gamesPlayed"],
                        x["goalsAgainst"],
                        x["goalsFor"],
                        x["losses"],
                        x["opponentTeamAbbrev"],
                        x["otLosses"],
                        x["penaltyKillPctg"],
                        x["points"],
                        x["ppGoalsAgainst"],
                        x["ppGoalsFor"],
                        x["ppOpportunities"],
                        x["ppPctg"],
                        x["shNumTimes"],
                        x["shootoutGamesLost"],
                        x["shootoutGamesWon"],
                        x["shotsAgainst"],
                        x["shotsFor"],
                        x["teamAbbrev"],
                        x["teamId"],
                        x["ties"],
                        x["wins"]
                        ])   
              
main()
