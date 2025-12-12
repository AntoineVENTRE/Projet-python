# Mini-projet Algorithmique et Programmation — Ivrognes et Dendrites

**Auteurs :** Germain Caudal Lhermite et Antoine VENTRE  
**IFIE1 – Octobre 2025 – IMT Mines Albi**

## 📌 Description

Ce projet propose deux simulations basées sur des balades aléatoires (“random walks”) pour générer des images :

1. Trois ivrognes en goguette

Trois marcheurs aléatoires se déplacent sur une image et laissent chacun une trace colorée, produisant des motifs visuels uniques.

2. Dendrites et ivrognes

Simulation d’une croissance dendritique inspirée du modèle de type DLA (Diffusion-Limited Aggregation) :

des points noirs fixes servent de graine initiale,

les “ivrognes” errent jusqu’à toucher la structure,

à ce moment, ils se figent et contribuent à la formation de la dendrite.

## ⚙️ Installation

Créer et activer un environnement virtuel :

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## 🧪 Commandes utiles

Envoyer les modifications sur GitHub :

git add .
git commit -m "upload"
git push


## Lancer les tests :

.\Tests\test_goguette.bat


