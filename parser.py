#!/usr/bin/env python
# coding: utf-8

# In[20]:


import json 
import pandas as pd
import os


# In[21]:


true = 'true'
false = 'false'
null = 'null'


# In[37]:


cols = ['Category','Category_Url','Name','Url','About','Screenshots','Awards','Features','Deployment',
       'Api','Business','Available Support','Company Name','Website','Headquarter','Full Address','Description','Pricing']
ndf = pd.DataFrame(columns = cols)
external_path = '/home/jordi/Jsons/'


# In[23]:


# def collected_jsons(path):
#     file_names = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
#     loaded_jsons = []
#     software_name = []
#     file_urls = []
#     final_dic = {}
#     for file in file_names:
#         with open(path+file) as temp:
#             temp = json.load(temp)
#         td = temp['Software']
#         for k,v in td.items():
#             software_name.append(k)
#             file_urls.append(v)
#             final_dic.update({k:v})
#     return (loaded_jsons)


# In[24]:


file_names = [pos_json for pos_json in os.listdir(external_path) if pos_json.endswith('.json')]


# In[25]:


len(file_names)


# In[31]:


class parser:
  def __init__ (self,D):
    self.D = D
    self.keys_list = [k for k,v in self.D.items()]
  def cat_name(self):
    td = self.D['Category']
    for k,v in td.items():
      temp = k
    return (temp)
  def cat_url(self):
    td = self.D['Category']
    for k,v in td.items():
      temp = v
    return (temp)
  def product_name(self):
    td = self.D['Software']
    for k,v in td.items():
      temp = k
    return (temp)
  def product_url(self):
    td = self.D['Software']
    for k,v in td.items():
      temp = v
    return (temp)
  def about(self):
    for key in self.keys_list:
      if ('About' in key):
        temp = self.D[key]
    return (temp)
  def screenshots(self):
    for key in self.keys_list:
      if ('Screenshots' in key):
        temp = self.D[key]
    return (temp)
  def awards(self):
    for key in self.keys_list:
      if ('Awards' in key):
        temp = self.D[key]
    return (temp)
  def features(self):
    for key in self.keys_list:
      if ('Features' in key):
        temp = self.D[key]
    return (temp)
  def deployment(self):
    for key in self.keys_list:
      if ('Specifications' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if('Deployment' in tdk):
            temp = td[tdk]
    return (temp)
  def Api(self):
    for key in self.keys_list:
      if ('Specifications' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if('Api' in tdk):
            temp = td[tdk]
    return (temp)
  def business(self):
    flag = 0
    for key in self.keys_list:
      if('Users' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if ('Business' in tdk):
            temp = td[tdk]
            temp2 = []
            for i in temp:
              j = i.replace('\n','')
              temp2.append(j)
    return (temp2)
  def available_support(self):
    for key in self.keys_list:
      if ('Users' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if ('Available Support' in tdk):
            temp = td[tdk]
            temp2 = []
            for i in temp:
              j = i.replace('\n','')
              temp2.append(j)
    return (temp2)
  def company_name(self):
    for key in self.keys_list:
      if ('Company Details' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if ('Company Name' in tdk):
            temp = td[tdk]
    return (temp)
  def company_website(self):
    flag = 0
    for key in self.keys_list:
      if ('Company Details' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if ('Website' in tdk):
            flag = flag+1
            temp = td[tdk]
    if (flag!=0):
      return (temp)
    else:
      return ('N/A')
  def company_headquarter(self):
    flag = 0
    for key in self.keys_list:
      if ('Company Details' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if ('Headquarter' in tdk):
            flag = flag+1
            temp = td[tdk]
    if (flag!=0):
      return (temp)
    else:
      return ('N/A')
  def full_address(self):
    flag = 0
    for key in self.keys_list:
      if ('Company Details' in key):
        td = self.D[key]
        for tdk in [k for k,v in td.items()]:
          if ('Full Address' in tdk):
            flag = flag+1
            temp = td[tdk]
    if (flag!=0):
      return (temp)
    else:
      return ('N/A')
  def description(self):
    flag = 0
    for key in self.keys_list:
      if ('Description') in key:
        flag = flag+1
        temp = self.D[key]
    if (flag!=0):
      return (temp)
    else:
      return ('N/A')
  def pricing(self):
    flag = 0
    for key in self.keys_list:
      if ('Pricing' in key):
        flag = flag +1
        temp = self.D[key]
        temp = str(temp)
    if (flag!=0):
      return (temp)
    else:
      return ("N/A")


# In[27]:


# anms = []
loaded_jsons = []
for file in file_names:
    with open(external_path+file) as temp:
        temp = json.load(temp)
    loaded_jsons.append(temp)
print(len(loaded_jsons))
print(type(loaded_jsons[0]))
print(loaded_jsons[1])


# In[38]:


anms=[]
for i,file in enumerate(loaded_jsons):
    try:
      one = parser(file)
      ndf.at[i,'Category'] = one.cat_name()
      ndf.at[i,'Category_Url'] = one.cat_url()
      ndf.at[i,'Name'] = one.product_name()
      ndf.at[i,'Url'] = one.product_url()
      ndf.at[i,'About'] = one.about()
      ndf.at[i,'Screenshots'] = one.screenshots()
      ndf.at[i,'Awards'] = one.awards()
      ndf.at[i,'Features'] = one.features()
      ndf.at[i,'Deployment'] = one.deployment()
      ndf.at[i,'Api'] = one.Api()
      ndf.at[i,'Business'] = one.business()
      ndf.at[i,'Available Support'] = one.available_support()
      ndf.at[i,'Company Name'] = one.company_name()
      ndf.at[i,'Website'] = one.company_website()
      ndf.at[i,'Headquarter'] = one.company_headquarter()
      ndf.at[i,'Full Address'] = one.full_address()
      ndf.at[i,'Description'] = one.description()
      ndf.at[i,'Pricing'] = one.pricing()
    except:
        print(i)
        anms.append(file)


# In[ ]:


# df.at[0,'Category'] = one.cat_name()
# df.at[0,'Category_Url'] = one.cat_url()
# df.at[0,'Name'] = one.product_name()
# df.at[0,'Url'] = one.product_url()
# df.at[0,'About'] = one.about()
# df.at[0,'Screenshots'] = one.screenshots()
# df.at[0,'Awards'] = one.awards()
# df.at[0,'Features'] = one.features()
# df.at[0,'Deployment'] = one.deployment()
# df.at[0,'Api'] = one.Api()
# df.at[0,'Business'] = one.business()
# df.at[0,'Available Support'] = one.available_support()
# df.at[0,'Company Name'] = one.company_name()
# df.at[0,'Website'] = one.company_website()
# df.at[0,'Headquarter'] = one.company_headquarter()
# df.at[0,'Full Address'] = one.full_address()
# df.at[0,'Description'] = one.description()
# df.at[0,'Pricing'] = one.pricing()


# In[35]:


print(len(anms))


# In[39]:


# len(file_names)
ndf


# In[46]:


ndf.to_csv('Saare Products.csv')


# In[45]:


anms[1]


# In[ ]:




