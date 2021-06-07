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
        print('Updated: ' + deutschland_date + '\n')

    if param == 'n' or param == '0':
        # Print NRW
        print(nrw_data['data']['NW']['name'] + ':')
        print(str(nrw_data['data']['NW']['weekIncidence']) [:LIM_DIGITS]) 
        print('Updated: ' + nrw_date + '\n')

    if param == 'a' or param == '0':
        # Print Heinsberg
        print(aachen_data['data'][ags_aachen]['name'] + ':')
        print(str(aachen_data['data'][ags_aachen]['weekIncidence']) [:LIM_DIGITS])
        print('Updated: ' + aachen_date + '\n') 

    if param == 'h' or param == '0':
        # Print Heinsberg
        print(heinsberg_data['data'][ags_heinsberg]['name'] + ':')
        print(str(heinsberg_data['data'][ags_heinsberg]['weekIncidence']) [:LIM_DIGITS])
        print('Updated: ' + heinsberg_date + '\n') 


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
