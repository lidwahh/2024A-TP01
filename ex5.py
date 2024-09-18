#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")

code_medals = input('Chaine représentant les médailles ? ')

lettres_autorisees = {'G', 'S', 'B'}
if set(code_medals) - lettres_autorisees:
    print("Veuillez entrer une chaîne valide. ")
else:
    lettre_G = code_medals.count("G")
    lettre_S = code_medals.count("S")
    lettre_B = code_medals.count("B")
    print(f"{country}:")
    print(f"- {lettre_G} OR\n- {lettre_S} Argent\n- {lettre_B} Bronze")






