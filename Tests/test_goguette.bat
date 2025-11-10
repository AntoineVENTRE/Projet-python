

@echo off
echo === Tests goguette ===
python "Programme code et Script/goguette.py" 1 150x150 4-connected goguette-1.png
python "Programme code et Script/goguette.py" 2 150x150 4-connected goguette-2.png
python "Programme code et Script/goguette.py" 5 150x150 8-connected goguette-5.png
python "Programme code et Script/goguette.py" 100 150x150 8-connected goguette-100.png

echo === Tests dendrite ===
python "Programme code et Script/dendrite.py" 1 150x150 4-connected dendrite-1.png
python "Programme code et Script/dendrite.py" 2 150x150 4-connected dendrite-2.png
python "Programme code et Script/dendrite.py" 5 150x150 8-connected dendrite-5.png
python "Programme code et Script/dendrite.py" 100 150x150 8-connected dendrite-100.png

echo === Tests terminés ===
pause


##print a faire dans le terminal avec le venv activé : .\Tests\test_goguette.bat