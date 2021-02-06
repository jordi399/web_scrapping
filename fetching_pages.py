#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
# import libs
# import fetching_pages as FP
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


# In[2]:


def type_of_page(url):
    soup = BeautifulSoup(get_response_page(url,'get',{}))
    if(soup.find('ul',{'id':'mypager_id'})):   
        return ('static number')
    
    elif(soup.find('div',{'id':'cat_list_tab_1'})):    
        return ('view more')
    
    else:  
        return ('other')


# In[3]:


'''
main_cat_url = "https://www.softwaresuggest.com/desktopview/getajaxdata"
main_cat_data = {'view':'desk_ajax_software_cat_header_dd'}
'''
def ALL_CAT_LINKS(main_cat_url,main_cat_data):
    main_cat_response = get_response_page(main_cat_url,'post',main_cat_data)#Getting response of main category button
    main_cat_soup = BeautifulSoup(main_cat_response,'html.parser')
    all_cat_links = []
    for i in set(main_cat_soup.find_all('div',{"id":"dd_tab_1"})):# for main category div containing all categories
        for j in set(i.find_all('li',class_='cat_title_color')):
            if(j.get_text()=='All Softwares Categories'): #Getting page of all links
                all_cats_page_url = ( j.find('a')['href'] )
                all_cats_page_response = get_response_page(all_cats_page_url,'get',{})#Getting response of each "All Software Category links"
                all_cats_page_soup = BeautifulSoup(all_cats_page_response,'html.parser')
                for k in set((all_cats_page_soup.find_all('section',{'id':'category-grids'}))):
                    for l in set(k.find_all('td')):
                        for m in set(l.find_all('a')):
                            if(m['href']):
                                all_cat_links.append(m['href'])
    all_cat_links = set(all_cat_links)
    return (all_cat_links)


# In[4]:


def get_response_page(url,method,data):
    if(type(data)==dict):
        if(method=='get'):
            return ((requests.get(url)).content)
        elif (method=='post' and data!=None):
            return ((requests.post(url,data)).text)
    else:
        print('data parameter should be in dictionary format')


# In[5]:


def get_products_from_a_page(page):
    soup = BeautifulSoup(page,'html.parser',from_encoding="iso-8859-1")
    scrap_urls = []
    for scrap_i in set(soup.find_all('div',class_='col-md-10 list_soft_content_main')):
        for scrap_j in scrap_i.find_all('a'):
            if(scrap_j.get_text()=='View Profile'):
                scrap_urls.append(scrap_j['href'])
        for scrap_k in scrap_i.find_all('span'):
            if(scrap_k.get_text()=='View Profile'):
                t_url = (scrap_k['onclick']).replace("ss_redirection(","")
                t_url = t_url.replace(" ' ","")
                t_url = t_url.replace("''","")
                t_url = t_url.replace("',)","")
                t_url = t_url.replace("'","")
                scrap_urls.append(t_url)
    return (scrap_urls)


# In[6]:


# url = 'https://www.softwaresuggest.com/desktopview/softwarelist'
# data = {'categoryid':1,'slug':'accounting','startlimit':25}


# In[7]:


def fget_products_from_a_page(page):
    
    soup = BeautifulSoup(page,'html.parser',from_encoding="iso-8859-1")
    scrap_urls = []
    for scrap_i in set(soup.find_all('div',class_='col-md-10 list_soft_content_main')):
        def anchor():
            for scrap_j in scrap_i.find_all('a'):
                if(scrap_j.get_text()=='View Profile'):
                    scrap_urls.append(scrap_j['href'])
        def span():
            for scrap_k in scrap_i.find_all('span'):
                if(scrap_k.get_text()=='View Profile'):
                    t_url = (scrap_k['onclick']).replace("ss_redirection(","")
                    t_url = t_url.replace(" ' ","")
                    t_url = t_url.replace("''","")
                    t_url = t_url.replace("',)","")
                    t_url = t_url.replace("'","")
                    scrap_urls.append(t_url)
                    
        if __name__ =="__main__":
            P1 = Process(target=anchor)
            P2 = Process(target=span)
            P1.start()
            P2.start()
            P1.join()
            P2.join()
    print('Done')
    return (scrap_urls)


# In[8]:


# page = get_response_page('https://www.softwaresuggest.com/360-degree-feedback-software','get',{})


# In[9]:


# print(len(get_products_from_a_page(page)))


# In[ ]:




