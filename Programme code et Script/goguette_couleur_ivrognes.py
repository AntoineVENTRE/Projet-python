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
from goguette import creation_image_fond,marche_ivrogne

def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 14 :
        usage("Erreur : nombre d’arguments incorrect.")

    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    filename = sys.argv[4]
    c1 = (int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    c2 = (int(sys.argv[8]), int(sys.argv[9]), int(sys.argv[10]))
    c3 = (int(sys.argv[11]), int(sys.argv[12]), int(sys.argv[13]))

    # --- Initialisation du hasard ---
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")

    # --- Création de l'image ---
    width, height = definition
    color_fond = (255, 255, 255)  # blanc
    im = SimpleImage.new(width,height, color_fond)

    # --- Paramètres ---
    n_steps = int((width * height) / 5) # nombre de pas par ivrogne
    colors_ivrognes = [c1,c2,c3]
    
    # Position initiale des 3 ivrognes
    pos = (width//2, height//2)

    # --- Simulation pour chaque ivrogne ---
    for color in colors_ivrognes :
        im = marche_ivrogne(im, pos, n_steps, connexity, color,width,height)

    # --- Sauvegarde ---
    os.makedirs("Images", exist_ok=True)     # garantit que le dossier existe
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()
