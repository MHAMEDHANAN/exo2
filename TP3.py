
"""
TP3 : Un jeu, deux versions
M'HAMED Hanan
"""
import random

def choix():
    """"
    prend un fichier de mots en entree et renvoi un mot au hasard
    parmie les mots du fichier d'entree.
    """
    fich = open('/home/hanan.m-hamed/tp-git/exo2/fich.txt','r')
    liste = fich.read()
    mot = random.choice(liste)
    fich.close()
    return mot

mot = choix()
lettres_trouvee = [mot[0]]
for i in range(len(mot)-1):
    lettres_trouvee.append('_')
lettres_proposees = list(mot)

def affichage(lettres_trouvee):
    return "".join(lettres_trouvee)

def verification(lettres_proposees, lettres_trouvee):
    lettre = input('saisie une lettre')
    if lettre in lettres_proposees:
        for (x,y) in enumerate(lettres_proposees):
            if y == lettre and lettre not in lettres_trouvee:
                lettres_trouvee[x] = lettre
            if y ==lettre and lettre in lettres_trouvee and lettres_trouvee.index(lettre) != x:
                    lettres_trouvee[x] = lettre

def jeu():
    nb_chance = 8
    while nb_chance>0:
        if affichage(lettres_trouvee) == mot:
            return 'bravo'
            break
        verification(lettres_proposees,lettres_trouvee)
        print(affichage(lettres_trouvee))
        nb_chance = nb_chance - 1
        print('il vous reste', nb_chance, 'chance')
    return 'vous etes mort'


print(jeu())