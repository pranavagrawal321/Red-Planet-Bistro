import numpy as np
import pandas as pd

import spacy

nlp = spacy.load("en_core_web_sm")


def details(request):
    doc = nlp(request.lower())
    food = []
    food_details = {}
    for token in doc:
        if token.pos_ == 'NUM' or token.pos_ == 'NOUN' or token.pos_ == 'ADJ' and token.text in ["regular", "medium",
                                                                                                 "large", "full",
                                                                                                 "half"]:
            food.append(token)

    ''.join([token.text_with_ws for token in food])

    j = -1
    for i in range(len(food)):
        food_item = ""
        if str(food[i]).isnumeric() and j == -1:
            j = i

        elif (str(food[i]).isnumeric() and j != -1) :
            for f in food[j + 1:i]:
                food_item += str(f) + " "
            food_details[food_item] = food[j]
            j = i
        elif (i == len(food) - 1):
            for f in food[j + 1:]:
                food_item += str(f) + " "
            food_details[food_item] = food[j]
    return food_details



import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")

import json

document = []
matcher = []
intents = json.loads(open("intents.json").read())
for intent in intents['intents']:
    for pattern in intent['patterns']:
        document.append([pattern, intent['tag']])
        matcher.append(pattern)



def sentence_embedding(sentences):  # sentences must be a list

    preprocessed = bert_preprocess(sentences)
    return bert_encoder(preprocessed)['pooled_output']



from sklearn.metrics.pairwise import cosine_similarity


def detect_intent(request):  # request must be a list
    sentences = request + matcher
    ans = -1
    embeddings = sentence_embedding(sentences)
    for i in range(1, len(embeddings)):

        if i == 1:
            best_match = curr = cosine_similarity([embeddings[0]], [embeddings[i]])
            ans = i

        else:
            curr = cosine_similarity([embeddings[0]], [embeddings[i]])

        if (best_match != max(best_match, curr)):
            best_match = curr
            ans = i

    order_type = ""

    for j in range(len(document)):
        if document[j][0] == sentences[ans]:
            order_type = document[j][1]
    return order_type


# detect_intent(["I want 3 choco brownies please"])

final_bill = []


def primary_order(request):
    details(request)
