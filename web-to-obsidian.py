import re #regular expression
from bs4 import BeautifulSoup #web parsing library
import io #manipulate files
import os #manipulate paths
import string
from datetime import date, datetime #get dates
import requests

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "https://www.jumia.co.ke/all-products/"

def make_request(url): #create a soup
    """request HTML soup object from url via beautiful soup"""
    req = requests.get(url, headers)
    soup = BeautifulSoup (req.content, 'html.parser')
    return soup

soup=make_request(url)

print("Extracting the data in HTML format")

def print_soup(soup):
    print(soup.prettify())

print_soup(soup)

print('generating md file, please wait...')

def get_details():
    for page in range(1,15):
        url = "https://www.jumia.co.ke/all-products/" + "?page=" +str(page)+"#catalog-listing"
        furl = requests.get(url)
        jsoup = BeautifulSoup(furl.content , 'html.parser')
        products = jsoup.find_all('div' , class_ = 'info')
        info = []
        for product in products:
            Name = product.find('h3' , class_="name").text.replace('\n', '')
            Price = product.find('div' , class_= "prc").text.replace('\n', '')
            try:
                Rating = product.find('div', class_='stars _s').text.replace('\n', '')
            except:
                Rating = 'None'

            info.append([Name,Price,Rating])
    return (info)

info=get_details()

def write_YAML_project(f,info):
    """ write file into .md file for Obsidian to read"""
    #YAML
    f.write("\ncreate_date: " + datetime.today().strftime('%Y-%m-%d') + "\n")
    print()
    for line in info:
        f.write(f"{line}\n")

def create_md_file_project(info):
    """output: project md file"""
    filename_project = "%s-%s.md" % ("atu", "test")
    project_path = "/Users/atu" + filename_project
    with io.open(project_path, "w+", encoding="UTF8") as f:
        write_YAML_project(f,info)

create_md_file_project(info)








