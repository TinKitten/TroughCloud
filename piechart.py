# random snippet code to create pie chart showing distribution of cloud type in SPLD
# wip, not relevant to images/metadata workflow

import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

cloudCounter_T = 0
cloudCounter_wispy = 0
cloudCounter_fluffy = 0
cloudCounter_bumpy = 0

file = open('R3_init.csv')
csv_f = csv.reader(file)
for row in csv_f:
    if "trough" in row[7]:
        cloudCounter_T += 1
    elif "wispy" in row[7]:
        cloudCounter_wispy += 1
    elif "fluffy" in row[7]:
        cloudCounter_fluffy += 1
    elif "bumpy" in row[7]:
        cloudCounter_bumpy += 1
    else:
        print("done")

# print(cloudCounter_fluffy)
# print(cloudCounter_wispy)
# print(cloudCounter_T)
# print(cloudCounter_bumpy)
pie2arr = [cloudCounter_fluffy, cloudCounter_bumpy, cloudCounter_wispy, cloudCounter_T]
my_labels2 = ["fluffy", "bumpy", "wispy", "trough"]
x = np.array(pie2arr)
plt.pie(x, labels=my_labels2)

plt.title("Cloud Types in R3")
plt.show()

# Nested pie chart
fig, ax = plt.subplots()
