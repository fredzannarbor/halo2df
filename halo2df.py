import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import argparse 
import numpy as np
from wordcloud import WordCloud, STOPWORDS

df = pd.DataFrame()

# reads csvs into DataFrames

for filepath in glob.iglob(r'Amazon Health Data/Tone/ToneUtterances*.csv'):
    print(filepath)
    t = pd.read_csv(filepath)
    
for filepath in glob.iglob(r'Amazon Health Data/Tone/ToneSessions*.csv'):
    print(filepath)
    s = pd.read_csv(filepath)


# reports on each dataframe

text = t['Descriptors'].values

def convertTuple(tup): 
    remove = ['[', ']']
    original_string =  ', '.join(tup)
    new_string = original_string
    for character in remove:
        #print(remove)
        new_string = new_string.replace(character, "")
    str = new_string
    return str

#print(convertTuple(text))

wordcloud = WordCloud(
    width = 1024,
    height = 768,
    background_color = 'black',
    stopwords = STOPWORDS).generate(str(text))
fig = plt.figure(
    figsize = (20, 15),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
fig.savefig('ToneUtterancesCloud')

print(' ')
print('Positivity stats')
s['Positivity'].hist()
print(s['Positivity'].describe())

