# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:57:43 2019

@author: dell
"""
#Oscars' web server for the 90 Academy Awards which will return the raw HTML. 
import requests
from bs4 import BeautifulSoup
house_raw = requests.get('http://clerk.house.gov/xml/lists/MemberData.xml').text
#This data is still in a string format (type(house_raw)), so it's difficult to search and navigate.

#There are more than 544,000 characters in the document!
print(len(house_raw))
'''
# The [0:1000] is a slicing notation 
# It gets the first (position 0 in Python) character until the 1000th character
print(house_raw[0:1000])
'''
#Let's make our first soup together using BeautifulSoup.
house_soup = BeautifulSoup(house_raw,'lxml')
#print(house_soup.prettify())
#First, let's inspect the different tags/elements in this tree of House member data. 
#This is the full tree of data.
children = []
for tag in house_soup.findChildren():
    if tag.name not in children:
        children.append(tag.name)
print(children)
#The .contents method is great for getting a list of the children below the tag as a 
#list. We can use the [0] slice to get the first member and their data in the list. 
#Interestingly, the <committee-assignments> tags are currently empty since these 
#have not yet been allocated, but will in the next few weeks.
print(house_soup.members.contents[0])  

#printing the First name after seeing the firstname tag in contents[0]
print(house_soup.members.contents[0].firstname)
        
#We can access the text inside the tag with .text
# .find() method to handle these hyphenated cases.        
print(house_soup.members.contents[0].find('state-fullname').text)        
        
#The .find_all() method will be your primary tool when working with structured data. 
#The <party> tag codes party membership (D=Dem, R=Rep) for each representative.        
print(house_soup.find_all('party')[:10])  
        
#iterate a loop over Party in the house_soup data to find how many each party have
Democrats = 0
Republic = 0
Other = 0
for p in house_soup.find_all('party'):
     if p.text == 'D':
         Democrats += 1
     elif p.text == 'R':
         Republic += 1
     else:
         Other += 1
print('There are {} Democrats, {} Republicans and {} others'.format(Democrats, Republic, Other))         



        
