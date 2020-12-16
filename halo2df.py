import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import argparse 
import numpy as np
from wordcloud import WordCloud, STOPWORDS

df = pd.DataFrame()

datafiles = {'tone_utterances':'Amazon Health Data/Tone/ToneUtterances*.csv', 'tone_sessions': 'Amazon Health Data/Tone/ToneSessions*.csv', 'activity_daily': 'Amazon Health Data/Activity/Activity_DailyData*.csv', 'activity_raw': 'Amazon Health Data/Activity/Activity_Raw*.csv', 'activity_work': 'Amazon Health Data/Activity/Activity_Work*.csv'}



# reads csvs into DataFrames

dflist = {}
for x, y in datafiles.items():
    print(x)
    print(glob.glob(y)[0])
    a = glob.glob(y)[0]
    dflist[x] = pd.read_csv(a)

# reports on each dataframe

text = dflist['tone_utterances']['Descriptors'].values

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
dflist['tone_sessions']['Positivity'].hist()
print(dflist['tone_sessions']['Positivity'].describe())

