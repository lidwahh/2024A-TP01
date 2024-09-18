# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = round(float(input("Pourcentage de batterie ? ")), 1)


if battery_level == 0:
    print("La batterie est vide")
else:

    if battery_level <= 5:
        resultat = battery_level * 6
    elif battery_level <= 10:
        resultat = 5 * 6 + (battery_level - 5) * 2.5
    elif battery_level <= 25:
        resultat = 5 * 6 + 5 * 2.5 + (battery_level - 10)
    elif battery_level <= 50:
        resultat = 5 * 6 + 5 * 2.5 + 15 + (battery_level - 25) * 0.5
    elif battery_level <= 100:
        resultat = 5 * 6 + 5 * 2.5 + 15 + 25 * 0.5 + (battery_level - 50) * 2
    
    resultatt = round(resultat, 1)
    
    print(f"{resultatt} km")
