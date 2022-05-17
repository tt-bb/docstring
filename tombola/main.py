import random


def tirage_tombola(prenoms: list) -> str:
    return prenoms[random.randint(0, len(prenoms) - 1)]


# TEST
utilisateurs = ["John", "Pierre", "Anne", "Sylvie"]
print(tirage_tombola(utilisateurs))
