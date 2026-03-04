# import copy

def trouver_tous_les_minima(mat):
    """Trouve toutes les paires (i, j) ayant la distance minimale."""
    min_dist = float('inf')
    paires = []
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            if mat[i][j] < min_dist:
                min_dist = mat[i][j]
                paires = [(i, j)]
            elif mat[i][j] == min_dist:
                paires.append((i, j))
    return paires, min_dist

def resoudre_clustering(noms, mat, historique_actuel, solutions_finales):
    # Condition d'arrêt : il ne reste qu'un seul groupe
    if len(noms) == 1:
        solutions_finales.append(historique_actuel)
        return

    paires, dist_min = trouver_tous_les_minima(mat)

    for (i, j) in paires:
        # 1. Préparation des nouveaux noms et groupes
        noms_restants = [noms[k] for k in range(len(noms)) if k != i and k != j]
        nouveau_bloc = noms[i] + noms[j]
        # On place les anciens devant, le nouveau derrière
        prochains_noms = noms_restants + [nouveau_bloc]

        # 2. Calcul de la nouvelle matrice (Single Linkage)
        nouvelles_distances_vers_bloc = []
        indices_restants = [k for k in range(len(mat)) if k != i and k != j]
        
        for k in indices_restants:
            d_min = min(mat[i][k], mat[j][k])
            nouvelles_distances_vers_bloc.append(d_min)

        nouvelle_mat = []
        for idx_r, origin_r in enumerate(indices_restants):
            ligne = []
            for idx_c, origin_c in enumerate(indices_restants):
                ligne.append(mat[origin_r][origin_c])
            ligne.append(nouvelles_distances_vers_bloc[idx_r])
            nouvelle_mat.append(ligne)
        
        # Ligne pour le nouveau bloc vers lui-même
        nouvelle_mat.append(nouvelles_distances_vers_bloc + [0])

        # 3. Récursion pour explorer ce chemin
        nouvel_historique = historique_actuel + [f"Fusion {noms[i]}-{noms[j]} (d={dist_min}) -> {prochains_noms}"]
        resoudre_clustering(prochains_noms, nouvelle_mat, nouvel_historique, solutions_finales)

# --- DONNÉES ---
noms_init = ["A", "B", "C", "D", "E", "F", "G"]
matrice_init = [
    [0, 4, 2, 7, 6, 8, 15],
    [4, 0, 5, 6, 3, 12, 4],
    [2, 5, 0, 10, 13, 17, 9],
    [7, 6, 10, 0, 18, 20, 10],
    [6, 3, 13, 18, 0, 1, 12],
    [8, 12, 17, 20, 1, 0, 20],
    [15, 4, 9, 10, 12, 20, 0]
]

toutes_les_solutions = []
resoudre_clustering(noms_init, matrice_init, [], toutes_les_solutions)

# --- AFFICHAGE ---
print(f"Nombre de solutions trouvées : {len(toutes_les_solutions)}")
for idx, sol in enumerate(toutes_les_solutions):
    print(f"\n--- SOLUTION {idx + 1} ---")
    for etape in sol:
        print(etape)