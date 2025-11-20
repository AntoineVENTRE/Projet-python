# Dentrite

import sys
import random
import time
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming, usage

def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    output_file = sys.argv[4]

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

    # Recherche du centre de l'image
    xm = width // 2
    ym = height // 2
    im.set_color((xm, ym), (0, 0, 0))
    im._check_coordinate((xm, ym))
    im._check_color((0, 0, 0))
    im._pil_image.putpixel((xm, ym), (0, 0, 0))

    # On définit le nombre d'ivrognes
    n_ivrogne = width * height // 5

    # Remplissage de l'image par marche aléatoire d'ivrognes
    deja_parcouru = [(xm,ym)]  # liste des positions déjà noires


    for _ in range(1, n_ivrogne):
        pos_ivrogne = (random.randint(0, width-1), random.randint(0, height-1))

        if pos_ivrogne in deja_parcouru:  # on s'assure que la position n'est pas déjà noire
            while pos_ivrogne in deja_parcouru:
                pos_ivrogne = (random.randint(0, width-1), random.randint(0, height-1))
        x, y = pos_ivrogne
        #on s'assure que l'ivrogne n'atteri pas voisin d'une position déjà noire
        voisin_proche = [(x, y-1), (x-1, y), (x+1, y), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
        voisin_proche_noir = [pos for pos in voisin_proche if pos in deja_parcouru]
        if pos_ivrogne in voisin_proche_noir:
            while pos_ivrogne in voisin_proche_noir:
                pos_ivrogne = (random.randint(0, width-1), random.randint(0, height-1))
            
        while pos_ivrogne not in deja_parcouru:
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height
            pos_ivrogne = (x, y)
            if pos_ivrogne in deja_parcouru:
                deja_parcouru.append(pos_ivrogne)
                im.set_color(pos_ivrogne, (0, 0, 0))
                im._check_coordinate(pos_ivrogne)
                im._check_color((0, 0, 0))
                im._pil_image.putpixel(pos_ivrogne, (0, 0, 0))
    
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")


if __name__ == "__main__":
    main()
