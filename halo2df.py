import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import argparse 
import numpy as np
from wordcloud import WordCloud, STOPWORDS

df = pd.DataFrame()

for filepath in glob.iglob(r'Amazon Health Data/Tone/ToneUtterances*.csv'):
    print(filepath)
    t = pd.read_csv(filepath)
    print(t)

print('read Halo data and created dataframe')

text = t['Descriptors'].values

def convertTuple(tup): 
    remove = ['[', ']']
    original_string =  ', '.join(tup)
    new_string = original_string
    for character in remove:
        print(remove)
        new_string = new_string.replace(character, "")
    str = new_string
    return str

print(convertTuple(text))

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    background_color = 'black',
    stopwords = STOPWORDS).generate(str(text))
fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
fig.savefig('ToneUtterancesCloud')