EXCEPTION = [' ', '.', ':']  # caractères non alphabétiques a ignorer

# caractères alphabétiques a remplacer
DICTIONNAIRE = [['x', 'e'], ['q', 'p'], ['o', 'r'], ['s', 'o'],
                ['c', 'd'], ['v', 'c'], ['l', 'h'], ['g', 'l'],
                ['n', 'a'], ['i', 's'], ['k', 'i'], ['d', 'n'],
                ['m', 'g'], ['f', 'm'], ['w', 'f'], ['u', 't'],
                ['y', 'u']]


def chercher_texte(repertoire):
    ''' va chercher le fichier donné et restitu une chaine de
    texte correspondant a son contenu '''
    fichier = open(repertoire, 'r')
    res = ''
    for elm in fichier:
        res += elm
    return res


def frequence_lettres(texte):
    ''' renvois les fréquences d'apparitions des caractères d'un texte
    donné '''
    # création d'un dictionnaire de fréquence
    temp = []
    for elm in texte:
        ctrl = [temp[i][0] for i in range(len(temp))]
        if elm not in ctrl:
            temp.append([elm, 1])
        else:
            temp[ctrl.index(elm)][1] += 1

    # tri du dictionnaire de fréquence
    temp2 = [temp[i][1] for i in range(len(temp))]
    freq = []
    while len(freq) != len(temp):
        freq.append(temp[temp2.index(max(temp2))])
        temp2[temp2.index(max(temp2))] = -1
    return freq


def substitution_dechiffrement(texte, dictionnaire):
    ''' remplace toutes les lettres d'un texte par leurs
    substitution en fonction d'un dictionnaire de correspondance '''
    temp = [DICTIONNAIRE[i][0] for i in range(len(DICTIONNAIRE))]
    res = ''
    for elm in texte:
        if elm in temp and elm not in EXCEPTION:
            res += DICTIONNAIRE[temp.index(elm)][1]
        else:
            res += elm
    return res


print(frequence_lettres(chercher_texte('texte_N°2/Texte2.txt')))
print(substitution_dechiffrement(chercher_texte('texte_N°2/Texte2.txt'),
      DICTIONNAIRE))
