import brewery
from brewery import ds
import sys
import csv
from csv import DictWriter
from csv import DictReader
import os


path = '/Users/sarahberlin/Desktop/PYTHON/JSONS/Localities'
os.listdir(path)

#get names of csv files so they can be merged
csv_files = []
for csv_file in os.listdir(path):
    if ".csv" in csv_file and 'merged' not in csv_file:
        csv_files.append(csv_file)

sources = []

for csv_file in csv_files:
    newDict = {}
    newDict['file'] = csv_file
    newDict['fieldnames'] = ['ElectionName', 'LocalityName', 'LocalityCode', 'RaceName', 'NumberOfSeats', 'BallotName', 'Percentage', 'Votes', 'PoliticalParty']
    sources.append(newDict)


# creates list of all fields and adds filename to store information
#all_fields = brewery.FieldList(["file"])
all_fields = []
#all_fields.append('file')
for source in sources:
    for field in source["fieldnames"]:
        if field not in all_fields:
            all_fields.append(field)


#gets each row in each csv file and puts it in a list
all_rows = []
for source in sources:
    for row in csv.DictReader(open(source['file'], 'rb')):
        all_rows.append(row)

#tries to write each of those rows to the new csv and then close the csv
fieldnames = all_fields
VA_merged_file = open('VA_merged_file.csv','wb')
csvwriter = csv.DictWriter(VA_merged_file, delimiter=',', fieldnames=fieldnames)
csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
for row in all_rows:
    csvwriter.writerow(row)

VA_merged_file.close()


