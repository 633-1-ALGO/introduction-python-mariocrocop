# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]
val_max = 0 #Valeur maximum
i_x = 0
i_i = 0

#Parcour de la liste et choix du plus grand
for i in range(0,len(tab)):
    for x in range(0,len(tab[i])):
        if tab[i][x] > val_max:
            val_max = tab[i][x]
            i_x = x
            i_i = i

print("La valeur maximum est :", val_max, "et elle se trouve à l'indice : [", i_x, "] [", i_i, "]" )




