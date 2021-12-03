try:
    n = int(input("saisir la tailles de la matrice"))
    M = [[int(input("M =")) for i in range(n)] for j in range(n)]
    indice_max_i = int(0)
    indice_min_i = int(0)
    indice_max_j = int(0)
    indice_min_j = int(0)

    valeur_max = M[0][0]
    valeur_min = M[0][0]

    for i in range(n):
        for j in range(n):
            if M[i][j] >= valeur_max :
                valeur_max = M[i][j]
                indice_max_i = i
                indice_max_j = j

            if M[i][j] <= valeur_min :
                valeur_min = M[i][j]
                indice_min_i = i
                indice_min_j = j

    print("max=", valeur_max, "i =", indice_max_i, "j =", indice_max_j)
    print("min=", valeur_min, "i =", indice_min_i, "j =", indice_min_j)

except ValueError:
    print("Saisie non valide")

