#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:11:31 2024

@author: quentin
"""

## Imports
import copy
import random
import pandas as pd

## Initial arguments
maxsteps=10

courses=["MT101", "MT102", "MT103", "MT104", "MT105", "MT106", "MT107", 
         "MT201", "MT202", "MT203", "MT204", "MT205", "MT206",
         "MT301", "MT302", "MT303", "MT304",
         "MT401", "MT402", "MT403",
         "MT501", "MT502",
         "", ""]
random.shuffle(courses)

classrooms=pd.DataFrame(dict(TP51=courses[:8], SP34=courses[8:16], K3=courses[16:24]), range(9, 17))

## Functions
def random_conflict(classrooms):
    conflicts_list=[]
    
    for i in classrooms.index:
        for course_tuple in [("TP51", "SP34"), ("TP51", "K3"), ("SP34", "K3")]:
            if classrooms.loc[i, course_tuple[0]] != "" and classrooms.loc[i, course_tuple[1]] != "":
                if classrooms.loc[i, course_tuple[0]][2] != 5 and classrooms.loc[i, course_tuple[1]][2] != 5:
                    if classrooms.loc[i, course_tuple[0]][2] == classrooms.loc[i, course_tuple[1]][2]:
                        conflicts_list.append((course_tuple[0], i))
    
    conflict_tuple=random.choice(conflicts_list)
    
    return conflict_tuple

def count_conflicts(classrooms):
    conflicts_num=0
    
    for i in classrooms.index:
        for course_tuple in [("TP51", "SP34"), ("TP51", "K3"), ("SP34", "K3")]:
            if classrooms.loc[i, course_tuple[0]] != "" and classrooms.loc[i, course_tuple[1]] != "":
               if classrooms.loc[i, course_tuple[0]][2] != 5 and classrooms.loc[i, course_tuple[1]][2] != 5:
                   if classrooms.loc[i, course_tuple[0]][2] == classrooms.loc[i, course_tuple[1]][2]:
                        conflicts_num+=1
    
    return conflicts_num

def optimize_conflicts(classrooms, classtuple, index_to_test):
    conflicts=count_conflicts(classrooms)
    classroom=classtuple[0]
    course_index=classtuple[1]
    classrooms_new=None
    
    for col in classrooms:
        for i in index_to_test:
            if i != course_index:
                classrooms_test=copy.deepcopy(classrooms)
                classrooms_test.at[i, col]=classrooms.loc[course_index, classroom]
                classrooms_test.at[course_index, classroom]=classrooms.loc[i, col]
                
                conflicts_test=count_conflicts(classrooms_test)
                if conflicts_test <= conflicts:
                    classrooms_new=copy.deepcopy(classrooms_test)
                    conflicts=conflicts_test
    
    if classrooms_new is not None:
        return classrooms_new

    return classrooms

def apply_preferences(classrooms, classtuples, prefs):
    for classtuple in classtuples:
        course_index=classtuple[1]
        if course_index in prefs:
            prefs.remove(course_index)
            classtuples.remove(classtuple)
            
    for classtuple in classtuples:
        classrooms=optimize_conflicts(classrooms, classtuple, prefs)
    
    return classrooms


## Main
conflicts=count_conflicts(classrooms)

while maxsteps > 0 and count_conflicts(classrooms) > 0:
    ## Min-Conflicts
    classroom_conflict_tuple=random_conflict(classrooms)
    classrooms=optimize_conflicts(classrooms, classroom_conflict_tuple, classrooms.index)
    
    maxsteps-=1
    
    ## Empty classes
    classrooms_empty=[]
    classrooms_empty_pref=[9, 12, 16]
    for col in classrooms:
        for i in classrooms[(classrooms[col] == '')].index.tolist():
            classrooms_empty.append((col, i))
    
    classrooms=apply_preferences(classrooms, classrooms_empty, classrooms_empty_pref)
    
    ## MT50x
    classrooms_50x=[]
    classrooms_50x_pref=[13, 14]
    for col in classrooms:
        for i in classrooms[(classrooms[col].str.contains('MT5'))].index.tolist():
            classrooms_50x.append((col, i))
    
    classrooms=apply_preferences(classrooms, classrooms_50x, classrooms_50x_pref) 

print(classrooms)