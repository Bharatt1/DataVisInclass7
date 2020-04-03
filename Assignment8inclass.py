#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import os


# In[10]:


import matplotlib.pyplot as plt
import numpy as np


# In[11]:


df = pd.read_csv(r"C:\Users\\Brian\Coronavirus_April1.csv")
df.head()


# In[21]:


axis1 = df.boxplot(by= 'Country_Region', column='Deaths')
axis1.set_ylim(0,1000)

