#!/usr/bin/python

import os

listdir = os.listdir('.')
for x in listdir:
    if os.path.isdir(x):
    	print x


os.chdir('/var/log')

listsdir = os.listdir('.')

for y in listsdir:
    print y
