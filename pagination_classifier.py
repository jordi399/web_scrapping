#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
import libs
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
import copyyyy as copy
import glob
import os


# In[2]:


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


# In[3]:


def get_cat_links():
    all_cat_links=[]
    url = 'https://www.softwaresuggest.com/all-categories'
    page = FP.get_response_page(url,'get',{})
    soup = BeautifulSoup(page)
    body = soup.body
    grid = body.find('section',{'id':'category-grids'})
    for a in grid.find_all('a'):
        all_cat_links.append(a['href'])
    all_cat_links.remove('/')
    return (all_cat_links)

all_cats = get_cat_links()


# In[4]:


# broken = list(split(all_cats,20))
# vm_pages = []
# df = pd.DataFrame(columns=['Urls'])


# In[5]:


def viewmore(url):
    page = FP.get_response_page(url,'get',{})
    soup = BeautifulSoup(page)
    vmb = soup.find('div',class_='view_more_btn_div')
    if(vmb):
        return (url)


# In[6]:


# def master(urls,stack):
#     for idx,url in enumerate(urls):
#         if(viewmore(url)==True):
#             stack.append(url)
#     return (stack)


# In[7]:


# if __name__ == '__main__':
    
#     p0 = Process(target=master,args=(broken[0],))
#     p1 = Process(target=master,args=(broken[1],))
#     p2 = Process(target=master,args=(broken[2],))
#     p3 = Process(target=master,args=(broken[3],))
#     p4 = Process(target=master,args=(broken[4],))
#     p5 = Process(target=master,args=(broken[5],))
#     p6 = Process(target=master,args=(broken[6],))
#     p7 = Process(target=master,args=(broken[7],))
#     p8 = Process(target=master,args=(broken[8],))
#     p9 = Process(target=master,args=(broken[9],))
#     p10 = Process(target=master,args=(broken[10],))
#     p11 = Process(target=master,args=(broken[11],))
#     p12 = Process(target=master,args=(broken[12],))
#     p13 = Process(target=master,args=(broken[13],))
#     p14 = Process(target=master,args=(broken[14],))
#     p15 = Process(target=master,args=(broken[15],))
#     p16 = Process(target=master,args=(broken[16],))
#     p17 = Process(target=master,args=(broken[17],))
#     p18 = Process(target=master,args=(broken[18],))
#     p19 = Process(target=master,args=(broken[19],))
    
#     p0.start()
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
#     p6.start()
#     p7.start()
#     p8.start()
#     p9.start()
#     p10.start()
#     p11.start()
#     p12.start()
#     p13.start()
#     p14.start()
#     p15.start()
#     p16.start()
#     p17.start()
#     p18.start()
#     p19.start()
    
#     p0.join()
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     p6.join()
#     p7.join()
#     p8.join()
#     p9.join()
#     p10.join()
#     p11.join()
#     p12.join()
#     p13.join()
#     p14.join()
#     p15.join()
#     p16.join()
#     p17.join()
#     p18.join()
#     p19.join()


# In[8]:


if __name__ == '__main__':
    p = Pool(20)
    vm_pages = []
    vm_pages.append(p.map(viewmore,all_cats))


# In[14]:


vmps = set(vm_pages[0])
df = pd.DataFrame(vmps)
df.to_csv('viewmorepages.csv')


# In[ ]:




