#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Bibliothèques nécessaires 
import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import connected_roaming, get_random_xy, definition_from_str, WEIGHTED_DEPS,positive_int_from_str
from demo_utils import usage,fill_with_color
from goguette import goguette
from fonction_utile import marche_ivrogne_goguette

if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 14:
        usage("Erreur : nombre d’arguments incorrect.")

    # Récupération des paramètres 
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])
    connexity = sys.argv[3]
    filename = sys.argv[4]
    c1 = (int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    c2 = (int(sys.argv[8]), int(sys.argv[9]), int(sys.argv[10]))
    c3 = (int(sys.argv[11]), int(sys.argv[12]), int(sys.argv[13]))

    # Initialisation du hasard
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")

    # Création de l'image
    width, height = definition
    color_fond = (255, 255, 255)
    im = SimpleImage.new(width, height)
    fill_with_color(im, color_fond)

    # Simulation avec goguette personnalisée 
    colors_ivrognes = [c1, c2, c3]
    pos = (width // 2, height // 2)
    n_steps = (width * height) // 5

    for color in colors_ivrognes:
        marche_ivrogne_goguette(im, pos, n_steps, connexity, color, width, height)

    # Sauvegarde 
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")
 

