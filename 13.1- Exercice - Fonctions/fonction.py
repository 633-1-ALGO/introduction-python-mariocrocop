# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' ', 'z'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def frequenceLettres (tab):
    tab_s = []
    for i in range(len(tab)):
        for x in range(len(tab[i])):
            if tab[i][x] not in tab_s:
                tab_s.append(tab[i][x])
    print("Le tableau de base est :", tab)
    print("Il est composé de..")
    for i in tab_s:
        for x in range(len(tab)):
            if tab[x].count(i) != 0:
                print("Le caractère :", i, tab[x].count(i), "fois")




frequenceLettres(tab_lettres)
