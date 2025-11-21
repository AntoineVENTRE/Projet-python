# Dentrite
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

def voisinage_8(pos):
    """Retourne les 8 positions voisines d'un pixel."""
    x, y = pos
    return [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),           (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]

def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

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

    # Recherche du centre de l'image
    xm = width // 2
    ym = height // 2
    im.set_color((xm, ym), (0, 0, 0))
  
    # On définit le nombre d'ivrognes
    n_ivrogne = width * height // 5

    # Remplissage de l'image par marche aléatoire d'ivrognes
    deja_parcouru = [(xm,ym)]  # liste des positions déjà noires

    for i in range(1, n_ivrogne):
        # Position de départ aléatoire
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        
        # Marche aléatoire jusqu'à rencontrer un voisin noir
        while True:
            # Vérifier les 8 voisins
            voisins = voisinage_8((x, y))
            if any((vx % width, vy % height) in deja_parcouru for vx, vy in voisins):
                im.set_color((x, y), (0, 0, 0))
                deja_parcouru.append((x, y))
                break

            # Sinon avancer aléatoirement
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height

    # --- Sauvegarde ---
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    os.makedirs("Images", exist_ok=True)
    print(f"Image enregistrée sous {output_file}")
    os.startfile(output_file)


if __name__ == "__main__":
    main()
