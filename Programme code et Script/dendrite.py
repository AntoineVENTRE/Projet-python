#!/usr/bin/env python3

# Bibliothèques nécessaires 
import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import connected_roaming, WEIGHTED_DEPS,get_random_xy,definition_from_str
from demo_utils import usage,decode_argv,fill_with_color

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

def position_depart_valide(im, connex, points_noirs, nb_pixels):
    """Trouve une position de départ valide pour un ivrogne (pas sur un point noir pas voisin 
    d'un point noir """
    max_tentatives = nb_pixels  #on limite le nombre de tentatives
    width, height = im.width, im.height
    for _ in range(max_tentatives):
        pos = get_random_xy(im)
        if pos not in points_noirs and not est_voisin_de_noir(pos, connex, width, height, points_noirs):
            return pos
    return None # Impossible de trouver une position valide

def marche_ivrogne(im, pos_depart, connex, points_noirs, nb_pixels):
    """Fait marcher un ivrogne jusqu'à ce qu'il arrive à proximité d'un point noir."""
    pos = pos_depart
    max_pas = 10 * nb_pixels
    width = im.width
    height = im.height
    for _ in range(max_pas):
        if est_voisin_de_noir(pos, connex, width, height, points_noirs):
            return pos
        pos = connected_roaming(pos, type=connex)
        pos = (pos[0] % width, pos[1] % height) # Assurer le monde torique
    return None  # L'ivrogne est perdu


def dendrite(im, nb_ivrognes, connex):
    """Simule la croissance d'une dendrite avec des ivrognes.
    Le nombre d'ivrognes est 1/5 du nombre total de pixels."""
    # Liste des points noirs
    points_noirs = []
    nb_pixels = im.width * im.height
    # Placer le germe au centre
    centre = (im.width // 2, im.height // 2)
    points_noirs.append(centre)
    im.set_color(centre, (0, 0, 0))
    for i in range(nb_ivrognes): # Déposer les ivrognes un par un
        pos_depart = position_depart_valide(im, connex, points_noirs, nb_pixels)
        # Si pas de point valide trouvé, on passe à l'ivrogne suivant
        if pos_depart is not None:
            # Faire marcher l’ivrogne jusqu'à proximité d’un point noir
            pos_arrivee = marche_ivrogne(im, pos_depart, connex, points_noirs, nb_pixels)
            if pos_arrivee is not None:
                # Vérifier si la position n'est pas déjà noire
                deja_noir = False
                for p in points_noirs:
                    if p == pos_arrivee:
                        deja_noir = True
                        break
                if not deja_noir:
                    points_noirs.append(pos_arrivee)
                    im.set_color(pos_arrivee, (0, 0, 0))

if __name__ == "__main__":

    # Vérification des arguments
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # Récupération des arguments de la ligne de commande
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])  # ex : "150x150" -> (150, 150)
    connexity = sys.argv[3]  # "4-connected" ou "8-connected"
    filename = sys.argv[4]

    # Initialisation du hasard 
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")
    
    # Calcul du nombre d'ivrognes (1/5 du nombre de pixels)
    width, height = definition
    nb_pixels =  width * height
    nb_ivrognes = nb_pixels // 5

    # Initialisation du générateur aléatoire
    if seed == 0:
        seed = time.time_ns()
    random.seed(seed)
    print(f"Graine: {seed}")
        
    # Préparation de l'image
    color_fond = (255, 255, 255)
    im = SimpleImage.new(width, height)
    fill_with_color(im, color_fond)

    # Croissance de la dendrite 
    dendrite(im, nb_ivrognes, connexity)
    
    # Sauvegarde 
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")