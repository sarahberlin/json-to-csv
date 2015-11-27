import csv
from csv import DictWriter
from csv import DictReader
from collections import Counter

assembly_winners = []
other_offices_winners = []

#stores csv data as a list of dictionaries
dictList = []

#opens csv and appends each row to dictList as a dictionary
with open('VA_merged_file.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		dictList.append(row)


assembly_list = []
other_offices_list = []

for entry in dictList:
	if 'Member Senate of Virginia' in entry['RaceName'] or 'Member House of Delegates' in entry['RaceName']:
		newDict = {}
		newDict['Office.Name'] = entry['RaceName']
		newDict['Official.Name'] = entry['BallotName']
		newDict['votes'] = entry['Votes']
		newDict['Official.Party'] = entry['PoliticalParty']
		assembly_list.append(newDict)
	else:
		newDict = {}
		newDict['locality'] = entry['LocalityName'].title()
		newDict['Office.Name'] = entry['RaceName']
		newDict['Official.Name'] = entry['BallotName']
		newDict['votes'] = entry['Votes']
		newDict['Official.Party'] = entry['PoliticalParty']
		other_offices_list.append(newDict)

####IDs winners for assembly
contestList =[]
for dictionary in assembly_list:
	contestList.append(dictionary['Office.Name'])

#finds unique values
contestSet = set(contestList)

for race in contestSet:
	compareList = []
	for dictionary in assembly_list:
		if dictionary['Office.Name'] == race:
			compareList.append(dictionary)
	print race#, compareList
	votes_list = []
	for dictionary in compareList:
		votes_list.append(int(dictionary['votes']))
	print votes_list
	votes_winner_value = max(votes_list)
	print votes_winner_value
	for dictionary in compareList:
		if int(dictionary['votes']) == votes_winner_value:
			print "WINNER: ", dictionary
			assembly_winners.append(dictionary)

#####IDs winners for other offices
contestList =[]
for dictionary in other_offices_list:
	contestDict = {}
	contestDict['locality'] = dictionary['locality']
	contestDict['Office.Name'] = dictionary['Office.Name']
	contestList.append(contestDict)

#finds unique values
contestDictSet = [dict(y) for y in set(tuple(x.items()) for x in contestList)]

for dictpair in contestDictSet:
	compList = []
	for dictionary in other_offices_list:
		if dictionary['Office.Name'] == dictpair['Office.Name'] and dictionary['locality'] == dictpair['locality']:
			compList.append(dictionary)
	print compList
	votes_list = []
	for dictionary in compList:
		votes_list.append(int(dictionary['votes']))
	print votes_list
	votes_winner_value = max(votes_list)
	print votes_winner_value
	for dictionary in compList:
		if int(dictionary['votes']) == votes_winner_value:
			print "WINNER: ", dictionary
			other_offices_winners.append(dictionary)


#adds other fields to each dictionary
for dictionary in assembly_winners:
	dictionary['State'] = 'VA'
	dictionary['Office.Level'] = 'State'
	dictionary['Body_Represents_State'] = 'VA'
	if "House" in dictionary['Office.Name']:
		dictionary['Body.Name'] = 'State House of Delegates'
	else:
		dictionary['Body.Name'] = 'State Senate'

for dictionary in other_offices_winners:
	dictionary['State'] = 'VA'
	dictionary['Body_Represents_State'] = 'VA'
	if "City County" in dictionary['locality']:
		dictionary['Office.Level'] = 'County'
		dictionary['Body_Represents_County'] = dictionary['locality']
	elif "City" in dictionary['locality']:
		dictionary['Office.Level'] = "City"
		dictionary['Body_Represents_Muni'] = dictionary['locality']
	elif "County" in dictionary ['locality']:
		dictionary['Office.Level'] = 'County'
		dictionary['Body_Represents_County'] = dictionary['locality']
	if 'Board of Supervisors' in dictionary['Office.Name']:
		dictionary['Body.Name'] = dictionary['locality'] + " Board of Supervisors"
	elif "School Board" in dictionary['Office.Name']:
		dictionary['Body.Name'] = dictionary['locality'] + " School Board"


#writes new file
with open('VA_WINNERS.csv','w') as csvfile:
	fieldnames = ['State', 'Office.Level','Body.Name','Body_Represents_State', 'Body_Represents_County', 'Body_Represents_Muni','Office.Name','Official.Name', "Official.Party",'locality','votes']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for row in assembly_winners:
		writer.writerow(row)
	for row in other_offices_winners:
		writer.writerow(row)



