import os
import json
import csv
from csv import DictWriter


path_to_json = '/Users/sarahberlin/Desktop/PYTHON/JSONS/Localities'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
#print json_files


def make_csv(dictionaryList):
    fieldnames = ['ElectionName', 'LocalityName', 'LocalityCode', 'RaceName', 'NumberOfSeats', 'BallotName', 'Percentage', 'Votes', 'PoliticalParty']
    testing_json_csv = open('{0}.csv'.format(locality),'wb')
    csvwriter = csv.DictWriter(testing_json_csv, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
    for row in dictList:
        csvwriter.writerow(row)
    testing_json_csv.close()
    with open('{0}.csv'.format(locality), "r") as testing_json_csv:
            testing_json = testing_json_csv.read()
    #print testing_json


for js in json_files:
    dictList = []
    with open(os.path.join(path_to_json, js)) as json_file:
        read_file = json.loads(json_file.read())
        races_list = read_file['Races']
        for x in range(0, len(races_list)):
            for y in range (0, (len(races_list[x]['Candidates']))):
                newDict = {}
                newDict['BallotName'] = races_list[x]['Candidates'][y]['BallotName']
                newDict['Votes'] = races_list[x]['Candidates'][y]['Votes']
                newDict['Percentage'] = races_list[x]['Candidates'][y]['Percentage']
                newDict['PoliticalParty'] = races_list[x]['Candidates'][y]['PoliticalParty']
                newDict['RaceName'] = races_list[x]['RaceName']
                newDict['NumberOfSeats'] = races_list[x]['NumberOfSeats']
                newDict['LocalityName'] = read_file['Locality']['LocalityName']
                newDict['LocalityCode'] = read_file['Locality']['LocalityCode']
                newDict['ElectionName'] =  read_file['ElectionName']
                dictList.append(newDict)
    locality = dictList[0]['LocalityName'].replace(' ', '_')
    #print dictList
    print locality + " converting to CSV"
    make_csv(dictList)



