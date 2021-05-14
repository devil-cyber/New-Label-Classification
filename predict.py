from train import Train
import matplotlib.pyplot as plt
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import *
import numpy as np

def predict(text):
    model = load_model('./news.h5')
    tokenizer=Tokenizer(num_words=VOCAB_SIZE,oov_token=OOV_TOK)
    tokenizer.fit_on_texts(text)
    sequence = tokenizer.texts_to_sequences(text)
    padded = pad_sequences(sequence,maxlen=MAX_LENGTH)
    pred = model.predict(padded)
    val = pred.tolist()
    print(val[0][4],'hi')
    #labels = ['sport', 'bussiness', 'politics', 'tech', 'entertainment','unknown']
    labels = ['tech','sport','world','business','unknown']
    proba = {labels[0]:str(val[0][0]*100)+'%',
             labels[1]:str(val[0][1]*100)+'%',
             labels[2]:str(val[0][2]*100)+'%',
             labels[3]:str(val[0][3]*100)+'%',
             labels[4]:str(val[0][4]*100)+'%',
             }
    print(proba)
    return (pred, labels[np.argmax(pred)],proba)

