import os
import csv
from pathlib import Path
import requests

pathName = os.getcwd()

csvFiles = []
fileNames = os.listdir(pathName)
for fileName in fileNames:
    if ".csv" in fileName:
        csvFiles.append(fileName)
        print(fileName)

counter = 0
for i in csvFiles:
    file = open((pathName + "/" + i), encoding="utf8")
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] != "Document Title":
            counter+=1
            try:
                print(str(counter) +": "+ row[0] + ":   " + row[15])

            except Exception as ex:
                print(ex)
                print(str(counter) +": "+ "Problem with " + str(row[0]) + " (" + str(i) + ")")

