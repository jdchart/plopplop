"""
02 DIMENSIONALITY REDUCTION

Perform dimensionality reduction on a set of embedding data.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

SRC_FOLDER = os.path.join(os.getcwd(), "output", "embeddings", "fsa_color")
OUT_FOLDER = os.path.join(os.getcwd(), "output", "embeddings", "fsa_color")
STAND = True
NORM = True
VISUALIZE = True

def normalize(data):
    return MinMaxScaler((0, 1)).fit_transform(data)

def standardize(data):
    return StandardScaler().fit_transform(data)

def dimensionality_reduction(data, dims = 2):
    reductor = TSNE(n_components = dims, perplexity=10)
    reduced = reductor.fit_transform(data)
    return reduced

def scatter_vis(data):
    transposed = np.transpose(data)
    plt.scatter(transposed[0], transposed[1])
    plt.show()

def process():
    original_data = np.load(os.path.join(SRC_FOLDER, "embeddings.npy"))
    
    if STAND:
        original_data = standardize(original_data)
    
    original_data = dimensionality_reduction(original_data)

    if NORM:
        original_data = normalize(original_data)

    print(original_data)
    np.save(os.path.join(OUT_FOLDER, "dim_redux.npy"), original_data)

    if VISUALIZE:
        scatter_vis(original_data)

process()