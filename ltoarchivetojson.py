#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
import sys

csvFile = str(sys.argv[1])
os.system('sed 1,1d ' + csvFile + ' >> temp.csv && mv temp.csv ' + csvFile + '')
f = open(csvFile)
csv_f = csv.reader(f)
for row in csv_f:
