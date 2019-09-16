# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]

total = 0

#Calcule du total
for i in A:
    total += i

#Calcule moyenne
moyenne = total/len(A)

print("La moyenne du tableau est de", moyenne)
