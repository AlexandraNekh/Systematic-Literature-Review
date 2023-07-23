import os

############################################### INPUT
years = ['2000', '2023']
search_terms = [['Stakeholder involvement', 'Participatory design', 'Stakeholder engagement', 'User-centered design',
                 'HCI', 'Human Computer Interaction', 'Collaborative design', 'Explainable AI', 'Data Transparency',
                 'Data Fairness', 'Explainable Data', 'Data Accountability', 'Agile software development',
                 'Project management'],
                ['MLOps', 'DevOps', 'AIOps'],
                ['Cloud', 'Machine Learning', 'Artificial Intelligence', 'Cloud-based', 'AI-based', 'ML-based']]


############################################### IEEE

ieee_url = '"https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&queryText=(('

add_term = ''
for i, and_term in enumerate(search_terms):
    if i!=0:
        add_term += '%20AND%20'
    add_term += '('
    for j, or_term in enumerate(and_term):
        if j!=0:
            add_term += '%20OR%20'
        add_term += '%22All%20Metadata%22:' + or_term.replace(' ', '%20')

    add_term += ')'
    ieee_url += add_term
    add_term = ''

ieee_url += '))&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=' + years[0] + '_' + years[1] + '_Year&' \
            'refinements=ContentType:Conferences&refinements=ContentType:Journals&refinements=ContentType:Standards"'

print("IEEE url: " + ieee_url)
os.system('start chrome ' + ieee_url)


############################################### ACM DL

acm_dl_url = '"https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1='

add_term = ''
for i, and_term in enumerate(search_terms):
    if i!=0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j!=0:
            add_term += '+OR+'
        add_term += or_term.replace(' ', '+')

    add_term += '%29'
    acm_dl_url += add_term
    add_term = ''


acm_dl_url += '&AfterMonth=1&AfterYear=' + years[0] + '&BeforeMonth=12&BeforeYear=' + years[1] + '"'

print("ACM DL url: " + acm_dl_url)
os.system('start chrome ' + acm_dl_url)


############################################### SPRINGER

springer_url = '"https://link.springer.com/search?date-facet-mode=between&facet-start-year=' + years[0] + '&facet-end-year=' + years[1] + '&query='

add_term = ''
for i, and_term in enumerate(search_terms):
    if i!=0:
        add_term += '+AND+'
    add_term += '%28'
    for j, or_term in enumerate(and_term):
        if j!=0:
            add_term += '+OR+'
        add_term += or_term.replace(' ', '+')

    add_term += '%29'
    springer_url += add_term
    add_term = ''


springer_url += '&showAll=true"'

print("Springer url: " + springer_url)
os.system('start chrome ' + springer_url)