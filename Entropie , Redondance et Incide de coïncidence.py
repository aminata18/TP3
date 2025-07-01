#entrepie

def entropie(texte_chiffre):
    nbtotal = len(texte_chiffre)
    compteur = {}

    for lettre in texte_chiffre:
        if lettre in compteur:
            compteur[lettre] += 1
        else:
            compteur[lettre] = 1

    entropie_simple = 0
    for lettre in compteur:
        probabilite = compteur[lettre] / nbtotal
        entropie_simple += probabilite  

    return round(entropie_simple, 2)


#redondance

def redondance(texte_chiffre):
    nbtotal = len(texte_chiffre)
    compteur = {}

    for lettre in texte_chiffre:
        if lettre in compteur:
            compteur[lettre] += 1
        else:
            compteur[lettre] = 1

    resultat = 0
    for nbapparitions in compteur.values():
        probabilite = nbapparitions / nbtotal
        resultat += probabilite * probabilite

    return round(resultat, 2)


#indice coincidence

def coincidence(texte_chiffre):
    nbtotal = len(texte_chiffre)
    compteur = {}

    for lettre in texte_chiffre:
        if lettre in compteur:
            compteur[lettre] += 1
        else:
            compteur[lettre] = 1

    total_paires = 0
    for nbapparitions in compteur.values():
        total_paires += nbapparitions * (nbapparitions - 1)

    if nbtotal <= 1:
        return 0

    indice = total_paires / (nbtotal * (nbtotal - 1))
    return round(indice, 2)


#test

textechiffre=input("Le texte à chiffrer est:")

print("Entropie:", entropie(textechiffre))
print("Redondance :", redondance(textechiffre))
print("Indice de coïncidence :", coincidence(textechiffre))
