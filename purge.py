# purging duplicate file_id's from CSVs
    # because the regions aren't well defined when downloading THEMIS images, some duplication may occur

import pandas as pd
import csv
from csv_diff import load_csv, compare

# file_list1 = pd.read_csv("search_results.csv")
# fileName1 = file_list1['file_id']
# file_list2 = pd.read_csv("R1_fullList.csv")
# fileName2 = file_list2['file_id']
f = open('saved_R2_2-NEWTHEMIS.csv', 'w', newline='')
writer = csv.writer(f)
with open('search_results2.csv') as f1, open('R2_fullList.csv') as f2:

    diff = compare(
        load_csv(f1, key="file_id"),
        load_csv(f2, key="file_id")
    )

    list1 = len(diff['added'])
    for i in range(list1):
        x = diff['added'][i-1]
        x = str(x.values())
        x = x[14:len(x)-3]
        writer.writerow([x])
    list2 = len(diff['removed'])
    for i in range(list2):
        y = diff['removed'][i-1]
        y = str(y.values())
        y = y[14:len(y)-3]
        writer.writerow([y])
f.close()

