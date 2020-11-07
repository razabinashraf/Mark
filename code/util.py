import re
import sqlite3
import re
import sys
import time
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


#function to convert "-- hrs -- min" to minutes
def time_conversion(line):
    total_time = 0
    x = re.findall('(\d+) hr', line) #converting hrs to minutes
    if x:
        total_time += int(x[0])*60
    x = re.findall('(\d+) min', line) #adding minutes to total time
    if x:
        total_time += int(x[0])
    return total_time

#function to import data from database
def import_data() :
    all_students = list()
    conn = sqlite3.connect('Student_data.sqlite')
    cur = conn.cursor()

    i = 0    #for keeping track of student no
    cur.execute('SELECT * FROM c_batch')
    rows = cur.fetchall()
    for row in rows :
        row_list = list(row)             #converting returned tuple into list
        all_students.append(row_list)    # adding current student detail to "all_students" list
        all_students[i].append("c")      # adding section to current student detail
        all_students[i].append("a")      # initializing with 'a' for absent
        i = i+1

    cur.execute('SELECT * FROM d_batch')
    rows = cur.fetchall()
    for row in rows :
        row_list = list(row)
        all_students.append(row_list)
        all_students[i].append("d")
        all_students[i].append("a")
        i = i+1
    return all_students

def open_file() :
    while True :
        print("Select attendance data file to be opened (CSV only)")
        time.sleep(3)
        root = tk.Tk()
        root.withdraw()
        downloads_dir = str(os.path.join(Path.home(), "Downloads"))
        path = filedialog.askopenfilename(initialdir = downloads_dir,title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        root.destroy()
        if not path:
            print("!!!!! No file selected !!!!!")
            choice = input("Enter 'y' to try opening again: ")
            if choice != "y" :
                print("***Program Aborted***")
                time.sleep(2)
                sys.exit()
            else :
                continue
        if (re.search('.*csv' , path)):
            return path
        else :
            print ("!!!!! Not a valid csv file, Try again !!!!!")
            choice = input("Enter 'y' to try opening again: ")
            if choice != "y" :
                print("***Program Aborted***")
                time.sleep(2)
                sys.exit()
