#!/usr/bin/env python3
import re
import random


def definition_from_str(argument):
    """Reçoit un argument de la forme "100x300" et retourne un tuple de la
    forme (100, 300).  Les 2 valeurs entières doivent être strictement
    positives.

    Retourne None Si l'argument n'est pas de la bonne forme.

    """
    match = re.fullmatch(r"(\d+)x(\d+)", argument)
    if match:
        return tuple(int(v) for v in match.group(1, 2))
    return None


def positive_int_from_str(argument):
    """Reçoit un argument sous la forme d'une suite de chiffres et retourne
    l'entier correspondant.

    Retourne None si l'argument n'est pas de la bonne forme.

    """
    match = re.fullmatch(r"(\d+)", argument)
    if match:
        return int(match.group(1))
    return None


def color_from_str(argument):
    """Reçoit une couleur sous la forme "123,0,255"
    et retourne un tuple de la forme (123, 0, 255)
    Les 3 valeurs entières doivent être dans l'intervalle [0, 255].

    Retourne None si l'argument n'est pas de la bonne forme.

    """
    match = re.fullmatch(r"(\d+),(\d+),(\d+)", argument)
    if match:
        res = tuple(int(v) for v in match.group(1, 2, 3))
        for v in res:
            if v < 0 or v > 255:
                return None
        return res
    return None


def coordinates_from_str(argument):
    """Reçoit des coordonnées sous la forme "17,23"
    et retourne un tuple de la forme (17, 23)
    Les 2 valeurs entières doivent être positives.

    Retourne None si l'argument n'est pas de la bonne forme.

    """
    match = re.fullmatch(r"(\d+),(\d+)", argument)
    if match:
        return tuple(int(v) for v in match.group(1, 2))
    return None


# WEIGHTED_DEPS associe à chaque nom de type de connexions, un
# dictionnaire définissant les déplacements relatifs faisables ("deps")
# et leur poids respectif ("weights") utilisés lors d'un choix au
# hasard.
#
# Lors de la définition d'un nouveau type de connexions, vérifier que
# "deps" contient bien des couples et que "weights" contient autant
# d'éléments que "deps".
WEIGHTED_DEPS = {
    "2-connected": {
        "deps": [(-1,1), (1,1)], # sud ouest, sud est
        "weights": [1, 1], # poids égaux
    },
    "2-connected-biased": {
        "deps": [(-1,1), (1,1)], # sud ouest, sud est
        "weights": [1, 1.5], # un "léger" biais
    },
    "4-connected": {
        "deps": [(0, -1), (-1, 0), (1, 0), (0, 1)], # nord, ouest, est, sud
        "weights": [1, 1, 1, 1], # poids égaux
    },
}


def connected_roaming(position, type="4-connected"):
    """À partir d'une 'position' (un couple: x, y) et d'un 'type' de
    connexions, choisit au hasard un déplacement en tenant compte des
    poids de chacun d'entre eux et retourne la nouvelle position.

    'type' permet de choisir le type de connexions utilisées (parmi ceux
    définit dans WEIGHTS_DEPS).

    """
    assert type in WEIGHTED_DEPS.keys()
    deps = WEIGHTED_DEPS[type]["deps"]
    weights = WEIGHTED_DEPS[type]["weights"]
    dep = random.choices(population=deps, weights=weights, k=1)[0]
    new_position = (position[0] + dep[0], position[1] + dep[1])
    return new_position


def get_random_xy(im):
    return (random.randrange(im.width), random.randrange(im.height))
