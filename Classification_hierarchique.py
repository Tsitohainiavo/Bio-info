from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Imaginons une matrice de distances entre 4 séquences (A, B, C, D)
# Ces distances auraient pu être calculées avec ton script Levenshtein !
# Format : [Séquence 1, Séquence 2, Distance]
distances = [
    [0, 1, 2.0], # Distance entre A et B = 2
    [0, 2, 8.0], # Distance entre A et C = 8
    [0, 3, 9.0], # Distance entre A et D = 9
    [1, 2, 7.0], 
    [1, 3, 8.0],
    [2, 3, 1.0]  # C et D sont très proches !
]

# On crée le lien (linkage) entre les données
# Ici on utilise une forme simplifiée pour l'exemple
from scipy.spatial.distance import squareform
matrice_symetrique = squareform([2, 8, 9, 7, 8, 1])
Z = linkage(matrice_symetrique, method='average')

# On dessine le dendrogramme
plt.figure(figsize=(8, 5))
dendrogram(Z, labels=["Seq_A", "Seq_B", "Seq_C", "Seq_D"])
plt.title("Classification Hiérarchique des Séquences")
plt.ylabel("Distance de Levenshtein")
plt.show()