import requests
import json
import sys

def cohs(param):
    LIM_DIGITS = 5
    #Allgemeine Gemeinde Schlüssel
    ags_heinsberg = '05370' 
    ags_aachen = '05334'

    # Get Deutschland
    deutschland = requests.get('https://api.corona-zahlen.org/germany')
    deutschland_data = deutschland.json()
    deutschland_date = formatDate(deutschland_data['meta']['lastCheckedForUpdate'])

    # Get NRW
    nrw = requests.get('https://api.corona-zahlen.org/states/NW')
    nrw_data = nrw.json()
    nrw_date = formatDate(nrw_data['meta']['lastCheckedForUpdate'])

    # Get Aachen
    aachen = requests.get('https://api.corona-zahlen.org/districts/' + ags_aachen)
    aachen_data = aachen.json()
    aachen_date = formatDate(aachen_data['meta']['lastCheckedForUpdate'])

    # Get Heinsberg
    heinsberg = requests.get('https://api.corona-zahlen.org/districts/'+ ags_heinsberg)
    heinsberg_data = heinsberg.json()
    heinsberg_date = formatDate(heinsberg_data['meta']['lastCheckedForUpdate'])

    if param == 'd' or param == '0':
        # Print Deutschland
        print('Deutschland:')
        print(str(deutschland_data['weekIncidence']) [:LIM_DIGITS])
        print('Last check: ' + deutschland_date + '\n')

    if param == 'n' or param == '0':
        # Print NRW
        print(nrw_data['data']['NW']['name'] + ':')
        print(str(nrw_data['data']['NW']['weekIncidence']) [:LIM_DIGITS]) 
        print('Last check: ' + nrw_date + '\n')

    if param == 'a' or param == '0':
        # Print Aachen
        print(aachen_data['data'][ags_aachen]['name'] + ':')
        print(str(aachen_data['data'][ags_aachen]['weekIncidence']) [:LIM_DIGITS])
        print('Last check: ' + aachen_date + '\n')  

    if param == 'h' or param == '0':
        # Print Heinsberg
        print(heinsberg_data['data'][ags_heinsberg]['name'] + ':')
        print(str(heinsberg_data['data'][ags_heinsberg]['weekIncidence']) [:LIM_DIGITS])
        print('Last check: ' + heinsberg_date + '\n') 

    incidence_history(ags_aachen, ags_heinsberg)


def incidence_history(ags1, ags2):
    link1 = 'https://api.corona-zahlen.org/districts/' + ags1 + '/history/incidence/7'
    link2 = 'https://api.corona-zahlen.org/districts/' + ags2 + '/history/incidence/7'
    history1 = requests.get(link1)
    history2 = requests.get(link2)
    history_data1 = history1.json()
    history_data2 = history2.json()

    values1 = []
    values2 = []

    file = open('./values.dat', 'w')

    for i in history_data1['data'][ags1]['history']:
       values1.append(str(i['date'][:10]) + ' ' + str(i['weekIncidence']) + ' ')

    for i in history_data2['data'][ags2]['history']:
        values2.append(str(i['weekIncidence']))

    for i in range (0,7):
        file.write(str(values1[i]) + str(values2[i]) + '\n')

    file.close()    


def formatDate(date):
    year = date[0:10]
    time = date[12:16]
    newDate = year + ' ' + time
    return newDate


if __name__=="__main__":
    try:
        param = sys.argv[1]
    except IndexError:
        param = '0'

    cohs(param)
