import spacy
from spacy.training.example import Example
import pickle
import random, os
import sys
import fitz

def traindata(file_name):
    nlp_model = spacy.load('resume_analysis/nlp_model')
    train_data = pickle.load(open(f'train_data.pkl', 'rb'))
    doc = nlp_model(train_data[0][0])
    # for ent in doc.ents:
    #     print(f'{ent.label_.upper():{30}}- {ent.text}')
    fname = file_name
    doc = fitz.open(fname)
    text = ""
    for page in doc:
        text = text + str(page.getText())
    tx = " ".join(text.split('\n'))

    doc = nlp_model(tx)
    label = []
    value = []
    for ent in doc.ents:
        if ent.label_.upper() not in label:
            label.append(ent.label_.upper())
            value.append(ent.text)
        print(f'{ent.label_.upper():{30}}- {ent.text}')
    return label, value