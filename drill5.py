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
from os.path import expanduser
home = expanduser("~")
import sqlite3
from datetime import datetime

def cutFiles(src,dst):
    currentTime=time()
    if not os.path.isdir(src):
        return False
    fileAgeMax=currentTime-tableGet()[1]
    names=os.listdir(src)
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
    tableUpdate()
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
    
def tableSetup():
    '''name="last updated"
    age=30
    date="I could use one"'''
    with sqlite3.connect("pointless.db") as connection:
        c=connection.cursor()
        print("created db")
        #c.execute("DROP TABLE IF EXISTS Pointless")
        c.execute("CREATE TABLE Pointless (Name TEXT, LastUpdate FLOAT, ReadableDate DATETIME)")
        #c.execute("INSERT INTO Pointless (Name,LastUpdate,ReadableDate) VALUES(?,?,?)",(name,age,date))
        '''c.execute("SELECT * FROM Pointless")
        rows=c.fetchall()
        for row in rows:
            print(row)'''

def tableGet():
    with sqlite3.connect("pointless.db") as connection:
        c=connection.cursor()
        c.execute("SELECT * FROM Pointless")
        rows=c.fetchall()
        for row in rows:
            print(row)
            return row
        
def tableUpdate():
    name="last updated"
    age=30
    date="last updated: "+str(datetime.now())
    with sqlite3.connect("pointless.db") as connection:
        c=connection.cursor()
        c.execute("DELETE FROM Pointless")
        c.execute("INSERT INTO Pointless (Name,LastUpdate,ReadableDate) VALUES(?,?,?)",(name,age,date))
        
#tableUpdate() 
#tableGet()
if not os.path.isfile("pointless.db"):
    tableSetup()
    lastDate="uninit"
else:
    lastDate=tableGet()[2]
#tableUpdate()
#tableGet()
    
root=tkinter.Tk()
title = tkinter.Label(root, text="File transfer utility\nCopies all files from source to destination that have been modified in the last 24 hours")
title.pack()

#lastDate="uninit"

#lastDate=tableGet()[2]

date=tkinter.Label(root,text=lastDate)
date.pack()

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

myString=entryText1.get()
print(myString)
transfer=tkinter.Button(root,text="Send Files",command=lambda: cutFiles(entryText1.get(),entryText2.get()))
transfer.pack()


root.mainloop()
