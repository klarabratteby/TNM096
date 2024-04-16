#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:11:31 2024

@author: quentin
"""

import copy
import random
import pandas as pd

maxsteps=10

courses=["MT101", "MT102", "MT103", "MT104", "MT105", "MT106", "MT107", 
         "MT201", "MT202", "MT203", "MT204", "MT205", "MT206",
         "MT301", "MT302", "MT303", "MT304",
         "MT401", "MT402", "MT403",
         "MT501", "MT502",
         "", ""]
random.shuffle(courses)

classrooms=pd.DataFrame(dict(TP51=courses[:8], SP34=courses[8:16], K3=courses[16:24]), range(9, 17))

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

conflicts=count_conflicts(classrooms)

while maxsteps > 0 and count_conflicts(classrooms) > 0:
    
    classroom_conflict_tuple=random_conflict(classrooms)
    
    classroom=classroom_conflict_tuple[0]
    course_index=classroom_conflict_tuple[1]
    
    classrooms_new=copy.deepcopy(classrooms)
    
    for key in classrooms:
        for i in classrooms.index:
            if i != course_index:
                classrooms_test=copy.deepcopy(classrooms)
                classrooms_test.at[i, key]=classrooms.loc[course_index, classroom]
                classrooms_test.at[course_index, classroom]=classrooms.loc[i, key]
                
                conflicts_test=count_conflicts(classrooms_test)
                if conflicts_test < conflicts:
                    classrooms_new=copy.deepcopy(classrooms_test)
                    conflicts=conflicts_test

    classrooms=copy.deepcopy(classrooms_new)
    maxsteps-=1

print(classrooms)