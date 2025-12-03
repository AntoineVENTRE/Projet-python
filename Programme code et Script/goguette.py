#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming
from demo_utils import usage

def creation_image_fond(width, height, color):
    """Crée une image unie de la couleur spécifiée."""
    im = SimpleImage.new(width, height)
    for x in range(width):
        for y in range(height):
            im.set_color((x, y), color)
    return im

def is_adjacent_black(im, pos, connexity):
    """Retourne True si le pixel est adjacent à un pixel noir."""
    x, y = pos
    width, height = im.width, im.height
    neighbors = connected_roaming((x, y), type=connexity)
    for nx, ny in neighbors:
        nx %= width
        ny %= height
        if im.get_color((nx, ny)) == (0, 0, 0):
            return True
    return False

def random_start(im, connexity):
    """Choisit un point de départ aléatoire non noir et non adjacent à un noir."""
    width, height = im.width, im.height
    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if im.get_color((x, y)) != (0, 0, 0) and not is_adjacent_black(im, (x, y), connexity):
            return (x, y)

def marche_ivrogne_dendrite(im, start_pos, connexity):
    """Fait errer l'ivrogne jusqu'à proximité d'un point noir, puis ajoute un point noir."""
    width, height = im.width, im.height
    x, y = start_pos
    while True:
        # Vérifie si proche d'un noir
        if is_adjacent_black(im, (x, y), connexity):
            im.set_color((x, y), (0, 0, 0))  # nouveau point noir
            break
        # Déplacement aléatoire
        x, y = connected_roaming((x, y), type=connexity)
        x %= width
        y %= height
    return im

def main():
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # --- Récupération des paramètres ---
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    filename = sys.argv[4]

    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")

    width, height = definition
    im = creation_image_fond(width, height, (255, 255, 255))  # image blanche

    # --- Germe central ---
    center = (width // 2, height // 2)
    im.set_color(center, (0, 0, 0))

    # --- Paramètres ---
    n_ivrognes = 1000  # nombre d'ivrognes à déposer

    for _ in range(n_ivrognes):
        start = random_start(im, connexity)
        im = marche_ivrogne_dendrite(im, start, connexity)

    # --- Sauvegarde ---
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()


