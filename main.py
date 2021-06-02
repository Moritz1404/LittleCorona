import requests
import json
import sys

def cohs(param):
    LIM_DIGITS = 5
    ags = '05370'


    # Get Deutschland
    deutschland = requests.get('https://api.corona-zahlen.org/germany')
    deutschland_data = deutschland.json()

    # Get NRW
    nrw = requests.get('https://api.corona-zahlen.org/states/NW')
    nrw_data = nrw.json()

    # Get Heinsberg
    heinsberg = requests.get('https://api.corona-zahlen.org/districts/05370')
    heinsberg_data = heinsberg.json()

    if param == 'd' or param == '0':
        # Print Deutschland
        print('Deutschland:')
        print(str(deutschland_data['weekIncidence']) [:LIM_DIGITS] + '\n')

    if param == 'n' or param == '0':
        # Print NRW
        print(nrw_data['data']['NW']['name'] + ':')
        print(str(nrw_data['data']['NW']['weekIncidence']) [:LIM_DIGITS] + '\n') 

    if param == 'h' or param == '0':
        # Print Heinsberg
        print(heinsberg_data['data'][ags]['name'] + ':')
        print(str(heinsberg_data['data'][ags]['weekIncidence']) [:LIM_DIGITS] + '\n') 


if __name__=="__main__":
    try:
        param = sys.argv[1]
    except IndexError:
        param = '0'

    cohs(param)