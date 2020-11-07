import time
import re
import sys
from util import *

#initializing a list to work with
unknown_users = list()

all_students = import_data()
path = open_file()
handle = open(path)
minimum_time_requirement = int(input('Enter minimum time requirement in minutes : '))
for line in handle :
    found = 0
    parts = line.split(",")
    duration = time_conversion(parts[2])
    for i in range(len(all_students)) :
        if parts[0].lower() == all_students[i][1].lower() :
            all_students[i][3] = "p"
            found = 1
            all_students[i].append(duration)
            break
    if found == 0 :
        if parts[0] == "Name" :
            continue
        unknown_users.append(parts[0])


absent_count_c = 0
absent_count_d = 0
for i in range(len(all_students)) :
    if ( (all_students[i][3] == "a" or ( (all_students[i][3] =="p") and (all_students[i][4]<minimum_time_requirement) ) )
                     and (all_students[i][2] == "c") ) :
        absent_count_c = absent_count_c+1
    if ( (all_students[i][3] == "a" or ( (all_students[i][3] =="p") and (all_students[i][4]<minimum_time_requirement) ) )
                     and (all_students[i][2] == "d") ) :
        absent_count_d = absent_count_d+1

print("\nTotal",absent_count_c+absent_count_d,"absentees")
print("\nTotal absentees in C batch is :",absent_count_c,"\n------------------------\n")
for i in range(len(all_students)) :
    if ( (all_students[i][3] == "a" or ( (all_students[i][3] =="p") and (all_students[i][4]<minimum_time_requirement) ) )
                     and (all_students[i][2] == "c") ) :
        remark = None
        if all_students[i][3] =='a' :
            remarks = "**Did not enter meet**"
        else:
            remarks = f"##Attended meet only for {all_students[i][4]} minutes##"
        print("{0} {1:20} {2:20}".format(all_students[i][0],all_students[i][1],remarks))

print("\nTotal absentees in D batch is :",absent_count_d,"\n------------------------\n")
for i in range(len(all_students)) :
    if ( (all_students[i][3] == "a" or ( (all_students[i][3] =="p") and (all_students[i][4]<minimum_time_requirement) ) )
                     and (all_students[i][2] == "d") ) :
        remark = None
        if all_students[i][3] =='a' :
            remarks = "**Did not enter meet**"
        else:
            remarks = f"##Attended meet only for {all_students[i][4]} minutes##"
        print("{0} {1:20} {2:20}".format(all_students[i][0],all_students[i][1],remarks))


#printing users who could not be identified on comparison with database
if unknown_users :
    print("\nThe following users who attended the meet could not be identified")
    for i in range(len(unknown_users)) :
        print(unknown_users[i])

#closing of program
print("\n***Press Enter to terminate program***")
input()
print("***Terminating Program***")
time.sleep(2)
