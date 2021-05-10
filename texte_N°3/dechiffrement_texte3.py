EXCEPTION = [' ', '.', ':', '\'', ',', '?']
# caractères non alphabétiques a ignorer


def chercher_texte(repertoire):
    ''' va chercher le fichier donné et restitu une chaine de
    texte correspondant a son contenu '''
    fichier = open(repertoire, 'r')
    res = ''
    for elm in fichier:
        res += elm
    return res


def rang(lettre):
    ''' renvois le rang d'une lettre donné '''
    return ord(lettre)-96


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


cle_inverse('kyhhep', 'indice')
print(dechiffrement_vigenere(chercher_texte('texte_N°3/Texte3.txt'), 'xova'))
