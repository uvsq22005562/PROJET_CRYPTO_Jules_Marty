EXCEPTION = [' ', 'M', '\'']
# caractères non alphabétiques a ignorer


def chercher_texte(repertoire):
    ''' va chercher le fichier donné et restitu une chaine de
    texte correspondant a son contenu '''
    fichier = open(repertoire, 'r')
    res = ''
    for elm in fichier:
        res += elm
    return res


def texte_miroir(texte):
    ''' inverse toutes les lignes du texte '''
    # séparation + inversions des lignes
    chaine1 = []
    temp = []
    for elm in texte:
        if elm == '\n':
            temp.reverse()
            chaine1.append(temp)
            temp = []
        else:
            temp.append(elm)
    temp.reverse()
    chaine1.append(temp)
    # remise au format initial
    chaine2 = ''
    for elm in chaine1:
        for elmm in elm:
            chaine2 += elmm
        chaine2 += '\n'
    return chaine2


def texte_en_liste(texte):
    ''' change le format du texte, place chaque ligne dans
    une liste '''
    res = []
    temp = ''
    for elm in texte:
        if elm != '\n':
            temp += elm
        elif len(temp) > 1:
            res.append(temp)
            temp = ''
    return res


def cle_inverse(chiffre, clair):
    ''' renvois la clé permettant de passer d'un texte chiffrer a
    un texte en clair (les deux ayants la meme taille) '''
    res = ''
    for i in range(len(chiffre)):
        temp = rang(clair[i]) - rang(chiffre[i])
        if temp > 0:
            res += chr(temp + 96)
        else:
            res += chr(122 + temp)
    print(res)


def rang(lettre):
    ''' renvois le rang d'une lettre donné '''
    return ord(lettre)-96


def decalage(lettre_message, lettre_cle):
    ''' décale une lettre en fonction du rang d'une seconde, reviens
    au début de l'alphabet si les rangs additionnés > 26 '''
    res = chr((rang(lettre_message) + rang(lettre_cle)) % 26 + 96)
    if ord(res) == 96:
        res = chr(122)
    return res


def dechiffrement_vigenere(texte, cle):
    ''' fait passer une clé sur tout un texte, en décalant chaque
    lettre du texte par chaque lettre de la clé (la clé se répéte) '''
    res = ''
    j = 0
    for elm in texte:
        if elm not in EXCEPTION:
            res += decalage(elm, cle[j])
        else:
            res += elm
        j += 1
        if j == len(cle):
            j = 0
    return res


def dechiffrement_multiple_vigenere(liste_texte, liste_cle):
    ''' déchiffre une liste de texte avec une liste de clé '''
    res = []
    j = 0
    for i in range(len(liste_texte)):
        res.append(dechiffrement_vigenere(liste_texte[i], liste_cle[j]))
        j += 1
        if j == len(liste_cle):
            j = 0
    print(res)


cle_inverse('jum kfj', 'sur les')
keylist = ['izevay', 'yizeva', 'yizeva', 'zevayi', 'vayize', 'ayizev',
           'yizeva', 'evayiz', 'vayize', 'ayizev', 'vayize', 'ayizev',
           'yizeva', 'vayize', 'ayizev', 'izevay', 'ayizev', 'yizeva']
chaine = texte_en_liste(texte_miroir(chercher_texte('texte_N°4/Texte4.txt')))
chaine_finale = dechiffrement_multiple_vigenere(chaine, keylist)
