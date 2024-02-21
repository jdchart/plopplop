"""
03 CLUSTERING

Get n number of clusters from dimensionality reduction data.
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import random
import utils
from sklearn.cluster import KMeans

SRC_FOLDER = os.path.join(os.getcwd(), "output", "embeddings", "fsa_color")
OUT_FOLDER = os.path.join(os.getcwd(), "output", "embeddings", "fsa_color")
NUM_CLUSTERS = 3
VISUALIZE = True

def cluster(data, num_clusters = 4):
    kmeans = KMeans(n_clusters = num_clusters, random_state=0) 
    clustered = kmeans.fit(data) 

    # kmeans.cluster_centers_
    # kmeans.predict([[0, 0], [12, 3]])

    return clustered.labels_

def get_colour_map(clusters):
    ret = {}
    used = []
    for item in clusters:
        if item not in used:
            ret[str(item)] = (random.random(), random.random(), random.random())
            used.append(item)
    return ret

def scatter_vis_colour(data, clusters, colour_map):
    transposed = np.transpose(data)
    col = []
    for item in clusters:
        col.append(colour_map[str(item)])

    plt.scatter(transposed[0], transposed[1], c=col)
    plt.show()

def process():
    original_data = np.load(os.path.join(SRC_FOLDER, "dim_redux.npy"))
    file_map = utils.read_json(os.path.join(SRC_FOLDER, "file_map.json"))

    clusters = cluster(original_data, NUM_CLUSTERS)
    colour_map = get_colour_map(clusters)
    
    print(clusters)

    for i, clus in enumerate(clusters):
        file_map[str(i)]["cluster"] = int(clus)

    if VISUALIZE:
        scatter_vis_colour(original_data, clusters, colour_map)

    utils.write_json(os.path.join(OUT_FOLDER, "file_map.json"), file_map)

process()