# compiles csv for all the SPLD regions where trough clouds have been recorded

import csv
import pandas as pd
import numpy as np

R1 = 'R1_complete.csv'
R2 = 'R2_complete.csv'
R3 = 'R3_complete.csv'
R4 = 'R4_complete.csv'
R1_newThemis = 'saved_R1_2-NEWTHEMIS.csv'
R2_newThemis = 'saved_R2_2-NEWTHEMIS.csv'

full_spld_fnames = []
full_spld_clouds = []
trough_fnames = []
trough_rnames = []
region_name = []
save_to = 'all_trough-and-region_SPLD.csv'


def cloudPick():
    for i, s in enumerate(full_spld_clouds):
        if 'trough' in s:
            trough_fnames.append(full_spld_fnames[i])
            trough_rnames.append(region_name[i])


def compileSPLD(region):
    with open(region) as rf:
        reader = csv.reader(rf, delimiter=',')
        r = 'DANGER'
        if region == 'R1_complete.csv':
            r = 'R1'
        elif region == 'R2_complete.csv':
            r = 'R2'
        elif region == 'R3_complete.csv':
            r = 'R3'
        elif region == 'R4_complete.csv':
            r = 'R4'
        elif region == 'saved_R1_2-NEWTHEMIS.csv':
            r = 'R1'
        elif region == 'saved_R2_2-NEWTHEMIS.csv':
            r = 'R2'
        for row in reader:
            if row[0] not in full_spld_fnames:
                # filename, cloud type, region name
                full_spld_fnames.append(row[0])
                full_spld_clouds.append(row[1])
                region_name.append(r)


### ADD WHICH REGION THEY'RE FROM ###
compileSPLD(R1)
compileSPLD(R2)
compileSPLD(R3)
compileSPLD(R4)
compileSPLD(R1_newThemis)
compileSPLD(R2_newThemis)

cloudPick()
data = {'file_id': trough_fnames, 'region': trough_rnames}
df = pd.DataFrame(data, columns=['file_id', 'region'])
df.to_csv(save_to, index=False, header=False)
