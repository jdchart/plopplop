"""
01 IMAGES TO IIIF

Convert a folder of images to IIIF Manifests.
"""
import os
import utils

SRC_FOLDER = os.path.join(os.getcwd(), "sources", "fsa_color", "images")

def process():
    sources = utils.collect_files(SRC_FOLDER, ["jpg"])
    print(f"Treating {len(sources)} image files...")

process()