# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 23:30:30 2021

@author: SHI
"""

import requests
from bs4 import BeautifulSoup

url = 'https://dontstarve.fandom.com/wiki/Don%27t_Starve_Wiki'

r = requests.get(url)
html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'lxml')
# Find the first h1 tag
first_h1 = html_soup.find('h1')