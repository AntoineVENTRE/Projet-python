#!/usr/bin/env python3

# Bibliothèques nécessaires 
import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import connected_roaming, WEIGHTED_DEPS,get_random_xy
from demo_utils import usage,decode_argv,fill_with_color

def get_voisins(pos, connex, width, height):
    """Retourne la liste des voisins d'une position selon la connexité."""
    x, y = pos
    voisins = []
    # Récupère les déplacements depuis WEIGHTED_DEPS
    deps = WEIGHTED_DEPS[connex]["deps"]
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
    # Déposer les ivrognes un par un
    for i in range(nb_ivrognes):
        # Trouver une position de départ valide
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
    # Récupération des arguments de la ligne de commande
    seed, definition, connex, im_name = decode_argv()
    if seed == 0:
        seed = time.time_ns()
    
    # Calcul du nombre d'ivrognes (1/5 du nombre de pixels)
    nb_pixels = definition[0] * definition[1]
    nb_ivrognes = nb_pixels // 5
    
    print(f"Graine: {seed}")
    print(f"Définition: {definition[0]}x{definition[1]}")
    print(f"Connexité: {connex}")
    print(f"Image à créer: {im_name}")

    # Initialisation du générateur aléatoire
    random.seed(seed)
        
    # Préparation de l'image
    im = SimpleImage.new(*definition)
    fill_with_color(im, (255, 255, 255))

    # Croissance de la dendrite
    dendrite(im, nb_ivrognes, connex)
    
    # Enregistrement de l'image finale
    im.save(im_name)