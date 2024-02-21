"""
04 VISUALISATION

Produce a visualisation of the reduciton data
"""
import os
import utils
from PIL import Image
import numpy as np

SRC_FOLDER = os.path.join(os.getcwd(), "output", "embeddings", "fsa_color")
OUT_FOLDER = os.path.join(os.getcwd(), "output", "embeddings", "fsa_color")
WIDTH, HEIGHT = 800, 600

def add_image(full_image, image_path, coordinates):
    x = int(float(coordinates[0]) * WIDTH)
    y = int(float(coordinates[1]) * HEIGHT)

    this_img = Image.open(image_path)
    this_img = this_img.resize((50, 50))
    
    full_image.paste(this_img, (x, y))

def process():
    file_map = utils.read_json(os.path.join(SRC_FOLDER, "file_map.json"))
    coordinates = np.load(os.path.join(SRC_FOLDER, "dim_redux.npy"))

    full_image = Image.new('RGB', (WIDTH, HEIGHT), 'white')

    for i, item in enumerate(coordinates):
        add_image(full_image, file_map[str(i)]["file_path"], item)

    full_image.save(os.path.join(OUT_FOLDER, "visualisation.jpg"))

process()