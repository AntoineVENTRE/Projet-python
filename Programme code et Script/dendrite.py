# Dendrite.py

import sys
import random
import time
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming, usage


def est_voisin_noir(pos, noirs, connexity):
    """Retourne True si un des voisins de pos est noir."""
    x, y = pos
    if connexity == "4-connected":
        voisins = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    else:
        voisins = [(x+i, y+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0)]
    return any(v in noirs for v in voisins)


def main():
    # --- Vérification des arguments ---
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])
    connexity = sys.argv[3]
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