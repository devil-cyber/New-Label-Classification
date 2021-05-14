import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def clean_text(text):
    result = re.sub(r'\d+','',text)
    translator = str.maketrans('','',string.punctuation)
    result = result.translate(translator)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(result)
    filtred_text = [word for word in word_tokens if word not in stop_words]
    new_text = ""
    for word in filtred_text:
        new_text =new_text +"  " + word
    return new_text

