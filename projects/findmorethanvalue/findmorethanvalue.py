#!/usr/bin/env python3
#import sys
def findmorethanvalue(list, value):
    filtered_list = []
    for i in list:
        if i > value:
            filtered_list += [i]
    return filtered_list

def checklist(list):
    if len(list) == 0:
        print ('no element')
    else:
        print ('i found', list)

input_list = list(map(int, input("Insert list (seoarated by comma): ").split(',')))
value = int(input("Insert value: "))
filtered_list = findmorethanvalue(input_list, value)
checklist(filtered_list) 


#