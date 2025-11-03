#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Bibliothèques nécessaires 
import sys
import random
import time
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming

def usage(msg=""):#indique comment bien renseigner les bons arguments
    print(msg)
    print("Usage : python goguette_color_ivrogne.py <seed> <definition> <connexity> <output_file> <position_width> <position_height> ")
    sys.exit(1)   #arrete le programme 


def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 7:
        print("Usage: goguette.py <seed> <definition> <connexity> <output>")
        sys.exit(1)

    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    output_file = sys.argv[4]
    position_width =  int(sys.argv[5])
    position_height = int(sys.argv[6])



    # --- Initialisation du hasard ---
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")

    # --- Création de l'image ---
    width, height = definition
    im = SimpleImage.new(width, height)
    for x in range(width):
        for y in range(height):
            im.set_color((x, y), (255, 255, 255))

    # --- Paramètres ---
    n_steps = int((width * height) / 5)  # nombre de pas par ivrogne
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # R, G, B

    # --- Position de départ : centre de l'image ---
    if not (0 <= position_width < width and 0 <= position_height < height):
        usage(f"Erreur : la position initiale ({position_width}, {position_height}) doit être dans l'image ({width}x{height}).")
    pos = (position_width, position_height)

    # --- Simulation pour chaque ivrogne ---
    for color in colors:
        x, y = pos
        for _ in range(n_steps):
            im.set_color((x, y), color)
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height

    # --- Sauvegarde ---
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()
