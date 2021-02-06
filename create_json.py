#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
# import libs
import fetching_pages as FP
import sections as sxn
# import create_json as C
import fetching_from_database as ffb

import bs4
import mysql.connector
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import time
import sys
from datetime import datetime
import random
from multiprocessing import Pool, Process


# In[4]:


def scrap_page(scrap_url):
    
    scrapped_page = FP.get_response_page(scrap_url,'get',{})
    scrap_soup = BeautifulSoup(scrapped_page,'html.parser')

    scrap_head = scrap_soup.head
    scrap_body = scrap_soup.body
    
    header = scrap_body.find('div',{"id":"sticky_header"})
    breadcrumb = header.find('div',class_='breadcrumb_main_profile')
    overview = scrap_body.find('div', {"id":"overview"})
    screenshots = scrap_body.find('div',{"id":"screenshots"})
    video = scrap_body.find('div',{"id":"video_panel"})
    award_section = scrap_body.find('div',{"id":"award_section"})
    features = scrap_body.find('div',{"id":"features"})
    specifications = scrap_body.find('div',{"id":"specifications"})
    languages = scrap_body.find('div',{"id":"languages"})
    users = scrap_body.find('div',{"id":"users"})
    company_details = scrap_body.find('div',{"id":"company-details"})
    description = scrap_body.find('div',{"id":"description"})
    customers = scrap_body.find('div',{"id":"customers"})
    alternatives = scrap_body.find('div',{"id":"alternatives"})
    frequently_used_together = scrap_body.find('div',{"id":"frequently_used_together"})
    compare = scrap_body.find('div',{"id":"compare"})
    pricing = scrap_body.find('div',{"id":"pricing"})
    
    bc = sxn.BREADCRUMB(breadcrumb)
    logo = sxn.LOGO(header)
    name = sxn.NAME(header)
    over_view_new = sxn.OVERVIEW(overview)
    ScreenShots = sxn.SCREENSHOTS(screenshots)
    Awards = sxn.AWARDS(award_section)
    Features = sxn.FEATURES(features)
    Specifications = sxn.SPECIFICATIONS(specifications)
    Video = sxn.VIDEO(video)
    Users = sxn.USERS(users)
    Details = sxn.DETAILS(company_details)
    Description = sxn.DESCRIPTION(description)        
    Pricing = sxn.PRICING(pricing)

    #Finalizing the main dictionary
    Super_one = {'Category':bc.Category(),'Software':bc.Software(),'Logo':logo,'Name':name, over_view_new.Key():over_view_new.Value(),
             
             ScreenShots.Key():ScreenShots.Value(),Video.Key():Video.Value(),
             
             Awards.Key():Awards.Value(),  Features.Key():Features.Value(),
             
             Specifications.Key():Specifications.Value(), 
             
             Users.Key():Users.Value(),  Details.Key():Details.Value(),
             
             Description.Key():Description.Value(),  Pricing.Key():Pricing.Value()
            }

    file_name = str(name)
    json_object = json.dumps(Super_one,indent=1)
    with open(file_name+'.json', 'w') as f:
        f.write(json_object)
        f.close()  


# In[11]:


# scrap_page('https://www.softwaresuggest.com/gallerymanager')

# temp_page = FP.get_response_page('https://www.softwaresuggest.com/gallerymanager','get',{})

# temp_soup = BeautifulSoup(temp_page)

# temp_body = temp_soup.body

# ss = temp_body.find('div',{'id':'video_panel'})

# ss.find('h2')

# ss.find('iframe')['src']


# In[12]:


# scrap_page('https://www.softwaresuggest.com/conferences-i-o')


# In[ ]:




