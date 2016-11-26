import os
import pickle

def save(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

def load(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

