#!/usr/bin/env python

import sys
import os
import re
from os import path
import regexdefines
import parserutils

def browseFolder(aFolder):
    dirList = os.listdir(aFolder)

    for fname in dirList:
        fullpath = aFolder + "\\" + fname
        if os.path.isdir(fullpath):
            browseFolder(fullpath)
        else:
            if fname.endswith(".txt") or fname.endswith(".py"):
                analyse_file(fullpath)

def analyse_file(aSrcFile, aTargetFile):

    cleaned_count = 0
    cleaned_name = "cleaned_lines.txt"
    cleaned_lines = open(cleaned_name, "w")

    try:
        with open(aSrcFile, 'r') as logfile:

            for line in logfile:
                for regex in regexdefines.regex_array:
                    found = re.match(regex, line)

                    if found:
                        break

                if not found:
                    aTargetFile.write(line)
                else:
                    cleaned_lines.write(line)
                    cleaned_count = cleaned_count + 1

        print(str(cleaned_count) + " lines cleaned. See \"" + str(cleaned_name) + "\" for details.")

    except IOError:
        print("Cannot open \"" + aSrcFile + "\"")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.exit("Usage!")

    full_name = sys.argv[1]
    print("Source: " + full_name)

    source_name, source_extension = path.splitext(full_name)
    target_name = source_name + "_clean" + source_extension
    print("Target: " + target_name)

    target_file = open(target_name, "w")
    parserutils.NUM_LINES = parserutils.file_len(sys.argv[1])
    print("Analysing " + str(parserutils.NUM_LINES) + " lines of trace log")
    
    analyse_file(full_name, target_file)
    target_file.close()

