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
WIDTH, HEIGHT = 10000, 10000
PADDING = 1000
IMAGE_ZOOM = 0.25

def add_image(full_image, image_path, coordinates):
    x = int(float(coordinates[0]) * WIDTH)
    y = int(float(coordinates[1]) * HEIGHT)

    this_img = Image.open(image_path)

    original_width, original_height = this_img.size
    w = int(original_width * IMAGE_ZOOM)
    h = int(original_height * IMAGE_ZOOM)

    x = int(x - (w * 0.5))
    y = int(y - (h * 0.5))

    x = int(utils.scale(x, 0, WIDTH, PADDING, WIDTH - (PADDING * 2)))
    y = int(utils.scale(y, 0, HEIGHT, PADDING, HEIGHT - (PADDING * 2)))

    this_img = this_img.resize((w, h))
    
    full_image.paste(this_img, (x, y))

def process():
    file_map = utils.read_json(os.path.join(SRC_FOLDER, "file_map.json"))
    coordinates = np.load(os.path.join(SRC_FOLDER, "dim_redux.npy"))

    full_image = Image.new('RGB', (WIDTH, HEIGHT), 'white')

    for i, item in enumerate(coordinates):
        add_image(full_image, file_map[str(i)]["file_path"], item)

    full_image.save(os.path.join(OUT_FOLDER, "visualisation.jpg"))

process()