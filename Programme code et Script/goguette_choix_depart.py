#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Bibliothèques nécessaires 
import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import definition_from_str
from demo_utils import usage
from goguette import marche_ivrogne, goguette

if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 7:
        usage("Erreur : nombre d’arguments incorrect.")

    # Récupération des paramètres
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])
    connexity = sys.argv[3]
    filename = sys.argv[4]
    position_width = int(sys.argv[5])
    position_height = int(sys.argv[6])

    # Initialisation du hasard
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")

    # Création de l'image 
    width, height = definition
    color_fond = (255, 255, 255)
    im = SimpleImage.new(width, height, color_fond)

    # Vérification position
    if not (0 <= position_width < width and 0 <= position_height < height):
        usage(f"Erreur : la position initiale ({position_width}, {position_height}) doit être dans l'image ({width}x{height}).")
    pos = (position_width, position_height)

    # Simulation 
    n_steps = (width * height) // 5
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for color in colors:
        marche_ivrogne(im, pos, n_steps, connexity, color, width, height)

    # Sauvegarde 
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")
