<<<<<<< HEAD
# Dendrite.py
=======
#Dentrite
>>>>>>> 7c20b47c7cd2a16f325df0df66380cecb7756460

import sys
import random
import time
from simple_image import Image as SimpleImage
<<<<<<< HEAD
from utils import definition_from_str, connected_roaming, usage


def est_voisin_noir(pos, noirs, connexity):
    """Retourne True si un des voisins de pos est noir."""
    x, y = pos
    if connexity == "4-connected":
        voisins = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    else:
        voisins = [(x+i, y+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0)]
    return any(v in noirs for v in voisins)
=======
from utils import definition_from_str, connected_roaming
from demo_utils import usage
import os
>>>>>>> 7c20b47c7cd2a16f325df0df66380cecb7756460


def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
<<<<<<< HEAD
    definition = definition_from_str(sys.argv[2])
    connexity = sys.argv[3]
    output_file = sys.argv[4]
=======
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    filename = sys.argv[4]
>>>>>>> 7c20b47c7cd2a16f325df0df66380cecb7756460

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
<<<<<<< HEAD

    # --- Point de départ : germe central ---
    xm, ym = width // 2, height // 2
    im.set_color((xm, ym), (0, 0, 0))
    deja_parcouru = [(xm, ym)]

    # --- Nombre d'ivrognes ---
    n_ivrogne = width * height // 5

    # --- Marche des ivrognes ---
    for _ in range(n_ivrogne):
        # Position de départ : ni noire, ni voisine d’un noir
        while True:
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            if (x, y) not in deja_parcouru and not est_voisin_noir((x, y), deja_parcouru, connexity):
                break

        # L’ivrogne marche jusqu’à toucher un voisin noir
        while not est_voisin_noir((x, y), deja_parcouru, connexity):
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height

        # L’ivrogne devient noir (croissance)
        deja_parcouru.append((x, y))
        im.set_color((x, y), (0, 0, 0))

    # --- Sauvegarde ---
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")


if __name__ == "__main__":
    main()
=======
    
    #recherche du centre de l'imagine
    xm=width//2
    ym=height//2
    im.set_color((xm,ym), (0,0,0))
    im._check_coordinate((xm,ym))
    im._check_color((0,0,0))
    im._pil_image.putpixel((xm,ym), (0,0,0))

    #on défini le nombre d'ivrogne
    n_ivrogne = width*height//5

    #remplissage de l'image par marche aléatoire d'ivrogne
    deja_parcouru=[] #liste des positions déjà noires
    
    pos_ivrogne = (xm,ym)

    while pos_ivrogne not in deja_parcouru :
        deja_parcouru.append(pos_ivrogne)
        im.set_color(pos_ivrogne, (0,0,0))
        im._check_coordinate(pos_ivrogne)
        im._check_color((0,0,0))
        im._pil_image.putpixel(pos_ivrogne, (0,0,0))
        x, y = connected_roaming((x, y), type=connexity)
        x %= width
        y %= height
        pos_ivrogne=(x,y)
    
    for _ in range(1,n_ivrogne):
        pos_ivrogne=(random.randint(0,width-1),random.randint(0,height-1))   #cal limite si width = 150 alors ca fonctionne pas 
        
        if pos_ivrogne in deja_parcouru: #on s'assure que la position n'est pas déjà noire
            while pos_ivrogne in deja_parcouru:
                pos_ivrogne=(random.randint(0,width-1),random.randint(0,height-1))
        
        while pos_ivrogne not in deja_parcouru :
            deja_parcouru.append(pos_ivrogne)
            im.set_color(pos_ivrogne, (0,0,0))
            im._check_coordinate(pos_ivrogne)
            im._check_color((0,0,0))
            im._pil_image.putpixel(pos_ivrogne, (0,0,0))
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height
            pos_ivrogne=(x,y)
    
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()
        
>>>>>>> 7c20b47c7cd2a16f325df0df66380cecb7756460
