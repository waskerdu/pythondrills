# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:32:14 2017
file mover
@author: Riley
"""

import shutil
import os

def cutFiles(src,dst):
    names=os.listdir(src)
    for name in names:
        #print (name)
        if name.endswith(".txt"):
            path=src+name
            print(path)
            shutil.move(path,dst)

cutFiles("C:/Users/Riley/Desktop/FolderA/","C:/Users/Riley/Desktop/FolderB/")