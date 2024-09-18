import math


water_quantity_str = input("Quelle quantité d'eau faut-il assainir ? ")

try:
    water_quantity = float(water_quantity_str)
    
    if water_quantity.is_integer():
        water_quantity = int(water_quantity)
    else:
        water_quantity1 = round(water_quantity)  

    qt_filtres = math.ceil(water_quantity / 5)  
    qt_lampes = math.ceil((water_quantity / 5) * 3)  
    qt_chlore = (water_quantity / 5) * 0.5  

    
    print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:\n")
    print(f"        \t- Filtre(s) : {qt_filtres}\n")
    print(f"        \t- Lampe(s) UV : {qt_lampes}\n")
    print(f"        \t- Chlore : {qt_chlore}kg")

except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")



