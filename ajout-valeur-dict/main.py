employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
i = 1
for item in liste:
    if type(item) == str:
        employes["id-" + "{:02d}".format(i)] = item
        i += 1
print(employes)
