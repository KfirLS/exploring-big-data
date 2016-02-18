# -*- coding: utf-8 -*-
import os
import re
from subprocess import call


def download_whole_site():
    call(["wget","-r", "midrag.co.il"]) #take a very long time watch out


def get_categories():
    cat_dict={}
    a = os.listdir("midrag.co.il")
    for f in a:
        if "disSectorSpesific.asp@" in f:
            file = open("midrag.co.il/" + f, 'r')
            text = file.read()
            ucd_text = unicode(text, 'windows-1255').strip()
            all =  re.finditer('OPTION.value=(\S*?)[\s>](.*?)<\/',ucd_text)
            for a in all:
                cat_dict[a.group(1)] =a.group(2)
                #print a.group(2)
    return cat_dict

def cat_tables(categories):
    for category in categories:
        print category, categories[category]
        url_cat = category
        

def get_locations():
    pass





if __name__ == '__main__':
    if "midrag.co.il" not in os.listdir(os.getcwd()):
        download_whole_site()
    categories = get_categories()
    cat_tables(categories)
    get_locations()
