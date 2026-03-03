def levenshtein_matrice(seq1, seq2):
    taille_1 = len(seq1) + 1
    taille_2 = len(seq2) + 1

    # 1. Création de la matrice remplie de zéros
    matrice = [[0] * taille_2 for _ in range(taille_1)]

    # 2. Initialisation des bordures (coût des insertions/suppressions)
    for i in range(taille_1): matrice[i][0] = i
    for j in range(taille_2): matrice[0][j] = j

    # 3. Remplissage de la matrice
    for i in range(1, taille_1):
        for j in range(1, taille_2):
            if seq1[i-1] == seq2[j-1]:
                cout = 0
            else:
                cout = 1
            
            # On choisit le chemin le moins coûteux
            matrice[i][j] = min(matrice[i-1][j] + 1,      # Suppression
                                matrice[i][j-1] + 1,      # Insertion
                                matrice[i-1][j-1] + cout) # Substitution

    return matrice[taille_1-1][taille_2-1]

# Test
seq_a = "GAAC"
seq_b = "GTACT"
dist = levenshtein_matrice(seq_a, seq_b)
print(f"Distance de Levenshtein (version matrice) : {dist}")