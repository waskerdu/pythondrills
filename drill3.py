# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:27:14 2017
drill 3
@author: Riley
"""

import shutil
import os
from time import time

def cutFiles(src,dst):
    fileAgeMax=24*60*60
    names=os.listdir(src)
    currentTime=time()
    print(currentTime)
    for name in names:
        #print (name)
        if name.endswith(".txt"):
            path=src+name
            #print(path)
            fileAge=currentTime-os.path.getmtime(path)
            print (fileAge)
            if fileAge<fileAgeMax:
                shutil.move(path,dst)
            #shutil.move(path,dst)
cutFiles("C:/Users/Riley/Desktop/FolderA/","C:/Users/Riley/Desktop/FolderB/")
print("")
cutFiles("C:/Users/Riley/Desktop/FolderB/","C:/Users/Riley/Desktop/FolderA/")