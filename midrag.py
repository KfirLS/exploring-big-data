# -*- coding: utf-8 -*-
import os
import re
from subprocess import call
from bs4 import BeautifulSoup
import requests

base_url = "http://www.midrag.co.il/"

def download_whole_site():
    call(["wget","-r", "midrag.co.il"]) #this calls the system wget and downloads the whole site take a very long time watch out


def get_categories():#this function goes throgh the category files in the site directory and gets the category names
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

def cat_tables(categories):#this is suppose to build the url calls
    area = 2 #needs to be conected to a location func
    rd =1 #need to build funvtion that takes care of this
    for category in categories:
        #print category, categories[category]
        url_cat = category
        select ="select1=" + str(area)
        rdio = "rdio100=" + str(rd)
        ctl = "ctl100=" + category
        hafnaya = "curHafnaya="
        feild = "field="
        group = "group="
        url = base_url  + "disSectorSpesific.asp?" + url_cat +"&" +select + "&" + rdio + "&" + ctl + "&" +  hafnaya + "&" +feild +"&" + group + "A"#rslts"
        print url
        req = requests.get(url)
        req.encoding = "windows-1255"
        soup = BeautifulSoup(req.text, "lxml", exclude_encodings=["ISO-8859-8"])
        tables = soup.findAll("div", {"class" :"appSeperator"})
        print tables
        for table in tables:
            rows = table.findAll("tr")
            for row in rows:
                cells = row.findAll("td")
                #print cells
                for cell in cells:
                #print type(cells[0].find(text=True))
                 text = unicode.join(u'\n',map(unicode,cell))
                 #print text
                 #if len(re.findall(ur"[א-ת]", text))> 0:
                 #    print text
def get_locations():
    pass





if __name__ == '__main__':
    if "midrag.co.il" not in os.listdir(os.getcwd()):
        download_whole_site()
    categories = get_categories()
    cat_tables(categories)
    get_locations()
