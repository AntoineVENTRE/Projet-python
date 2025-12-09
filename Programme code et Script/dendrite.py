#!/usr/bin/env python3
import sys
import random
import os
import time
from utils import connected_roaming, get_random_xy, definition_from_str, WEIGHTED_DEPS,positive_int_from_str
from simple_image import Image
from demo_utils import usage,fill_with_color

def decode_argv():
    """Décode le contenu de la ligne de commande (sys.argv) et retourne tous
    les éléments analysés
    """
    # le nombre d'arguments (le nom du script + 4 arguments)
    len(sys.argv) == 5 or usage("Nombre d'arguments incorrect")
    # le 1er argument est la graine (un entier positif)
    seed = positive_int_from_str(sys.argv[1])
    seed != None or usage(f"Graine incorrecte: '{sys.argv[1]}'")
    # le 2e argument est une définition d'image (de la forme 800x600)
    definition = definition_from_str(sys.argv[2])
    definition != None or usage(f"Définition incorrecte: '{sys.argv[2]}'")
    if definition[0] < 30 or definition[1] < 30:
        usage(f"Définition minimum: 30x30")
    # le 3e argument est la connexité
    connex = str(sys.argv[3])
    if connex not in ['4-connected', '8-connected']:
        usage(f"Connexité incorrecte: '{sys.argv[3]}' (doit être '4-connected' ou '8-connected')")
    # le 4e argument est le chemin d'un fichier image à créer
    filename = sys.argv[4]
    return seed, definition, connex, filename

def get_voisins(pos, connexity, width, height):
    """Retourne la liste des voisins d'une position selon la connexité."""
    x, y = pos
    voisins = []
    # Récupère les déplacements depuis WEIGHTED_DEPS
    deps = WEIGHTED_DEPS[connexity]["deps"]
    for dx, dy in deps:
        # Le modulo prend en compte le monde torique pour la vérification des voisins
        nx = (x + dx) % width
        ny = (y + dy) % height
        voisins.append((nx, ny))
    return voisins


def est_voisin_de_noir(pos, connex, width, height, points_noirs):
    """Vérifie si la position est voisine d'un point noir."""
    voisins = get_voisins(pos, connex, width, height)
    for v in voisins:
        if v in points_noirs:
            return True
    return False

def position_depart_valide(im, connex, points_noirs):
    """Trouve une position de départ valide pour un ivrogne (pas sur un point noir pas voisin 
    d'un point noir """
    max_tentatives = nb_pixels  #on limite le nombre de tentatives
    width, height = im.width, im.height
    for _ in range(max_tentatives):
        pos = get_random_xy(im)
        if pos not in points_noirs and not est_voisin_de_noir(pos, connex, width, height, points_noirs):
            return pos
    return None # Impossible de trouver une position valide


def marche_ivrogne(im, pos_depart, connex, points_noirs):
    """Fait marcher un ivrogne jusqu'à ce qu'il arrive à proximité d'un point noir."""
    pos = pos_depart
    width = im.width
    height = im.height
    max_pas = 10 * height * width 
    for _ in range(max_pas):
        if est_voisin_de_noir(pos, connex, width, height, points_noirs):
            return pos
        pos = connected_roaming(pos, type=connex)
        pos = (pos[0] % width, pos[1] % height) # Assurer le monde torique
    return None  # L'ivrogne est perdu

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
        pos_arrivee = marche_ivrogne(im, pos_depart, connex, points_noirs)

        # 3) Ajouter le point noir si nécessaire
        if pos_arrivee is not None and pos_arrivee not in points_noirs:
            points_noirs.add(pos_arrivee)
            im.set_color(pos_arrivee, (0, 0, 0))



if __name__ == "__main__":
    seed, definition, connex, filename = decode_argv()
    if seed==0: seed = int(time.time_ns())
    random.seed(seed)
    width,height = definition
    nb_pixels = width*height
    nb_ivrognes = nb_pixels//5

    im = Image.new(width, height)
    color=(255, 255, 255)
    fill_with_color(im,color)

    dendrite(im, nb_ivrognes, connex)

    os.makedirs("Images", exist_ok=True)
    im.save(os.path.join("Images", filename))
    print(f"Image enregistrée sous Images/{filename}")
