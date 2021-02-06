#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
import fetching_pages as FP
import sections as sxn
import create_json as C
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
import glob
import os
import http.client


# In[2]:


http.client._MAXHEADERS = 1000
import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv('625vmpages.csv')
df = df.drop('Unnamed: 0',axis=1)
vmps = df['0'].tolist()


# In[33]:


def pagination(data):
    xpath = 'https://www.softwaresuggest.com/desktopview/softwarelist'
    products = []
    button = 'view more'
    i = 25
    new_data = data
    while(button):
        page = FP.get_response_page(xpath,'post',new_data)
        temp = FP.get_products_from_a_page(page)
        products.append(temp)
        i = i+25
        new_data["startlimit"] = i
        if(len(temp)<25):
            button = None
    new_pro=[]
    for p in products:
        for i in p:
            new_pro.append(i)
    new_pro = set(new_pro)
    return(new_pro)


# In[34]:


data = {"categoryid": "66","startlimit":"25",
         "softwareid": "undefined",
         "software": "Server Monitoring Tools",
         "page_type": "Category",
         "current_cat_id": "66"}


# In[37]:


res = pagination(data)
for i in res:
    print(i)
print(len(res))


# In[ ]:




