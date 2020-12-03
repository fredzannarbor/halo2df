# halo2df
_Loads Amazon Halo user data into Pandas dataframe &amp; runs analysis_

The script will iterate over your personal health data, import each dataset into an appropriate dataframe, and carry out some analysis.

Version 1.0 of this script  analyzes only the Tone Utterance data and turns it into a wordcloud. Future versions will support other data sets and carry out other visualizations.

## Requirements

Python > 3 and < 3.9 until pandas and matplotlib are stable for Python 3.9 and above.

## Installation

1.  git clone to a new working directory (halo2df).

2.  In that directory, pip install -r requirements.txt.  This will install several libraries including pandas and matplotlib.

### Setup

1. Request your latest Amazon Health Data from the Halo app on your phone -- see Settings > Download Health Data.

2. Unzip the resulting file into the same directory as this script.

3.  Run the script:

**halo2df.py**

4. The output will include a wordcloud of your Tone Utterances called ToneUtterancesCloud.png, located in the current directory.
