#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:11:31 2024

@author: quentin
"""

import copy
import random
import pandas as pd

# Maximum number of steps
maxsteps = 10

# List of courses
courses = ["MT101", "MT102", "MT103", "MT104", "MT105", "MT106", "MT107",
           "MT201", "MT202", "MT203", "MT204", "MT205", "MT206",
           "MT301", "MT302", "MT303", "MT304",
           "MT401", "MT402", "MT403",
           "MT501", "MT502",
           "", ""]
random.shuffle(courses)

# Dataframe representing the classrooms and thier schedules
classrooms = pd.DataFrame(
    dict(TP51=courses[:8], SP34=courses[8:16], K3=courses[16:24]), range(9, 17))

# Defines the conflict list and choose one conflict


def random_conflict(classrooms):
    conflicts_list = []

    # Iterate over time slots
    for i in classrooms.index:
        # Check for conflicts
        for course_tuple in [("TP51", "SP34"), ("TP51", "K3"), ("SP34", "K3")]:
            if classrooms.loc[i, course_tuple[0]] != "" and classrooms.loc[i, course_tuple[1]] != "":
                if classrooms.loc[i, course_tuple[0]][2] != 5 and classrooms.loc[i, course_tuple[1]][2] != 5:
                    if classrooms.loc[i, course_tuple[0]][2] == classrooms.loc[i, course_tuple[1]][2]:
                        conflicts_list.append((course_tuple[0], i))

    # Choose random conflict from the list
    conflict_tuple = random.choice(conflicts_list)

    return conflict_tuple

# Count the conflicts 


def count_conflicts(classrooms):
    conflicts_num = 0
    # Iterate over the time slots
    for i in classrooms.index:
        # Check for conflicts between different classroom pairs
        for course_tuple in [("TP51", "SP34"), ("TP51", "K3"), ("SP34", "K3")]:
            if classrooms.loc[i, course_tuple[0]] != "" and classrooms.loc[i, course_tuple[1]] != "":
                if classrooms.loc[i, course_tuple[0]][2] != 5 and classrooms.loc[i, course_tuple[1]][2] != 5:
                    if classrooms.loc[i, course_tuple[0]][2] == classrooms.loc[i, course_tuple[1]][2]:
                        conflicts_num += 1

    return conflicts_num


# Count initial conflicts
conflicts = count_conflicts(classrooms)
# Main loop
while maxsteps > 0 and count_conflicts(classrooms) > 0:
    # Find a random conflicting time slot
    classroom_conflict_tuple = random_conflict(classrooms)

    classroom = classroom_conflict_tuple[0]  # Extract classroom index
    course_index = classroom_conflict_tuple[1]  # Extract time slot index

    # Make a copy of the current schedule
    classrooms_new = copy.deepcopy(classrooms)

    # Try swapping courses to resolve conflict
    for key in classrooms:
        for i in classrooms.index:
            if i != course_index:
                classrooms_test = copy.deepcopy(classrooms)
                classrooms_test.at[i,
                                   key] = classrooms.loc[course_index, classroom]
                classrooms_test.at[course_index,
                                   classroom] = classrooms.loc[i, key]
                # Count conflicts in the new schedule
                conflicts_test = count_conflicts(classrooms_test)
                if conflicts_test < conflicts:
                    # If the new schedule has fewer conflicts, update
                    classrooms_new = copy.deepcopy(classrooms_test)
                    conflicts = conflicts_test
    # Update schedule
    classrooms = copy.deepcopy(classrooms_new)
    maxsteps -= 1

print(classrooms)
