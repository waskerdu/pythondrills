# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:25:05 2017
drill 4
@author: Riley
"""

import shutil
import os
from time import time
import tkinter
from tkinter import filedialog
from os.path import expanduser
home = expanduser("~")

def cutFiles(src,dst):
    if not os.path.isdir(src):
        return False
    fileAgeMax=24*60*60
    names=os.listdir(src)
    currentTime=time()
    print(currentTime)
    for name in names:
        #print (name)
        if name.endswith(".txt"):
            path=src+"/"+name
            #print(path)
            fileAge=currentTime-os.path.getmtime(path)
            print (fileAge)
            if fileAge<fileAgeMax:
                shutil.move(path,dst)
    return True

def magicStuff(toReturn):
    print("did stuff!")
    print (entryText1.get())
    print(toReturn)
    return True

def browse():
    dir_opt={}
    dir_opt['initialdir'] = home + '\\'
    dir_opt['title'] = 'Please select directory'
    result=tkinter.filedialog.askdirectory(**dir_opt)
    print(result)
    return str(result)
   
def browseFunc1():
    global entryText1
    dir_opt={}
    dir_opt['initialdir'] = home + '\\'
    dir_opt['title'] = 'Please select directory'
    result=tkinter.filedialog.askdirectory(**dir_opt)
    entryText1.delete(0,tkinter.END)
    entryText1.insert(0,result)
    
def browseFunc2():
    global entryText2
    dir_opt={}
    dir_opt['initialdir'] = home + '\\'
    dir_opt['title'] = 'Please select directory'
    result=tkinter.filedialog.askdirectory(**dir_opt)
    entryText2.delete(0,tkinter.END)
    entryText2.insert(0,result)

root=tkinter.Tk()
title = tkinter.Label(root, text="File transfer utility\nCopies all files from source to destination that have been modified in the last 24 hours")
title.pack()

entryText1=tkinter.Entry(root)
entryText1.pack()
entryText1.delete(0, tkinter.END)
entryText1.insert(0, "path to files to copy")

browse1=tkinter.Button(root,text="Browse",command=browseFunc1)
browse1.pack()

entryText2=tkinter.Entry(root)
entryText2.pack()
entryText2.delete(0, tkinter.END)
entryText2.insert(0, "path to folder to copy to")

browse2=tkinter.Button(root,text="Browse",command=browseFunc2)
browse2.pack()


#result = tkinter.tkFileDialog.askdirectory(**dir_opt)

myString=entryText1.get()
print(myString)
#transfer=tkinter.Button(root,text="Send Files",command=lambda: magicStuff("lambda is a thing"))
transfer=tkinter.Button(root,text="Send Files",command=lambda: cutFiles(entryText1.get(),entryText2.get()))
#transfer=tkinter.Button(root,text="Send Files",command=lambda: cutFiles(browse(),browse()))
transfer.pack()


root.mainloop()

'''root=tkinter.Tk()
#root.title("file transfer utility")
#menu=ttk.Frame(root,padding="3 3 12")
ttk.Button(root, text="Hello World").grid()
root.mainloop()'''



            #shutil.move(path,dst)
#cutFiles("C:/Users/Riley/Desktop/FolderA/","C:/Users/Riley/Desktop/FolderB/")
#print("")
#cutFiles("C:/Users/Riley/Desktop/FolderB/","C:/Users/Riley/Desktop/FolderA/")