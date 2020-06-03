# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Here only boolean news can be authentcated
#We were previously using selenium and firfox webdriver, but being unable to find an id or classname for google search bar, we are hence following a different method

from googlesearch import search
import re

class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      calculator =0
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=10,pause=2):
         count += 1
         #mention the source you are willing to find below
         if re.search('wiki', i, re.IGNORECASE):
             print (count)
             print(i + '\n')
             calculator+=1
      percentage=100*calculator/10
      print(str(percentage) + 'percent accurate.') 
         
             
      

if __name__=='__main__':
    #input what you are searching below in between the inverted commas
   gs = Gsearch_python("Is Russia winning in Syria?")
   gs.Gsearch()
   
   