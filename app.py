#!/usr/bin/python3
# good for the data output format of the data source as at 2025-02-12
#
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
import pandas

json_arr_dates = ' [ \
    "2019/09/01", \
    "2019/09/08"  \
    ] '

url_prefix_1 = "https://racing.hkjc.com/racing/information/english/Racing/DisplaySectionalTime.aspx?RaceDate="

arr_races = range(1,10) # too lazy to determine the range for each date , & too lazy to type [ 1,2, ... ,14 ]

arr_dates  = json.loads( json_arr_dates )

for i in arr_dates :
    for j in arr_races :
        i_url =  f"{url_prefix_1}{ (datetime.strptime( i, '%Y/%m/%d')).strftime('%d/%m/%Y') }&RaceNo={ str(j) }"
        print( "=====" )
        print( i_url )
        response = requests.get( i_url )
        soup = BeautifulSoup(response.text, 'html.parser')
        sz_html_table = soup.select_one('table.race_table')
        dfs=pandas.read_html( str(sz_html_table) )
        dfs[0].to_csv("output_sample/"+f"{ (datetime.strptime( i, '%Y/%m/%d')).strftime('%Y-%m-%d') }_{ str(j) }"+".csv" , mode='a', header=False )