#!/usr/bin/env python

import pefile
import sys
import os
import json
import subprocess

result = {}
if len(sys.argv) < 2:
    result["stat"] = "error"
    result["messagetype"] = "string"
    result["message"] = "Usage: python smy.py INPUT_FILE1 INPUT_FILE2 ......"
    print json.dumps(result)
    exit(1)

for idx, name in enumerate(sys.argv):
    if idx == 0:
        continue
    try:
        filename, extension = os.path.splitext(name)
        if extension != '.asm':
            raise Exception('Not .asm file')

        with open(name, 'r') as fd:
            data = fd.read()

        symbol = ['-', '+', '*', ']', '[', '?', '@']
        array = [0]*8
        for idx, s in enumerate(symbol):
            array[idx] += data.count(s)

        result["stat"] = "success"
        result["messagetype"] = "list"
        result["message"] = "-: %d, +: %d, *: %d, ]: %d, [: %d, ?: %d, @: %d" % (array[0], array[1], array[2], \
            array[3], array[4], array[5], array[6])
    except Exception as e:
        result["stat"] = "error"
        result["messagetype"] = "string"
        result["message"] = e.message
    finally:
        print json.dumps(result)
