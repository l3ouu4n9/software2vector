#!/usr/bin/env python

import pefile
import sys
#sys.path.append('/root')
import json
from filetype import *

result = {}
if len(sys.argv) < 2:
    result["stat"] = "error"
    result["messagetype"] = "string"
    result["message"] = "Usage: ./header.py INPUT_FILE1 INPUT_FILE2 ......"
    print json.dumps(result)
    exit(1)

for idx, name in enumerate(sys.argv):
    if idx == 0:
        continue
    #print 'File:',name
    try:
        f = File(name)
        if not f.is_pe():
            raise Exception("Not Pe file")
        if f.is_upx():
            raise Exception("Upx packed")
        pe = pefile.PE(name, fast_load=True)
        pe.parse_data_directories()
        array = [0]*256

        #print pe.FILE_HEADER
        for idx, s in enumerate(pe.FILE_HEADER.__keys__):
            array[(hash((s[0], pe.FILE_HEADER.__unpacked_data_elms__[idx]))%256)] += 1
        
        result["stat"] = "success"
        result["messagetype"] = "list"
        result["message"] = array
    except Exception as e:
        result["stat"] = "error"
        result["messagetype"] = "string"
        result["message"] = e.message
    finally:
        print json.dumps(result)
