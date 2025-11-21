#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Bibliothèques nécessaires
import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming
from demo_utils import usage
from goguette import creation_image_fond,marche_ivrogne

def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 5:
        print("Usage: goguette.py <seed> <definition> <connexity> <output>")
        sys.exit(1)

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
    couleur = (255, 255, 255)  # blanc
    im = creation_image_fond(width, height, couleur)

    # --- Paramètres ---
    n_pas = int((width * height) / 5)  # nombre de pas par ivrogne
    
    # --- Position de départ : centre de l'image ---
    pos = (width // 2, height // 2)

    # --- Simulation pour chaque ivrogne ---
    for i in range(3):      #3 ivrognes comme dans les autres codes
        couleur = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        im = marche_ivrogne(im, pos, n_pas, connexity, couleur)

    # --- Sauvegarde ---
    os.makedirs("Images", exist_ok=True)     # garantit que le dossier existe
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()
