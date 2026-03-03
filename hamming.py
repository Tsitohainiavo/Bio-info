def distance_hamming(sequence1, sequence2):
    # On vérifie d'abord que les séquences ont la même longueur
    if len(sequence1) != len(sequence2):
        raise ValueError("Les séquences doivent avoir la même taille")
    
    distance = 0
    
    # On parcourt les deux séquences en même temps
    for i in range(len(sequence1)):
        # Si les bases sont différentes à la même position, on ajoute 1
        if sequence1[i] != sequence2[i]:
            distance += 1
            
    return distance

# Exemple d'utilisation avec de l'ADN
adn_a = "GAGCCTACTAACGGGAT"
adn_b = "CATCGTAATGACGGCAT"

resultat = distance_hamming(adn_a, adn_b)
print(f"La distance de Hamming est : {resultat}")