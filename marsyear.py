# snippet, don't need for workflow
# reads Mars Year from THEMIS url metadata for each image file_id in csv

from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
import requests
from os.path import exists
import csv

df = pd.read_csv('all_trough-and-region_SPLD.csv', usecols=['file_id', 'region'])
for each in df.iterrows():
    u = each[1][0]
    region = each[1][1]
    url = 'https://viewer.mars.asu.edu/viewer/themis/' + u + '#P=' + u + '&T=2'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    my = soup.select_one('[data-field="Mars Year"]').parent.nextSibling.get_text()

