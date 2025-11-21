@echo off
REM =========================================
REM Tests pour tous les programmes Goguette puis Dendrite
REM =========================================

REM --- Tests goguette.py ---
echo === Tests goguette.py ===
python "Programme code et Script/goguette.py" 1 150x150 4-connected goguette-1.png
python "Programme code et Script/goguette.py" 2 150x150 4-connected goguette-2.png
python "Programme code et Script/goguette.py" 5 150x150 8-connected goguette-5.png
python "Programme code et Script/goguette.py" 100 150x150 8-connected goguette-100.png

REM --- Tests goguette_choix_depart.py ---
echo === Tests goguette_choix_depart.py ===
python "Programme code et Script/goguette_choix_départ.py" 1 150x150 4-connected goguette_cd-1.png
python "Programme code et Script/goguette_choix_départ.py" 2 150x150 4-connected goguette_cd-2.png
python "Programme code et Script/goguette_choix_départ.py" 5 150x150 8-connected goguette_cd-5.png
python "Programme code et Script/goguette_choix_départ.py" 100 150x150 8-connected goguette_cd-100.png

REM --- Tests goguette_couleur_ivrognes.py ---
echo === Tests goguette_couleur_ivrognes.py ===
python "Programme code et Script/goguette_couleur_ivrognes.py" 1 150x150 4-connected goguette_couleur-1.png
python "Programme code et Script/goguette_couleur_ivrognes.py" 2 150x150 4-connected goguette_couleur-2.png
python "Programme code et Script/goguette_couleur_ivrognes.py" 5 150x150 8-connected goguette_couleur-5.png
python "Programme code et Script/goguette_couleur_ivrognes.py" 100 150x150 8-connected goguette_couleur-100.png

REM --- Tests goguette_variation_couleur.py ---
echo === Tests goguette_variation_couleur.py ===
python "Programme code et Script/goguette_variation_couleur.py" 1 150x150 4-connected goguette_var_couleur-1.png
python "Programme code et Script/goguette_variation_couleur.py" 2 150x150 4-connected goguette_var_couleur-2.png
python "Programme code et Script/goguette_variation_couleur.py" 5 150x150 8-connected goguette_var_couleur-5.png
python "Programme code et Script/goguette_variation_couleur.py" 100 150x150 8-connected goguette_var_couleur-100.png

REM --- Tests goguette.py avec variation de couleurs aléatoires ---
echo === Tests goguette.py couleur aléatoire ===
python "Programme code et Script/goguette.py" 42 50x50 4-connected test_image.png


##REM --- Tests dendrite.py ---
##echo === Tests dendrite.py ===
##python "Programme code et Script/dendrite.py" 1 150x150 4-connected dendrite-1.png
##python "Programme code et Script/dendrite.py" 2 150x150 4-connected dendrite-2.png
##python "Programme code et Script/dendrite.py" 5 150x150 8-connected dendrite-5.png
##python "Programme code et Script/dendrite.py" 100 150x150 8-connected dendrite-100.png


REM --- Fin des tests ---
echo === Tests terminés ===



##print a faire dans le terminal avec le venv activé : .\Tests\test_goguette.bat
