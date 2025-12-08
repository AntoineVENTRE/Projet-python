#!/usr/bin/env python3
import sys, random, os, time
from utils import connected_roaming, get_random_xy, definition_from_str, WEIGHTED_DEPS
from simple_image import Image

def usage(msg):
    print(f"{msg}\nUsage: {sys.argv[0]} <seed> <definition> <connex> <image_out>")
    sys.exit(1)

def decode_args():
    if len(sys.argv) != 5:
        usage("Nombre d'arguments incorrect")
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])
    connex = sys.argv[3]
    if connex not in ["4-connected","8-connected"]:
        usage(f"Connexité incorrecte: '{connex}'")
    filename = sys.argv[4]
    return seed, definition, connex, filename

def fill_with_color(im, color=(255,255,255)):
    for x in range(im.width):
        for y in range(im.height):
            im.set_color((x,y), color)

def get_voisins(pos, connex, width, height):
    x,y = pos
    deps = WEIGHTED_DEPS[connex]["deps"]
    return [((x+dx)%width, (y+dy)%height) for dx,dy in deps]

def est_voisin_de_noir(pos, connex, width, height, points_noirs):
    return any(v in points_noirs for v in get_voisins(pos, connex, width, height))

def position_depart_valide(im, connex, points_noirs):
    for _ in range(im.width * im.height):
        pos = get_random_xy(im)
        if pos not in points_noirs and not est_voisin_de_noir(pos, connex, im.width, im.height, points_noirs):
            return pos
    return None

def marche_ivrogne(im, pos, connex, points_noirs):
    max_pas = 10 * im.width * im.height
    for _ in range(max_pas):
        if est_voisin_de_noir(pos, connex, im.width, im.height, points_noirs):
            return pos
        pos = connected_roaming(pos, type=connex)
        pos = (pos[0]%im.width, pos[1]%im.height)
    return None

def dendrite(im, nb_ivrognes, connex):
    points_noirs = set()
    centre = (im.width//2, im.height//2)
    points_noirs.add(centre)
    im.set_color(centre, (0,0,0))
    for _ in range(nb_ivrognes):
        pos = position_depart_valide(im, connex, points_noirs)
        if pos is None: continue
        pos_fin = marche_ivrogne(im, pos, connex, points_noirs)
        if pos_fin and pos_fin not in points_noirs:
            points_noirs.add(pos_fin)
            im.set_color(pos_fin, (0,0,0))

if __name__ == "__main__":
    seed, definition, connex, filename = decode_args()
    if seed==0: seed = int(time.time_ns())
    random.seed(seed)
    width,height = definition
    nb_pixels = width*height
    nb_ivrognes = nb_pixels//5

    im = Image.new(width, height)
    fill_with_color(im)

    dendrite(im, nb_ivrognes, connex)

    os.makedirs("Images", exist_ok=True)
    im.save(os.path.join("Images", filename))
    print(f"Image enregistrée sous Images/{filename}")
