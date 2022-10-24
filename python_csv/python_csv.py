#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:25:47 2022

@author: angelinetjandra
"""

from bs4 import BeautifulSoup
import requests

csv_wiki = requests.get("https://en.wikipedia.org/wiki/Comma-separated_values")
soup = BeautifulSoup(csv_wiki.text, 'html.parser')

ths = soup.find(id='Example')
table = ths.findNext('pre').text
table

f = open('car.csv', 'w')
f.write(table)
f.close()

import pandas as pd
pd.read_csv('car.csv')