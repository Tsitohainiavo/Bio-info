def calculer_tm_intelligent(sequence):
    # Nettoyage de la séquence
    seq = sequence.upper().strip()
    L = len(seq)
    
    # 1. Comptage des bases
    nGC = seq.count('G') + seq.count('C')
    nAT = seq.count('A') + seq.count('T')
    
    # Vérification de sécurité
    if (nGC + nAT) != L:
        return "Erreur : La séquence contient des caractères invalides."

    # 2. Calcul du %GC
    pourcentage_gc = (nGC / L) * 100

    # 3. Choix de la formule selon la longueur
    if L < 13:
        # Formule de Wallace
        tm = (2 * nAT) + (4 * nGC)
        methode = "Wallace (Séquence courte)"
    else:
        # (Marmur-Doty modifiée)
        tm = 64.9 + 41 * (nGC - 16.4) / L
        methode = "Marmur-Doty (Séquence longue)"

    # Affichage des résultats
    print(f"--- Résultats pour {L} bp ---")
    print(f"Séquence : {seq}")
    print(f"Contenu GC : {pourcentage_gc:.1f}%")
    print(f"Méthode utilisée : {methode}")
    print(f"Température de fusion (Tm) : {tm:.2f} °C")

# --- TESTS ---
print("Test 1 (Court) :")
calculer_tm_intelligent("GATTACA") # 7 bp

print("\nTest 2 (Long) :")
calculer_tm_intelligent("GATCGATCGATCGATCGATC") # 20 bp