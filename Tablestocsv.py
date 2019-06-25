#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tabula
from tabula import read_pdf
from tabula import convert_into


# In[71]:



#path = "C:\\Users\pranavi\\Downloads\\Data_Scientist_Resume_Format1.pdf"
df =tabula.read_pdf("D:\\SageIT-DS\\Srinivas\\1-s2.0-S221439981630011X-main.pdf" ,multiple_tables=True, pages = 'all')
df


# In[2]:


tabula.convert_into("D:\\SageIT-DS\\Srinivas\\1-s2.0-S2542504819300211-main.pdf","D:\\SageIT-DS\\tables-csv\\table15.csv", pages = 'all')


# In[64]:





# In[6]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




