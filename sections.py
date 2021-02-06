#!/usr/bin/env python
# coding: utf-8

# In[2]:


import import_ipynb
# import libs
import fetching_pages as FP
# import sections as sxn
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


class DESCRIPTION:
    
    def __init__(self,description):
        self.description = description
        
    def Key(self):
        if(self.description):
            for i in self.description.find_all('h2'):
                key=(i.get_text()) 
            return (key)
        else:
            return ('Description')
    def Value(self):
        if(self.description):
            D_value = ""
            for i in self.description.find_all('div',class_='software_discription section_bg_prof'):
                for j in i.find_all('div'):
                    for k in j.find_all('p'):
                        D_value = D_value+str(k.get_text())
            return (D_value)
        else:
            return (None)


# In[3]:


class PRICING:
    
    def __init__(self,pricing):
        self.pricing = pricing

    def Key(self):   
        if(self.pricing):
        #Getting the P_key for whole
            for i in self.pricing.find_all('div', class_='row section_main'):
                for j in i.find_all('div', class_='col-12 section_title'):
                    key =  (j.find('h2').get_text())
            return (key)
        else:
            return ('Pricing')

        #Getting value
    def Value(self):
        if(self.pricing):
            
            names_of_plan = []
            costs = []
            for i in self.pricing.find_all('div', class_='row price_row_mar_top'):
                for j in i.find_all('div', class_='col-xl-4 pricing_sec_cell'):
                    for k in j.find_all('div', class_='table-header'):
                        for l in k.find_all('div', class_='d-flex align-items-center justify-content-center soft-plan-heading'):
                            names_of_plan.append(
                                str(l.get_text()).replace('\n', ""))
                        for m in k.find_all('div', class_='d-flex flex-column align-items-center justify-content-center soft-plan-price'):
                            costs.append(str(m.get_text()).replace("\n", ""))
            length = len(costs)
            features_of_plans = [[] for x in range(len(costs))]
            plans = [{} for x in range(len(costs))]
            for fv in self.pricing.find_all('div', class_='soft-pricing-table'):
                temp = str(fv.find(
                    'div', class_='d-flex align-items-center justify-content-center soft-plan-heading').get_text())
                temp = temp.replace("\n", "")
                for check in range(length):
                    if(temp == names_of_plan[check]):
                        for fu in fv.find_all('div', class_='soft-pricing-instruction'):
                            for ft in fu.find_all('ul'):
                                for fs in ft.find_all('li'):
                                    features_of_plans[check].append(
                                        str(fs.get_text()).replace("\n", ""))
            P_value = {}
            list_of_plans = [{} for ck in range(len(names_of_plan))]
            for i in range(length):
                t_dict = plans[i]
                features_of_plans[i].pop()
                t_dict.update(
                    {"Name": names_of_plan[i], "Costs": costs[i], "Benifits": features_of_plans[i]})
                P_value.update({"Plan"+str(i+1): t_dict})
            return (P_value)
        else:
            return (None)


# In[4]:


class DETAILS:
    
    def __init__(self,company_details):
        self.company_details = company_details
    
    def Key(self):
        return ('Company Details')
            
    def Value(self):
        if(self.company_details):
            details_value = {}
            for i in (self.company_details.find_all('div',class_='row section_main')):
                for j in i.find_all('div',class_='col-12 section_title'):
                    Details=(j.find('h2').get_text())
                for k in i.find_all('ul'):
                    for l in k.find_all('li'):
                        for s in l.find_all('span'):
                            for b in s.find_all('b'):
                                tk = (b.get_text())
                        for p in l.find_all('p'):
                            if(p.find('a')!=None):
                                temp = p.find('a')
                                tv = ( temp['href'] )
                            else:
                                tv = ( p.get_text())
                            details_value.update( {tk:tv} )
            return (details_value)
        else:
            return (None)


# In[5]:


class USERS:
    
    def __init__(self,users):
        self.users = users
        
    def Key(self):
        if(self.users):
            key = (self.users.find('div',class_='col-12 d-flex align-items-center justify-content-between section_title section_title_with_btn')).find('h2').get_text()
            return (key)
        else:
            return ('Users')
    def Value(self):
        if(self.users):
            B_list=[]
            A_list=[]
            C_list=[]
            user_main = {}
            for i in self.users.find_all('div',class_='row section_main'):
                for k in i.find_all('div',class_='section_bg_prof'):
                    for l in k.find_all('div',class_='user_title'):
                            temp_k = l.get_text()
                    for m in k.find_all('ul',class_='d-flex user_list_main'):
                            for n in m.find_all('li'):
                                o = n.find('i')
                                if(o.get_text()!='cancel'):
                                    temp_v = (n.get_text()).replace(o.get_text(),"")
                                    if(l.get_text()=='Business'):
                                        B_list.append((n.get_text()).replace(o.get_text(),""))
                                    elif(l.get_text()=='Available Support'):
                                        A_list.append((n.get_text()).replace(o.get_text(),""))
                                    else:
                                        C_list.append((n.get_text()).replace(o.get_text(),""))
                            if(temp_k=='Business'):
                                user_main.update({temp_k:B_list})
                            elif(temp_k=='Available Support'):
                                user_main.update({temp_k:A_list})
                            else:
                                user_main.update({temp_k:C_list})
            return (user_main)
        else:
                return (None)


# In[6]:


class SPECIFICATIONS:
    
    def __init__(self,specifications):
        self.specifications = specifications
        
    def Key(self):
        if (self.specifications):
            key = self.specifications.find('h2').get_text()
            return (key)
        else:
            return ('Specifications')

    def Value(self):
        if (self.specifications):
            fspex = {}
            for i in (self.specifications.find_all('div', class_='row section_main')):
                for j in (i.find_all('div', class_='row')):
                    for k in (j.find_all('div', class_='col-xs-12 col-sm-12 col-xl-6 speci_column')):
                        if(k.find('h3') == None):
                            for l in k.find_all('ul'):
                                for m in l.find_all('li'):
                                    if(m.find('i') == None):
                                            span = m.find('span')
                                            p = m.find('p')
                                            fspex.update(
                                                {span.get_text(): p.get_text()})
                                    else:
                                            i_li = m.find('i')
                                            spans = m.find('span')
                                            if(i_li.get_text() == 'cancel'):
                                                fspex.update(
                                                    {spans.get_text(): False})
                                            else:
                                                fspex.update(
                                                    {spans.get_text(): True})
                        else:
                            for n in k.find_all('div', class_='specification_small_title'):
                                for o in n.find_all('h3'):
                                    p = o.get_text()
                                    if(p == 'Other Categories'):
                                        ocats = []
                                        for q in k.find_all('div', class_='d-flex flex-wrap speci_other_cat'):
                                            for r in q.find_all('a', class_='ga_track_oth_cat d-flex align-items-center'):
                                                ocats.append(r.get_text())
                                        fspex.update({p: ocats})
                                    else:
                                        ans = []
                                        for s in k.find_all('ul'):
                                            for t in s.find_all('li'):
                                                i_t = t.find('i').get_text()
                                                s_t = t.find('span').get_text()
                                                if(i_t != 'cancel'):
                                                    ans.append(s_t)
                                        if(len(ans) != 0):
                                            fspex.update({p: ans})
                                        else:
                                            fspex.update({p: False})
                    for u in j.find_all('div', class_='col-xs-12 col-sm-12 col-xl-6'):
                        x_ans = []
                        for v in u.find_all('div', class_="specification_small_title"):
                            for w in v.find_all('h3'):
                                x = w.get_text()
                            for y in u.find_all('ul'):
                                for z in y.find_all('li'):
                                    i_z = z.find('i').get_text()
                                    s_z = z.find('span').get_text()
                                    if(i_z != 'cancel'):
                                        x_ans.append(s_z)
                                        fspex.update({x: x_ans})
                        if(len(x_ans) != 0):
                            fspex.update({x: x_ans})
                        else:
                            fspex.update({x: False})
            return (fspex)
        else:
            return (None)


# In[15]:


class VIDEO:
    
    def __init__(self,video):
        self.video = video
        
    def Key(self):
        if(self.video):
            key = self.video.find('h2').get_text()
            return (key)
        else:
            return ('Video')
    def Value(self):
        if(self.video):
            if(self.video.find('a')):
                value = self.video.find('a')['href']
            elif(self.video.find('iframe')):
                value = self.video.find('iframe')['src']
            else:
                value = 'None'
            return (value)


# In[8]:


class FEATURES:
    
    def __init__(self,features):
        self.features = features
        
    def Key(self):
        if(self.features):
            key = self.features.find('h2').get_text()
            return (key)
        else:
            return ('Features')
    
    def Value(self):
        if(self.features):
            value=[]
            for i in (self.features.find_all('ul')):
                value.append( (i.find('li')).get_text() )
            return (value)
        else:
            return (None)


# In[9]:


class AWARDS:
    def __init__(self,award_section):
        self.award_section = award_section
        
    def Key(self):
        
        if (self.award_section):
            key = (self.award_section.find('h2').get_text())
            return (key)
        else:
            return ('Awards')
    def Value(self):
        if (self.award_section):
            value = []
            for i in (self. award_section.find_all('img',alt = True) ):
                value.append(i['src'])
                value.append(i['data-src'])
                return (value)
        else:
              return (None)


# In[10]:


class SCREENSHOTS:
    def __init__(self,screenshots):
        self.screenshots = screenshots
        
    def Key(self):
        if (self.screenshots):
            key = (self.screenshots.find('h2')).get_text()
            return (key)
        else:
            return ('Screenshots')

    def Value(self):
        if (self.screenshots):
            value = []
            for i in set(self.screenshots.find_all('a',alt=True)):
                value.append(i['src'])
                value.append(i['data-src'])
            return (value)
        else:
              return (None)


# In[11]:


class OVERVIEW:
    
    def __init__(self,overview):
        self.overview = overview
        
    def Key(self):
        if(self.overview):
            if(self.overview.find('h2').get_text()=='Overview'):
                  return (self.overview.find('h3').get_text())
            else:
                  return ('Overview')

    def Value(self):
        if(self.overview):
            if(self.overview.find('p')):
                  return (self.overview.find('p').get_text())
            else:
                  return (None)


# In[12]:


def NAME(header):
    try:
        if(header):
            if(header.find('h1')):
                name = (header.find('h1')).get_text()
                return (name)
            else:
                name = None
                return Name
    except:
        name = None
        return (name)


# In[13]:


def LOGO(header):
    logo = []
    try:
        if(header):
            if(header.find_all('img')):
                for i in (header.find_all('img',alt=True)):
                        logo.append(i['src'])
                        logo.append(i['data-src'])
                return (logo)
        else:
            logo.append(None)
            return (logo)
    except:
        logo.append("Not found")
        return (logo)


# In[14]:


class BREADCRUMB:
    
    def __init__(self,breadcrumb):
        self.breadcrumb = breadcrumb
    def Category(self):
        cat={}
        if(self.breadcrumb):
            for ul in (self.breadcrumb.find_all('ul')):
                for idx,li in enumerate(ul.find_all('li')):
                    if (idx==1):
                        for a in li.find_all('a'):
                            cat.update({a.get_text():a['href']})
            return cat
        else:
            return {}
    def Software(self):
        sw = {}
        if(self.breadcrumb):
            if(self.breadcrumb):
                for ul in (self.breadcrumb.find_all('ul')):
                    for idx,li in enumerate(ul.find_all('li')):
                        if (idx==2):
                            for a in li.find_all('a'):
                                sw.update({a.get_text():a['href']})
            return sw
        else:
            return {}


# In[ ]:





# In[ ]:





# In[ ]:




