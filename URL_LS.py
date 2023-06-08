# creates csv which includes all file_id, Solar Longitude, Mars Year, and Region # of images where trough
# clouds have been recorded

# works with Windows 10/11, doesn't work with Linux Ubuntu 22.04.2 LTS because of latest security update,
# breaks Beautiful Soup library (as of June 2023)


from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
import requests
from os.path import exists
import csv

name = []
Ls = []
MY = []
region = []
save_to = 'final.csv'

df = pd.read_csv('all_trough-and-region_SPLD.csv', usecols=['file_id', 'region'])
for each in df.iterrows():
    u = each[1][0]
    r = each[1][1]
    url = 'https://viewer.mars.asu.edu/viewer/themis/' + u + '#P=' + u + '&T=2'
    # print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    my = soup.select_one('[data-field="Mars Year"]').parent.nextSibling.get_text()
    date = soup.select_one('[data-field="Solar Longitude"]').parent.nextSibling.get_text()[0:-2]
    # print(u, date, my, r)
    file_exists = exists('all_trough-and-region_SPLD.csv')
    name.append(u)
    Ls.append(date)
    MY.append(my)
    region.append(r)

Data = {'file_id': name, 'Ls': Ls, 'Mars Year': MY, 'region': region}
df = pd.DataFrame(Data, columns=['file_id', 'Ls', 'Mars Year', 'region'])
df.to_csv(save_to, index=False)
