import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming, get_random_xy
from demo_utils import usage
from goguette import creation_image_fond

def voisinage_8(pos):
    x, y = pos
    return [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),             (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]

def main():
    # Vérification des arguments
    if len(sys.argv) != 5:
        usage("Erreur : nombre d’arguments incorrect.")

    # Paramètres
    seed = int(sys.argv[1])
    definition = definition_from_str(sys.argv[2])
    connexity = sys.argv[3]
    filename = sys.argv[4]

    # Initialisation du hasard
    if seed == 0:
        seed = time.time_ns()
    print(f"Graine: {seed}")
    random.seed(seed)

    width, height = definition
    im = creation_image_fond(width, height, (255, 255, 255))

    # Pixel central noir
    xm = width // 2
    ym = height // 2
    im.set_color((xm, ym), (0, 0, 0))

    # Liste des pixels noirs
    deja_parcouru = {(xm, ym)}

    # Nombre d’ivrognes = 1/5 de la surface
    n_ivrogne = (width * height) // 5

    # Limites
    pas_max = (width * height) * 10
    recherche_max = width * height

    # Boucle principale des ivrognes
    for _ in range(n_ivrogne):

        # --- Recherche d’un point de départ valide ---
        recherche_points = 0
        while True:
            recherche_points += 1
            if recherche_points > recherche_max:
                # On abandonne cet ivrogne
                break

            x, y = get_random_xy(im)

            # Ne doit pas être noir
            if (x, y) in deja_parcouru:
                continue

            # Ne doit pas être voisin d’un pixel noir
            voisins = voisinage_8((x, y))
            voisins_toriques = [(vx % width, vy % height) for vx, vy in voisins]

            if any(v in deja_parcouru for v in voisins_toriques):
                continue

            # Point de départ valide trouvé
            break

        # Si aucun point valide trouvé → on passe à l’ivrogne suivant
        if recherche_points > recherche_max:
            continue

        # --- Marche de l’ivrogne ---
        pas = 0
        while pas < pas_max:
            # Voisins pour contact avec une dendrite
            voisins = voisinage_8((x, y))
            voisins_toriques = [(vx % width, vy % height) for vx, vy in voisins]

            # L’ivrogne touche une dendrite → dépôt
            if any(v in deja_parcouru for v in voisins_toriques):
                im.set_color((x, y), (0, 0, 0))
                deja_parcouru.add((x, y))
                break

            # Sinon marche aléatoire
            x, y = connected_roaming((x, y), type=connexity)
            x %= width
            y %= height
            pas += 1

        # Si pas >= pas_max → l’ivrogne est perdu (on ne dépose rien)

    # Sauvegarde
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()