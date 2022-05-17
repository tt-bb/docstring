def additionner_valeurs_dictionnaires(dictionnaire):
    """
    La fonction additionne les valeurs d'un dictionnaire
    :param dictionnaire: (Dict) dictionnaire dont on doit additionner les valeurs
    :return: (Int) somme des valeurs du dictionnaire
    """
    resultat = 0
    for valeur in dictionnaire.values():
        resultat += valeur
    return resultat


employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
print(additionner_valeurs_dictionnaires(employes))
