# Download THEMIS images into specified folder
# check pathsave folder name &  file_list name (csv used is generated from Search THEMIS Query/ csv downloaded here:
# https://viewer.mars.asu.edu/viewer/themis/#P=V33151003&T=1)
# double check url, odtbws_num {depends on number following "odtbws1_" in first image of the csv specific url}


import pandas as pd
import requests
import PIL
from PIL import Image
import time


def imagesize(odtbws_num):
    global odtbws_import
    n = odtbws_num
    if n < 10:
        odtbws_import = "000" + str(n)
    elif n >= 10 and n < 100:
        odtbws_import = "00" + str(n)
    elif n >= 100 and n < 1000:
        odtbws_import = "0" + str(n)
    elif n >= 1000:
        odtbws_import = str(n)
    else:
        print("error, check file name")
    return odtbws_import


if __name__ == '__main__':
    file_list = pd.read_csv("search_results_R4_NEWTHEMIS.csv")
    fileName = file_list['file_id']
    pathsave = 'SPLD_R4_new/'

    try:
        for ii in fileName:
            i = 0
            odtbws_num = 0  # input starting value
            while not fileName.empty:
                odtbws_import = imagesize(odtbws_num)
                ii = fileName[i]
                # print(ii)
                ii = ii.strip('\n')
                parent = "v" + ii[1:4] + "xx"
                url = 'https://image.mars.asu.edu/convert/' + ii + '.png?image=/mars/readonly/themis/pds/ODTSDP_v1/browse/odtbws1_' + odtbws_import + '/' + parent + '/' + ii + '.png&rotate=0&format=png'
                img_data = requests.get(url).content
                fname = ii + ".png"
                with open(pathsave + fname, 'wb') as handler:
                    handler.write(img_data)
                    time.sleep(10)
                image = PIL.Image.open("SPLD_R4_new/" + fname) # this is to check that the image has been downloaded correctly
                # because the image will be a 300x300 placeholder if not, and the odtbws number will be incremented to
                # eventually download the correct image (as determined by size)
                w1, h1 = image.size
                if w1 == 300 and h1 == 300:
                    odtbws_num = odtbws_num + 1
                else:
                    with open(pathsave + fname, 'wb') as handler:
                        handler.write(img_data)
                    i = i + 1
    except KeyError:
        print("done")
