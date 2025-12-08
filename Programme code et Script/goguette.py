# -*- coding: utf-8 -*- 

# #Bibliothèques nécessaires 
import sys
import random
import time
import os
from simple_image import Image as SimpleImage
from utils import definition_from_str, connected_roaming
from demo_utils import usage


def marche_ivrogne (im, pos, n_steps, connexity, color,width,height): 
    """Effectue une marche aléatoire d’un seul ivrogne sur l’image."""  
    x, y = pos 
    for _ in range(n_steps): 
        im.set_color((x, y), color) 
        x, y = connected_roaming((x, y), type=connexity) 
        x %= width 
        y %= height 
    return im 

def main(): 
    # --- Vérification des arguments --- 
    if len(sys.argv) != 5: 
        usage("Erreur : nombre d’arguments incorrect.") 
    
    # --- Récupération des paramètres --- 
    seed = int(sys.argv[1]) 
    definition = definition_from_str(sys.argv[2]) # ex : "150x150" -> (150, 150) 
    connexity = sys.argv[3] # "4-connected" ou "8-connected" 
    filename = sys.argv[4] 
    
    # --- Initialisation du hasard --- 
    if seed == 0: 
        seed = time.time_ns() 
    random.seed(seed) 
    print(f"Graine: {seed}") 
    
    # --- Création de l'image ---
    width, height = definition
    color_fond = (255, 255, 255) # blanc 
    im = SimpleImage.new(width,height, color_fond) 
    
    # --- Paramètres --- 
    n_steps = int((width * height) / 5) # nombre de pas par ivrogne 
    colors_ivrognes = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] # R, G, B 
    
    # --- Position de départ : centre de l'image --- 
    pos = (width // 2, height // 2) 
    
    # --- Simulation pour chaque ivrogne --- 
    for color in colors_ivrognes: 
        marche_ivrogne(im, pos, n_steps, connexity, color, width, height) 
    
    # --- Sauvegarde ---
    os.makedirs("Images", exist_ok=True)
    output_file = os.path.join("Images", filename)
    im.save(output_file)
    print(f"Image enregistrée sous {output_file}")

if __name__ == "__main__":
    main()


