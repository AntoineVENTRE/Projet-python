@echo off
REM =========================================
REM Tests pour tous les programmes Goguette puis Dendrite
REM =========================================

REM Pour lancer le test, copier-coller cette commande dans le terminal avec le venv activé :
REM .\Tests\test_goguette.bat

REM --- Tests goguette.py ---
echo === Tests goguette.py ===
python "Programme code et Script/goguette.py" 1 150x150 4-connected goguette-1.png
python "Programme code et Script/goguette.py" 2 150x150 4-connected goguette-2.png
python "Programme code et Script/goguette.py" 5 150x150 8-connected goguette-5.png
python "Programme code et Script/goguette.py" 100 150x150 8-connected goguette-100.png

REM --- Tests goguette_choix_depart.py ---
echo === Tests goguette_choix_depart.py ===
python "Programme code et Script/goguette_choix_depart.py" 1 150x150 4-connected goguette_cd-01.png 45 60
python "Programme code et Script/goguette_choix_depart.py" 2 150x150 4-connected goguette_cd-02.png  30 90
python "Programme code et Script/goguette_choix_depart.py" 5 150x150 8-connected goguette_cd-05.png 75 120
python "Programme code et Script/goguette_choix_depart.py" 100 150x150 8-connected goguette_cd-0100.png 10 10

REM --- Tests goguette_couleur_ivrognes.py ---
echo === Tests goguette_couleur_ivrognes.py ===
python "Programme code et Script/goguette_couleur_ivrognes.py" 1 150x150 4-connected goguette_couleur-001.png 255 0 0 0 0 255
python "Programme code et Script/goguette_couleur_ivrognes.py" 2 150x150 4-connected goguette_couleur-002.png 60 180 90 30 15 75
python "Programme code et Script/goguette_couleur_ivrognes.py" 5 150x150 8-connected goguette_couleur-005.png 200 50 100 150 250 0
python "Programme code et Script/goguette_couleur_ivrognes.py" 100 150x150 8-connected goguette_couleur-00100.png 0 0 0 255 255 255

REM --- Tests goguette_variation_couleur.py ---
echo === Tests goguette_variation_couleur.py ===
python "Programme code et Script/goguette_variation_couleur.py" 1 150x150 4-connected goguette_var_couleur-0001.png
python "Programme code et Script/goguette_variation_couleur.py" 2 150x150 4-connected goguette_var_couleur-0002.png
python "Programme code et Script/goguette_variation_couleur.py" 5 150x150 8-connected goguette_var_couleur-0005.png
python "Programme code et Script/goguette_variation_couleur.py" 100 150x150 8-connected goguette_var_couleur-000100.png

REM --- Tests goguette.py avec variation de couleurs aléatoires ---
echo === Tests goguette.py couleur aléatoire ===
python "Programme code et Script/goguette.py" 42 50x50 4-connected test_image.png

REM --- Tests dendrite.py ---
python "Programme code et Script/dendrite.py" 1 150x150 8-connected dendrite-00001.png
python "Programme code et Script/dendrite.py" 2 150x150 8-connected dendrite-00002.png
python "Programme code et Script/dendrite.py" 5 150x150 8-connected dendrite-00005.png
python "Programme code et Script/dendrite.py" 100 150x150 8-connected dendrite-0000100.png



REM --- Fin des tests ---
echo === Tests termines ===