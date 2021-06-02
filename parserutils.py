#!/usr/bin/env python

import re
import linecache

NUM_LINES = 0

def getIntValue(aLineNbr, aLogFileName):
    tempLine = linecache.getline(aLogFileName, aLineNbr)
    matchObj = re.search(r'(\s\d+$)', tempLine)
    if matchObj:
        return int(matchObj.group())
    else: return int(0)

def findIntValue(aLineNbr, aMatchString, aLogFileName):
    found = False
    line_nbr = aLineNbr

    while line_nbr < NUM_LINES:
        tempLine = linecache.getline(aLogFileName, line_nbr)
        regex = "^.*" + aMatchString + ".*(\s\d+$)"
        matchObj = re.search(regex, tempLine)
        if matchObj: return int(matchObj.group(1))
        else: line_nbr = line_nbr + 1

def file_len(fileName):
    with open(fileName) as file:
        i = -1
        for i, l in enumerate(file):
            pass
    return i + 1


