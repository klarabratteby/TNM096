#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:11:31 2024

@author: quentin
"""

import copy
import random

maxsteps=10

courses=["MT101", "MT102", "MT103", "MT104", "MT105", "MT106", "MT107", 
         "MT201", "MT202", "MT203", "MT204", "MT205", "MT206",
         "MT301", "MT302", "MT303", "MT304",
         "MT401", "MT402", "MT403",
         "MT501", "MT502",
         "", ""]
random.shuffle(courses)

classrooms=dict(TP51=courses[:8], SP34=courses[8:16], K3=courses[16:24])

def random_conflict(classrooms):
    conflicts_list=[]
    
    for i in range(len(classrooms['TP51'])):
        for course_tuple in [("TP51", "SP34"), ("TP51", "K3"), ("SP34", "K3")]:
            if classrooms[course_tuple[0]][i] != "" and classrooms[course_tuple[1]][i] != "":
                if classrooms[course_tuple[0]][i][2] != 5 and classrooms[course_tuple[1]][i][2] != 5:
                    if classrooms[course_tuple[0]][i][2] == classrooms[course_tuple[1]][i][2]:
                        conflicts_list.append((course_tuple[0], i))
    
    conflict_tuple=random.choice(conflicts_list)
    
    return conflict_tuple
    
    
    

def count_conflicts(classrooms):
    conflicts_num=0
    
    for i in range(len(classrooms['TP51'])):
        for course_tuple in [("TP51", "SP34"), ("TP51", "K3"), ("SP34", "K3")]:
            if classrooms[course_tuple[0]][i] != "" and classrooms[course_tuple[1]][i] != "":
               if classrooms[course_tuple[0]][i][2] != 5 and classrooms[course_tuple[1]][i][2] != 5:
                   if classrooms[course_tuple[0]][i][2] == classrooms[course_tuple[1]][i][2]:
                        conflicts_num+=1

    
    return conflicts_num

conflicts=count_conflicts(classrooms)

while maxsteps > 0 and count_conflicts(classrooms) > 0:
    
    classroom_conflict_tuple=random_conflict(classrooms)
    
    classroom=classroom_conflict_tuple[0]
    course_index=classroom_conflict_tuple[1]
    
    classrooms_new=copy.deepcopy(classrooms)
    
    for key in classrooms:
        for i in range(len(classrooms[key])):
            if i != course_index:
                classrooms_test=copy.deepcopy(classrooms)
                classrooms_test[key][i]=classrooms[classroom][course_index]
                classrooms_test[classroom][course_index]=classrooms[key][i]
                
                conflicts_test=count_conflicts(classrooms_test)
                if conflicts_test < conflicts:
                    classrooms_new=copy.deepcopy(classrooms_test)
                    conflicts=conflicts_test

    classrooms=copy.deepcopy(classrooms_new)
    maxsteps-=1

for key in list(classrooms.keys()):
    print(key)
    print(classrooms[key])