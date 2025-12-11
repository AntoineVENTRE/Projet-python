#!/usr/bin/env python3
import sys
import random
import os
import time
from utils import connected_roaming, get_random_xy, definition_from_str, WEIGHTED_DEPS,positive_int_from_str
from simple_image import Image
from demo_utils import usage,fill_with_color
from fonction_utile import decode_args,position_depart_valide,marche_ivrogne_dendrite

def dendrite(im, nb_ivrognes, connex):
    """
    Simule la croissance d'une dendrite.
    Le nombre d'ivrognes est 1/5 du nombre total de pixels.
    Utilisation d'un set pour les points noirs pour des recherches rapides.
    """
    width, height = im.width, im.height

    # Ensemble des points noirs
    points_noirs = set()

    # Placer le germe central
    centre = (width // 2, height // 2)
    points_noirs.add(centre)
    im.set_color(centre, (0, 0, 0))

    # Déposer les ivrognes un par un
    for _ in range(nb_ivrognes):
        # 1) Trouver une position de départ valide
        pos_depart = position_depart_valide(im, connex, points_noirs)

        # Vérifier que la position de départ existe
        if pos_depart is None:
            continue

        # 2) Faire marcher l'ivrogne jusqu'à proximité d'un point noir
        pos_arrivee = marche_ivrogne_dendrite(im, pos_depart, connex, points_noirs)

        # 3) Ajouter le point noir si nécessaire
        if pos_arrivee is not None and pos_arrivee not in points_noirs:
            points_noirs.add(pos_arrivee)
            im.set_color(pos_arrivee, (0, 0, 0))


if __name__ == "__main__":
    seed, definition, connex, filename = decode_args()
    if seed==0: seed = int(time.time_ns())
    random.seed(seed)
    width,height = definition
    nb_pixels = width*height
    nb_ivrognes = nb_pixels//5

    im = Image.new(width, height)
    color=(255, 255, 255)
    fill_with_color(im,color)

    dendrite(im, nb_ivrognes, connex)

     # Sauvegarde 
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")
