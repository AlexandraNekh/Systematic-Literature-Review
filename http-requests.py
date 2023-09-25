import os
import urllib.parse

start_chrome = False
start_edge = True

############################################### INPUT
years = ['2000', '2024']
search_terms = [
    # 'Data Transparency', 'Data Fairness', 'Explainable Data', 'Data Accountability', 
    # [ 'HCI', 'Human Computer Interaction', 'Agile software development', 'Project management'], # AND
    [ 
        '"Collaborative design"',
        '"Participatory design"',  
        '"Stakeholder engagement"', 
        '"Stakeholder involvement"', 
        '"Stakeholder management"',
    ], # AND
    [ 
        '" AI "',
        '"AIOps"',
        '"Artificial Intelligence"', 
        '"DevOps"', 
        '"Explainable AI"',
        '"LLMOPs"',
        '"Machine Learning"', 
        '" ML "',
        '"MLOps"',
    ]
]

############################################### IEEE

ieee_url = '"https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&queryText=(('

add_term = ''
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '%20AND%20'
    add_term += '('
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '%20OR%20'
        #add_term += '%22All%20Metadata%22:' + urllib.parse.quote(or_term)
        add_term += '%22Full%20Text%20.AND.%20Metadata%22:' + urllib.parse.quote(or_term)


    add_term += ')'
    ieee_url += add_term
    add_term = ''

ieee_url += '))&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=' + years[0] + '_' + years[
    1] + '_Year&' \
         'refinements=ContentType:Conferences&refinements=ContentType:Journals&refinements=ContentType:Standards"'

print("IEEE url: " + ieee_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + ieee_url)
if start_edge: os.system('start msedge ' + ieee_url)

############################################### ACM DL
# TODO: check if the search terms could be 'better' :D
acm_dl_url = '"https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1='

add_term = ''
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '+OR+'
        #add_term += urllib.parse.quote(or_term.replace(' ', '+'))
        add_term += urllib.parse.quote(or_term)

    add_term += '%29'
    acm_dl_url += add_term
    add_term = ''

acm_dl_url += '&AfterMonth=1&AfterYear=' + years[0] + '&BeforeMonth=12&BeforeYear=' + years[1] + '"'

print("ACM DL url: " + acm_dl_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + acm_dl_url)
if start_edge: os.system('start msedge ' + acm_dl_url)

############################################### SPRINGER
# https://link.springer.com/search?new-search=true&query=%28%22Collaborative%2Bdesign%22+OR+%22Participatory%2Bdesign%22+OR+%22Stakeholder%2Bengagement%22+OR+%22Stakeholder%2Binvolvement%22+OR+%22Stakeholder%2Bmanagement%22%29+AND+%28%22AI%22+OR+%22AIOps%22+OR+%22Artificial%2BIntelligence%22+OR+%22DevOps%22+OR+%22Explainable%2BAI%22+OR+%22LLMOPs%22+OR+%22Machine%2BLearning%22+OR+%22ML%22+OR+%22MLOps%22%29&sortBy=relevance&content-type=ConferencePaper&content-type=Article&date=custom&dateFrom=2000&dateTo=2023&facet-discipline=%22Computer+Science%22
# TODO: update this to have less results again :D
# use showAll=false to hide papers that we do not have access to

springer_url = '"https://link.springer.com/search?date-facet-mode=between&facet-start-year=' + years[
    0] + '&facet-end-year=' + years[1] + '&query='

add_term = ''
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '+OR+'
        add_term += urllib.parse.quote(or_term)

    add_term += '%29'
    springer_url += add_term
    add_term = ''

springer_url += '&showAll=true"'

print("Springer url: " + springer_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + springer_url)
if start_edge: os.system('start msedge ' + springer_url)

############################################### SCOPUS

print("SCOPUS needs VPN!!!")
print("\n"*2)

scopus_url = '"https://www.scopus.com/results/results.uri?sort=plf-f&src=s&s='

add_term = '%28'
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '+OR+'
        add_term += 'TITLE-ABS-KEY%28%22' + or_term.replace('"', '') + '%22%29'

    add_term += '%29'
    scopus_url += add_term
    add_term = ''

scopus_url += '%29+AND+PUBYEAR+%26gt%3B+' + years[0] + '+AND+PUBYEAR+%26lt%3B+' + str(
    int(years[1]) + 1) + '&origin=searchadvanced"'

print("Scopus url: " + scopus_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + scopus_url)
if start_edge: os.system('start msedge ' + scopus_url)

############################################### WILEY
x = ''' # no access to wiley?
wiley_url = '"https://onlinelibrary.wiley.com/action/doSearch?field1=AllField&text1='

add_term = '%28'
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '+OR+'
        add_term += urllib.parse.quote(or_term)

    add_term += '%29'
    wiley_url += add_term
    add_term = ''

wiley_url += '%29&field2=AllField&text2=&field3=AllField&text3=&Ppub=&AfterMonth=1&AfterYear=' + years[
    0] + '&BeforeMonth=12&BeforeYear=' + years[1] + '"'

print("Wiley url: " + wiley_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + wiley_url)
if start_edge: os.system('start msedge ' + wiley_url)
'''

############################################### IET DL

iet_url = '"https://digital-library.theiet.org/search?value1='

add_term = ''
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '+OR+'
        add_term += urllib.parse.quote(or_term)

    add_term += '%29'
    iet_url += add_term
    add_term = ''

iet_url += '&fulltextcheck=option1checked&option1=all&operator3=AND&value3=&option3=author&operator2=AND&value2' \
           '=&option2=title&operator4=AND&value4=&option4=issnisbndoi&operator5=NOT&value5=&option5=all&operator7=' \
           'AND&option7=subjectarea&value7=&operator6=AND&option6=contentType&value6=&maxyear=' + years[1] + \
           '&operator9=AND&option9=year_from&value9=' + years[0] + '&operator10=AND&option10=year_to&value10=' + \
           years[1] + '&sortField=default&sortDescending=true&pageSize=10"'

print("IET DL url: " + iet_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + iet_url)
if start_edge: os.system('start msedge ' + iet_url)

############################################### DBPL

dblp_url = '"https://dblp.org/search?q='

add_term = ''
for i, and_term in enumerate(search_terms):
    if i != 0:
        add_term += '+%20'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j != 0:
            add_term += '%7C'
        add_term += '%28'
        add_term += or_term.replace('"', '')
        add_term += '%29'

    add_term += '%29'
    dblp_url += add_term
    add_term = ''

dblp_url += '"'

print("DBLP url: " + dblp_url)
print("\n"*2)
if start_chrome: os.system('start chrome ' + dblp_url)
if start_edge: os.system('start msedge ' + dblp_url)
