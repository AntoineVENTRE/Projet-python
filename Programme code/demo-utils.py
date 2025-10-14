#!/usr/bin/env python3
"""Ce script sert de démonstration des modules 'utils' et
'simple_image'.

Vous pouvez vous en inspirer pour écrire vos propres scripts.

"""
import sys
import random
from time import time_ns
from utils import connected_roaming, positive_int_from_str, definition_from_str, color_from_str
from simple_image import Image

def usage(error):
    """Affiche le message 'error', rappelle à l'utilisateur l'usage du
    script, et arrête brutalement le script en retournant 1 au système.

    """
    print(f"{error}\n\n"
          f"Usage: {sys.argv[0]} <seed> <definition> <color> <image_out>\n"
          "\n"
          "\t<seed> est un entier positif qui servira de graine pour le hasard\n"
          "\t       (0 pour changer à chaque fois)\n"
          "\t<definition> est de la forme: 800x600\n"
          "\t<color> est de la forme: 123,34,255\n"
          "\t<image_out> est le nom de l'image à créer.\n",
          "\n"
          "\tDémonstration des fonctions de utils.py.\n",
          file=sys.stderr)
    sys.exit(1)


def decode_argv():
    """Décode le contenu de la ligne de commande (sys.argv) et retourne tous
    les éléments analysés.

    Si l'un des éléments n'est pas correct, appelle usage() avec le
    message d'erreur adéquat.

    """
    # le nombre d'arguments (le nom du script + 4 arguments)
    len(sys.argv) == 5 or usage("Nombre d'arguments incorrect")
    
    # le 1er argument est la graine (un entier positif)
    seed = positive_int_from_str(sys.argv[1])
    seed != None or usage(f"Graine incorrecte: '{sys.argv[1]}'")

    # le 2e argument est une définition d'image (de la forme 800x600)
    definition = definition_from_str(sys.argv[2])
    definition != None or usage(f"Définition incorrecte: '{sys.argv[2]}'")
    if  definition[0] < 100 or definition[1] < 100:
        usage(f"Définition minimum: 100x100")

    # le 3e argument est une couleur
    color = color_from_str(sys.argv[3])
    color != None or usage(f"Couleur incorrecte: '{sys.argv[3]}'")
        
    # le 4e argument est le chemin d'un fichier image à créer
    im_name = sys.argv[4]
    
    return seed, definition, color, im_name
    

def fill_with_color(im, color):
    """Remplit l'image im avec la couleur color."""
    for x in range(im.width):
        for y in range(im.height):
            im.set_color((x, y), color)

def demo(im, color):
    """Modifie l'image pour démontrer l'utilisation de connected_roaming()"""
    color2 = tuple(255 - composante for composante in color) # couleur complémentaire
    for j in range(20):
        xy = (round(im.width/2), 0) # le milieu en haut de l'image
        while xy[1] < im.height and xy[0] >= 0 and xy[0] < im.width:
            im.set_color(xy, color2)
            xy = connected_roaming(xy, type="2-connected")
    color3 = tuple([color2[1], color2[2], color2[0]])
    for j in range(20):
        xy = (round(im.width/2), 0) # le milieu en haut de l'image
        while xy[1] < im.height and xy[0] >= 0 and xy[0] < im.width:
            im.set_color(xy, color3)
            xy = connected_roaming(xy, type="2-connected-biased")

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    seed, definition, color, im_name = decode_argv()
    if seed == 0:
        seed = time_ns()
    print(f"Graine choisie: {seed}")
    print(f"Définition choisie: {definition[0]}x{definition[1]}")
    print(f"Couleur choisie: {color}")
    print(f"Image à créer: {im_name}")

    # Initialisation du générateur aléatoire
    random.seed(seed)
        
    # Préparation de l'image
    im = Image.new(*definition)
    fill_with_color(im, color)

    # La démonstration
    demo(im, color)
    
    # Enregistrement de l'image finale
    im.save(im_name)

    
    
    
