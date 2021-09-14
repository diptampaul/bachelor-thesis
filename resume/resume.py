import spacy
from spacy.training.example import Example
import pickle
import random

train_data = pickle.load(open('train_data.pkl', 'rb'))
train_data


nlp = spacy.blank('en')

def train_model(train_data):
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe('ner', last=True)
    for _, annotation in train_data:
        for ent in annotation['entities']:
            ner.add_label(ent[2])

    #Prepare the data

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):     #Only train NER
        optimizer = nlp.begin_training()
        for itn in range(10):
            print("Starting iteration "+str(itn))
            random.shuffle(train_data)
            losses = {}
            index = 0

            
            for text, annotation in train_data:
                try:
                    doc = nlp.make_doc(text)
                    example = Example.from_dict(doc, annotation)
                    nlp.update(
                        [example],   #batch of Example objects
                        drop = 0.2,
                        sgd = optimizer,
                        losses = losses
                    )
                #     nlp.update(
                #         [text],   #Batch of texts
                #         [annotation],   #Batch of annotations
                #         drop = 0.2,
                #         sgd = optimizer,
                #         losses = losses
                #     )
                except Exception as e:
                    #print(e)
                    pass
                
            print('losses')
            print(losses)

#Training the model
train_model(train_data)

#Storing the trained NLP model

nlp.to_disk('nlp_model')