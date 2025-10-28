## But et contexte rapide

Ce dépôt produit des images par simulation de marches aléatoires ("ivrognes") et par génération de structures de type dendrite. Les scripts principaux se trouvent dans le dossier `Programme code et Script/` et sont destinés à être lancés depuis la ligne de commande.

## Ce que l'agent doit savoir pour être immédiatement productif

- Architecture simple : ensemble de scripts Python qui utilisent une petite couche utilitaire (`utils.py`) et un wrapper autour de PIL (`simple_image.py`).
- Flux de données principal : entrée CLI -> parsing (fonctions dans `utils.py`) -> génération d'une `Image` -> écriture fichier via PIL.
- Dépendances externes : Pillow (vérifié au runtime dans `simple_image.py`) et autres paquets listés dans `requirements.txt`.

## Commandes utiles (Windows cmd.exe)

1) Créer l'environnement et installer les dépendances (extrait du README) :

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2) Exemple d'exécution (démonstration) :

```cmd
python "Programme code et Script\demo-utils.py" 0 300x300 123,34,255 sortie.png
python "Programme code et Script\goguette.py" 0 150x150 4-connected sortie_goguette.png
```

Remarque : les scripts attendent des arguments très précis — utilisez les fonctions de parsing dans `utils.py` (ex. `definition_from_str`, `color_from_str`).

## Fichiers clés à lire en priorité

- `README.md` — instructions d'installation et description du projet.
- `Programme code et Script/utils.py` — parsing d'arguments, génération de déplacements (fonction `connected_roaming`) et constantes (`WEIGHTED_DEPS`).
- `Programme code et Script/simple_image.py` — wrapper autour de PIL (classe `Image`) ; vérifie la version de PIL et expose `new`, `read`, `save`, `get_color`, `set_color`.
- `Programme code et Script/demo-utils.py` — exemple d'utilisation des API du projet (bon modèle de référence pour les scripts à venir).
- `Programme code et Script/goguette.py` — script principal « ivrognes en goguette » (important : contient des appels incompatibles avec `simple_image.py`, voir ci‑dessous).

## Pièges et incohérences observées (à garder en tête)

- API image non uniforme : `simple_image.py` définit la classe `Image` avec `set_color/get_color/new/read/save`, mais `goguette.py` importe `SimpleImage` et appelle `set_pixel`, `fill` et `save`. De même, `demo-utils.py` utilise `Image.new(...).set_color(...)`.
  - Conséquence : avant d'ajouter ou modifier du code, vérifier quelle API est utilisée par le script ciblé; un refactor global serait utile mais est hors-scope sans tests.

- Signature de `connected_roaming` : dans `utils.py` la fonction est définie comme `connected_roaming(position, type="4-connected")` (sans paramètres width/height) tandis que certains scripts appellent `connected_roaming(..., width=..., height=...)` — attention aux appels posant des erreurs d'arguments.

- Style de validation : les fonctions de parsing retournent `None` si invalide (par ex. `definition_from_str`, `color_from_str`). Les scripts utilisent souvent `or usage(...)` pour arrêter en cas d'erreur — respecter ce pattern pour garder un comportement homogène.

## Règles pratiques pour les PRs et modifications automatisées

- Préférer modifier `demo-utils.py`/écrire un petit script d'exemple avant de toucher les scripts principaux.
- Ajouter des tests minimaux (ex. un petit test qui crée une image 50x50 et vérifie `save()` fonctionne) avant de réécrire l'API image.
- Lors d'un fix global d'API (ex. unifier `Image` vs `SimpleImage`), documenter la décision et mettre à jour tous les scripts en une seule PR pour éviter régressions.

## Exemples concrets à utiliser dans les suggestions de code

- Pour parser une définition : utiliser `from Programme code et Script.utils import definition_from_str` et valider `None`.
- Pour créer une image compatible avec `demo-utils.py` : `im = Image.new(width, height); im.set_color((x,y), color); im.save(path)`.

## Questions pour l'auteur / points à clarifier

- Voulez-vous standardiser l'API image (préférer `Image` ou `SimpleImage`), ou dois‑je proposer des patches pour rendre les deux compatibles ?
- Y a‑t‑il des workflows de test/CI souhaités (ex. GitHub Actions) pour exécuter des scripts ou vérifier l'environnement PIL ?

Si quelque chose dans ce fichier est incomplet ou manque de contexte, dites‑moi quelles priorités vous voulez (corriger incohérences API, ajouter tests, ajouter CI) et je fusionne/itère.
