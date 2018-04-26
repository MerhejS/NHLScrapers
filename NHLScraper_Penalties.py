'''
Created on Apr 25, 2018

@author: mac
'''


import requests
import json
import csv


def main():

    site = "http://www.nhl.com/stats/rest/team?isAggregate=false&reportType=basic&isGame=true&reportName=penalties&sort=[{%22property%22:%22penaltyMinutes%22,%22direction%22:%22DESC%22}]&cayenneExp=gameDate%3E=%222017-10-04%22%20and%20gameDate%3C=%222018-04-09%22%20and%20gameTypeId=2"    
    # Requests the site info
    blob = requests.get(site).content

    # Converts that info from a string to readable json
    json_data = json.loads(blob)['data']

    # Opens a blank CSV file
    csv_file = csv.writer(open("NHLTEAMSUMMARIES_DATA.csv","w"))

    # Writes our header row
    csv_file.writerow(["gameDate",
                        "gameId", 
                        "gameLocationCode",    
                        "gamesPlayed",   
                        "losses",    
                        "opponentTeamAbbrev",  
                        "otLosses",    
                        "penalties",    
                        "penaltiesGameMisconduct",    
                        "penaltiesMajor",    
                        "penaltiesMatch",   
                        "penaltiesMinor",   
                        "penaltiesMisconduct",    
                        "penaltyMinutes",    
                        "points",    
                        "teamAbbrev",       
                        "teamId",
                        "ties",
                        "wins"])

    # Writes each line one by one to the csv file
    for x in json_data:
        csv_file.writerow([x["gameDate"],
                        x["gameId"], 
                        x["gameLocationCode"],    
                        x["gamesPlayed"],   
                        x["losses"],    
                        x["opponentTeamAbbrev"],  
                        x["otLosses"],    
                        x["penalties"],    
                        x["penaltiesGameMisconduct"],    
                        x["penaltiesMajor"],    
                        x["penaltiesMatch"],   
                        x["penaltiesMinor"],   
                        x["penaltiesMisconduct"],    
                        x["penaltyMinutes"],    
                        x["points"],    
                        x["teamAbbrev"],       
                        x["teamId"],
                        x["ties"],
                        x["wins"]
                        ])
main()
