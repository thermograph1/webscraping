# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:20:11 2021

@author: SHI
"""

import requests
from bs4 import BeautifulSoup

url = 'https://terraria.fandom.com/wiki/Attack_speed'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'lxml')

# We'll use a list to store our accessory list.
accessories = []

ac_tables = html_soup.find_all('table',
                            class_='terraria sortable')

# Extract a table about attack speed.
for table in ac_tables:
    headers =[]
    rows = table.find_all('tr')
    # Start by fetching the header cells from the first row to determine
    # the field names.
    for header in table.find('tr').find_all('th'):
        headers.append(header.text.strip())
    # Then go through all the rows except the first one.
    for row in rows[1:]:
        values = []
        # And get the column cells, the first one being inside a td-tag.
        for col in row.find_all('td'):
            values.append(col.text.strip())
        if values:
            accessory_dict = {headers[i]: values[i] for i in
                             range(len(values))}
            accessories.append(accessory_dict)
            
# Show the results.
for accessory in accessories:
    print(accessory)
