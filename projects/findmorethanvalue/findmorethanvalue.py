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
        return ('no element')
    else:
        return ('i found', list)

if __name__ == '__main__':
    input_list = list(map(int, input("Insert list (separated by comma): ").split(',')))
    value = int(input("Insert value: "))
    filtered_list = findmorethanvalue(input_list, value)
    print(checklist(filtered_list))


