import os
import requests
from bs4 import BeautifulSoup
import logging
import csv
import re


f = open('data/link_to_schools.txt')
lines = f.read().splitlines()
# for line in lines:
#lines[1]

def details(url, writer):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    name = soup.select('.col-xs-12 > h2')
    #print(name[0].getText().encode('utf-8').strip())
    school_name = name[0].getText().encode('utf-8')
    #print(school_name)

    area_ownership = soup.select('.col-xs-12 > em')
    area = area_ownership[1]
    ownership = area_ownership[0]
    #print(area.getText().encode('utf-8').strip())
    area = area.getText().encode('utf-8').strip()
    #print(ownership.getText().encode('utf-8').strip())
    ownership = ownership.getText().encode('utf-8').strip()

    type = soup.select('.sidebar-box')
    school_type = type[7].getText().encode('utf-8')
    #print(school_type)

    contact = type[3].select('li')
    address = contact[0].getText().encode('utf-8').strip()
    email = contact[1].getText().encode('utf-8').strip()
    phone = contact[2].getText().encode('utf-8')
    #print(address)
    #print(email)
    #print(phone)

    #fieldnames = ['Name of School', 'LGA', 'Ownership', 'Type of School', 'Address', 'Email', 'Phone Numbers']
    #f = open('data/schools_information.csv', 'ab')
    writer.writerow({'Name of School': school_name,
                     'LGA':area,
                     'Ownership':ownership,
                     'Type of School': school_type,
                     'Address': address,
                     'Email': email,
                     'Phone Numbers':phone,})


fieldnames = ['Name of School', 'LGA', 'Ownership', 'Type of School', 'Address', 'Email', 'Phone Numbers']
f = open('data/schools_information.csv', 'ab')
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
counter = 0
for line in lines:
    details(line, writer)
    counter = counter + 1
    print ('done %s school' % (str(counter)))
f.close()
