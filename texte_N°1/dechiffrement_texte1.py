EXCEPTION = [' ', '.', ':']  # caractères non alphabétiques a ignorer


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


def decalage(lettre_message, lettre_cle):
    ''' décale une lettre en fonction du rang d'une seconde, reviens
    au début de l'alphabet si les rangs additionnés > 26 '''
    res = chr((rang(lettre_message) + rang(lettre_cle))%26 +96)
    if ord(res) == 96:
        res = chr(122)
    return res


def dechiffrement_cesar(text_chiffre, cle):
    ''' décale toute une chaine de texte selon le rang d'une lettre donnée,
    en permettant d'ignorer certains caractères chiffrés. '''
    clair = ''
    for elm in text_chiffre:
        if elm not in EXCEPTION:
            clair += decalage(elm, cle)
        else:
            clair += elm
    return clair


print(dechiffrement_cesar(chercher_texte('texte_N°1/Texte1.txt'), 'a'))
