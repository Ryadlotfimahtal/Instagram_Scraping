"""
@Ryad Lotfi MAHTAL

This script aim to process and clean the subject given.
"""
from nltk.corpus import stopwords
import re

#nltk.download('stopwords') #to download the first time à INCLURE dans requirements.TXT ou dans le readme 


#nettoyage du texte 
stopwords =  stopwords.words('french')

punctuations = r'''!()[]{};:'"\,<>.-+/?@#$%^&*_~'''


def clean_text(
    string: str,
    punctuations = punctuations,
    stop_words = stopwords) -> str:

    #numbers

    #string = re.sub(r'[0-9]+', '', string)

    #Removing the punctuations
    for x in string.lower():
      if x in punctuations:
        string = string.replace(x,"")

    # Converting the text to lower
    #string = string.lower()

    #stop_words
    string = ' '.join([word for word in string.split() if word not in stop_words])

    #Cleaning the whitespaces
    string = re.sub(r'\s', ' ', string).strip()
    string_list = string.split()
    return string_list
