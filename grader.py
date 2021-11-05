import numpy as np
from tensorflow.keras.models import load_model
import math
from model import *
from helpers import *

def getGrade(essay):
    if len(essay.split()) > 50:
        num_features = 300
        model = word2vec.KeyedVectors.load_word2vec_format('word2vecmodel.bin', binary=True)
        clean_test_essay = []  
        clean_test_essay.append(essay_to_wordlist( essay, remove_stopwords=True ))
        testDataVecs = getAvgFeatureVecs( clean_test_essay, model, num_features )
        testDataVecs = np.array(testDataVecs)
        testDataVecs = np.reshape(testDataVecs, (testDataVecs.shape[0], 1, testDataVecs.shape[1]))
        lstm_model = load_model('final_model')

        preds = lstm_model.predict(testDataVecs)

        if (math.isnan(preds)) or (preds < 0):
            return 0
        else:
            return int(np.around(preds)[0][0])
            
    else:
        return 0

def gradeMe(essay):
    score = getGrade(essay)
    return score