#!/usr/bin/env python
# coding: utf-8

# In[319]:


import requests
from bs4 import BeautifulSoup


# In[320]:


path = "D:\\SageIT-DS\\Wi-Fi is an important threat to human health - ScienceDirect.html"
path1 = "D:\\SageIT-DS\\Worldwide decline of the entomofauna_ A review of its drivers - ScienceDirect.html"
path2 = 'D:\\SageIT-DS\\Aluminium in brain tissue in autism - ScienceDirect.html'
path3 = 'D:\\SageIT-DS\\Bleb Formation in Human Fibrosarcoma HT1080 Cancer Cell Line Is Positively Regulated by the Lipid Signalling Phospholipase D2 (PLD2) - ScienceDirect.html'
path4 = "D:\\SageIT-DS\\Structure of Extracellular Polysaccharides (EPS) Produced by Rhizobia and their Functions in Legume–Bacteria Symbiosis_ — A Review - ScienceDirect.html"
path5 = "D:\\SageIT-DS\\Arsenic and Cadmium Contamination in Water, Sediments and Fish is a Consequence of Paddy Cultivation_ Evidence of River Pollution in Sri Lanka - ScienceDirect.html"
path6 = "D:\\SageIT-DS\\Hyperthermia_ Role and Risk Factor for Cancer Treatment - ScienceDirect.html"
path7 = "D:\\SageIT-DS\\Grip Strength and Impact on Cognitive Function in Healthy Kitchen Workers - ScienceDirect.html"
path8 = "D:\\SageIT-DS\\Extracellular_Circulating MicroRNAs_ Release Mechanisms, Functions and Challenges - ScienceDirect.html"
path9 = 'D:\\SageIT-DS\\Sub-acute Ruminal Acidosis (SARA) and its Consequence in Dairy Cattle_ A Review of Past and Recent Research at Global Prospective - ScienceDirect.html'
page = open(path9, 'r',encoding = 'utf-8')
page = (page.read())


# In[321]:


soup = BeautifulSoup(page, 'html.parser')


# In[322]:


article = soup.find('article')
#print(article.prettify())


# In[323]:


#Title Extraction
Title = article.find('span', class_="title-text")
output_title = Title.text
print(output_title)


# In[324]:


#4 cells extraction
Cells = article.find('div')
ouput_cells = Cells.text
print(ouput_cells)


# In[325]:


#Author name
Author = article.find('div', class_ = "wrapper truncated")
ouput_Author = Author.text[31:]
print(ouput_Author)


# In[326]:


#Highlights of the article
#Highlights = article.find('div', class_='abstract author-highlights')
#Highlights_text = Highlights.text
#print(Highlights_text)


# In[327]:


#Abstract of the article
Abstract = article.find('div', "abstract author")
output_Abstract = Abstract.text
print(output_Abstract)


# In[328]:


#Keywords 
Keywords = article.find('div', class_ = 'Keywords u-font-serif')
ouput_Keywords = Keywords.text
print(ouput_Keywords)


# In[329]:


#Freqplot
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


# In[330]:


L1 = sent_tokenize(output_Abstract)
for x in  L1:
    print(x,"\n")


# In[331]:


from nltk.corpus import stopwords
example_sent = output_Abstract

stop_words = set(stopwords.words('english'))
#print(stop_words)


# In[332]:


word_tokens = word_tokenize(output_Abstract)
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

#print(word_tokens)
print(filtered_sentence)


# In[333]:


from nltk.text import Text

stop_words = nltk.corpus.stopwords.words('english')
newStopWords = [',', '.', "?",";","Ca2+","aspects",'&'] # Remove words
stop_words.extend(newStopWords)


# In[334]:


filtered_sentence2 = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence2.append(w)

#print(word_tokens)
print(filtered_sentence2)


# In[335]:


fdist = nltk.FreqDist(filtered_sentence2)
fdist


# In[336]:


from nltk.text import Text
aText = Text(nltk.corpus.gutenberg.words('D:\\SageIT-DS\\HighlightsText.txt'))
fdist = nltk.FreqDist(aText)
stopwords = nltk.corpus.stopwords.words('english')
newStopWords = ['has', ".","?",",","The"]
stopwords.extend(newStopWords)
import matplotlib.pyplot as plt
fdist_no_punc_no_stopwords = nltk.FreqDist(dict((word, freq) for word, freq in fdist.items() if word not in stopwords and word.isalpha()))
fdist_no_punc_no_stopwords.plot(10, cumulative=False, title="10 most common tokens (no stopwords or punctuation)")


# In[337]:


#hapaxes
print(fdist)
output_hapaxes =fdist.hapaxes()
print(output_hapaxes)


# In[338]:


#collocations

ouput_collocations = aText.collocations()
print(ouput_collocations)


# In[339]:


#Visualization using wordcloud
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# In[340]:


f = open("D:\\SageIT-DS\\HighlightsText.txt","r")
#print(f.read())
textContent = f.read()
f.close()

# Open, Read/write , close

wordcloud = WordCloud().generate(textContent)

def plot_wordcloud(wordcloud):
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# In[341]:


plot_wordcloud(wordcloud)


# In[342]:


#Saving into CSV format

Output_list = {'OUTPUT':[output_title,ouput_cells,ouput_Author,output_Abstract,ouput_Keywords,fdist,output_hapaxes,
                         ouput_collocations]}

import csv
print(len(Output_list ))



import pandas as pd
from pandas import DataFrame
df = DataFrame(Output_list, columns= ['OUTPUT'])
df.to_csv("D:\\SageIT-DS\\TextMining-csv\\record10_output.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:





# In[32]:





# In[55]:





# In[34]:





# In[ ]:





# In[ ]:




