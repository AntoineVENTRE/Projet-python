#Dentrite
# Dentrite
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming
from demo_utils import usage
from goguette import creation_image_fond

def voisinage_8(pos):
    x, y = pos
    return [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),             (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]

def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")
    
    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])
    connexity = sys.argv[3]
    filename = sys.argv[4]

    # --- Initialisation du hasard ---
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")

    #Paramètres 
    width, height = definition
    im = creation_image_fond(width, height, (255, 255, 255))

    # Pixel central noir
    xm = width // 2
    ym = height // 2
    im.set_color((xm, ym), (0, 0, 0))

    # Liste des pixels noirs
    deja_parcouru = [(xm, ym)]

    #Nombre ivrognes
    n_ivrogne = width * height//5

    # Limite anti-boucle infinie
    pas_max = width * height*10

    recherche_max = width * height

    for i in range(1, n_ivrogne):
        recherche_points = 0
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        voisins = voisinage_8((x, y))
        while True:
            recherche_points += 1
            if recherche_points > recherche_max:
                break     # abandon du point de départ

            x, y = random.randint(0, width-1), random.randint(0, height-1)

            if (x, y) in deja_parcouru:
                continue

            if any(v in deja_parcouru for v in voisins_toriques):
                continue

            break

        
        pas = 0
        while pas < pas_max :

            # Vérifie si l’un des voisins est noir
            voisins = voisinage_8((x, y))
            if any((vx % width, vy % height) in deja_parcouru for vx, vy in voisins):
                im.set_color((x, y), (0, 0, 0))
                deja_parcouru.append((x, y))
                break



            # Avance aléatoirement
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height

            pas += 1

        # Si l’ivrogne abandonne, on passe au suivant
        # (pour éviter blocage total)

    # Sauvegarde
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)

    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()