import numpy as np
import pandas as pd
from joblib import load

def predictor(data):
    intancia = pd.DataFrame([data])
    print(intancia)
    clf = load('meu_modelo.pkl')

    pred = clf.predict(intancia)[0]
    probas = clf.predict_proba(intancia)[0]

    print(probas)

    if int(pred):
        return "Você sobreviveria!"
    else:
        return "Você morreria =()"
    