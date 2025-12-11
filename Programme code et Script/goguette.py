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
from fonction_utile import marche_ivrogne

def goguette(im, n_ivrognes, connexity, width, height):
    """Fonction principale "goguette" avec plusieurs ivrognes."""
    # Nombre de pas par ivrogne (1/5 de la surface)
    n_steps = (width * height) // 5
    # Couleurs des ivrognes
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    # Position de départ : centre
    pos = (width // 2, height // 2)

    # Simulation pour chaque ivrogne
    for color in colors:
        marche_ivrogne(im, pos, n_steps, connexity, color, width, height)


if __name__ == "__main__":
    # Vérification des arguments 
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # Récupération des paramètres 
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    filename = sys.argv[4]

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

    # Appel de la fonction goguette
    goguette(im, n_ivrognes=3, connexity=connexity, width=width, height=height)

    # Sauvegarde 
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")
