# Problème : Etant donné une variable a et b, on demande de mettre la valeur de a dans b et celle de b dans a
# Contraintes : Ne pas utiliser de valeurs numériques.
# Données : les variables a et b

a = 11
b = 42

print("Variable a :", a)
print("Variable b :", b)

a ,b = b, a

print("Echange des variables...")
print("Variable a :", a)
print("Variable b :", b)
