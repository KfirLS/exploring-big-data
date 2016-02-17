# -*- coding: utf-8 -*-
import os
import re
from subprocess import call
#call(["wget","-r", "midrag.co.il"]) #take a very long time watch out
a = os.listdir("midrag.co.il")
for f in a:
    if "disSectorSpesific.asp@" in f:
        file = open("midrag.co.il/" + f, 'r')
        text = file.read()
        ucd_text = unicode(text, 'windows-1255').strip()
        all =  re.finditer('OPTION.value=(\S*?)[\s>](.*?)<\/',ucd_text)
        for a in all:
            print a.group(1)
            print a.group(2)
