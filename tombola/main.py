import random


def tirage_tombola(prenoms: list) -> str:
    """
    La fonction tire au sort une personne de la liste
    :param prenoms: (List) la liste des prénoms
    :return: (Str) le prénom tiré au sort
    """
    return prenoms[random.randint(0, len(prenoms) - 1)]


# TEST
utilisateurs = ["John", "Pierre", "Anne", "Sylvie"]
print(tirage_tombola(utilisateurs))
