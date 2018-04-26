'''
Created on Apr 17, 2018

@author: mac
'''
import csv
from StdSuites.Table_Suite import row

def createList(fileName):
    backUpList = []
    with open(fileName, 'r') as f:
        openFile = csv.reader(f)
        for row in openFile:
            print(row[0])
            data=row[0]
            backUpList.append(data)
            print(backUpList)
        return(backUpList)

def main(backUpGoalies,NHLdata):
    checkName = createList(backUpGoalies)
    data = open(NHLdata, 'r')
    output = open("NHLDataClean.csv", 'w')
    writer = csv.writer(output)
    print(checkName)
    
    for row in csv.reader(data):
        name=row[15]
        #type(name)
        for i in range(0,54):
            if checkName[i]==name:
                writer.writerow(row)      
        
main("NHLbackups.csv", "NHLgoalieData.csv")
   
        
    
    