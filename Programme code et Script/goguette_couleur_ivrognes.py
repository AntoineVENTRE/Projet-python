#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Bibliothèques nécessaires 
import sys
import random
import time
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming
from demo_utils import usage 
import os


def usage(msg=""):#indique comment bien renseigner les bons arguments
    print(msg)
    print("Usage : python goguette_color_ivrogne.py <seed> <definition> <connexity> <output_file> "
          "<r1> <v1> <b1> <r2> <v2> <b2> <r3> <v3> <b3>")
    sys.exit(1)   #arrete le programme 


def main():
    # Vérifier le nombre d’arguments
    if len(sys.argv) != 14:
        usage("Il faut 4 argument pour le fonctionement de la fonction et 9 entiers pour les trois couleurs RGB des ivrognes.")
    
    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    filename = sys.argv[4]

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
    n_steps = int((width * height) )  # nombre de pas par ivrogne je n'ai pas divisé par cinq ici pour avoir une image plus remplie
    c1 = (int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    c2 = (int(sys.argv[8]), int(sys.argv[9]), int(sys.argv[10]))
    c3 = (int(sys.argv[11]), int(sys.argv[12]), int(sys.argv[13]))
    ivrogne_colors = [c1,c2,c3]
    
    # Position initiale des 3 ivrognes
    pos = (width//2, height//2)

    # --- Simulation pour chaque ivrogne ---
    for color in ivrogne_colors:
        x, y = pos
        for _ in range(n_steps):
            im.set_color((x, y), color)
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height

    # --- Sauvegarde ---
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()
