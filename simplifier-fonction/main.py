def est_majeur(age):
    """
    La fonction définit si une personne est majeur ou non
    :param age: (int) l'age de la personne à tester
    :return: (bool) retourne True si la personne est majeur, sinon False
    """
    return age >= 18


# TEST
print(est_majeur(18))
