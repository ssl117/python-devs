import cv2
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

import os
from os import listdir
from os.path import isfile, join

# RENOMBRAR TODOS LOS ARCHIVOS A -IMAGE X- 

def rename_files(mypath):

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    i = 1

    for file in onlyfiles:
        old_file_name = mypath + str(file)
        new_file_name = mypath + 'image-' + str(i) + '.jpg'
        os.rename(old_file_name, new_file_name)
        i = i + 1
    
mypath = 'C:/Users/Sebastian/Desktop/fotos-prueba/'

rename_files(mypath)

# TRANSFORMAMOS LAS FOTOS A BLANCO Y NEGRO

def toBlackandWhite(mypath):
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    i = 1

    for file in onlyfiles:
        img_path = mypath + str(file)
        print(img_path)
        img = cv2.imread(img_path)

        img_low = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img_low, cv2.COLOR_RGB2GRAY)

        write_path = mypath + 'image-' + str(i) + '-gray.jpg'
        write_path_low = mypath + 'image-' + str(i) + '-low.jpg'
        cv2.imwrite(write_path, img_gray, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        cv2.imwrite(write_path_low, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        i = i + 1
        
mypath = 'C:/Users/Sebastian/Desktop/fotos-prueba/'

toBlackandWhite(mypath)