#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup 

poem_of_the_day_url = 'https://www.poetryfoundation.org/poems/poem-of-the-day'
harlem = 'https://www.poetryfoundation.org/poems/46548/harlem'
html = requests.get(poem_of_the_day_url).text
soup = BeautifulSoup(html, "html.parser")

#find title
print(soup.find('div',{'class':'c-feature-hd'}).getText().strip())
#find author
print(soup.find('div',{'class':'c-feature-sub c-feature-sub_vast'}).getText().strip())

print()


#code for poem
poem_raw = soup.find('div', {'class':'o-poem'}).findAll('div') 
for line in poem_raw:
    print(line.getText())


