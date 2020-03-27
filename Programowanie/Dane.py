#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

def POBIERZ(path):
    file = open(path,"r")
    for line in file:
        fields = line.split(" ")
        print(fields)
def TASUJ(lista):
    for i in range(len(lista)-1, 0, -1):  
        j = random.randint(0, i + 1)  
        lista[i], lista[j] = lista[j], lista[i]  
def NORMALIZUJ(x):
    min = np.min(x)
    max = np.max(x)
    range = max - min
    return [(a - min) / range for a in x]


# In[ ]:




