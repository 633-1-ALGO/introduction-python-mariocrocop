# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

#Nombre d'occurence
x = texte.count("exemple")
print(x)

#Remplacement
texte2 = texte.replace("est", "représente")
print(texte)
print(texte2)

print(texte[::-1])
