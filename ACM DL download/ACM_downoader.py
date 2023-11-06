import os
import csv
from pathlib import Path

import pandas as pd
import requests
from pybtex.database.input import bibtex

# open a bibtex file

pathName = os.getcwd()

# if not os.path.exists("pdfs"):
#    os.makedirs("pdfs")

bibFiles = []
fileNames = os.listdir(pathName)
for fileName in fileNames:
    if ".bib" in fileName:
        bibFiles.append(fileName)
        print(fileName)

counter = 0
for i in bibFiles:
    print(str(i))
    parser = bibtex.Parser()
    bibdata = parser.parse_file(pathName + "/" + i)
    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        counter += 1
        try:
            try:
                print(
                    str(counter) + ": " + b["title"] + ":   " + b["url"] + ", PDF:   " + "https://dl.acm.org/doi/pdf/" +
                    b["doi"])
                # filename = Path("pdfs/"+b["title"]+".html")
                # url = "https://dl.acm.org/doi/pdf/"+b["doi"]
                # response = requests.get(url)
                # filename.write_bytes(response.content)
            except:
                print(str(counter) + ": " + b["title"] + ":   " + b["url"] + ", No PDF")
        except Exception as ex:
            print(str(counter) + ": " + "Error:" + str(ex))
            try:
                print(str(counter) + ": " + "No url for " + b["title"] + " (" + str(i) + ")")
            except:
                print(str(counter) + ": " + "Problem with " + " (" + str(i) + ")")
