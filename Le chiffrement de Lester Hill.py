def hill_chiffrement(texte):
    m11, m12, m21, m22 = 1, 2, 3, 5
    texte = texte.upper().replace(" ", "")

    if len(texte) % 2 != 0:
        texte += "X"

    texte_chiffre = ""

    for i in range(0, len(texte), 2):
        lettre1 = ord(texte[i]) - 65
        lettre2 = ord(texte[i+1]) - 65

        chiffre1 = (m11 * lettre1 + m12 * lettre2) % 26
        chiffre2 = (m21 * lettre1 + m22 * lettre2) % 26

        texte_chiffre += chr(chiffre1 + 65) + chr(chiffre2 + 65)

    return texte_chiffre


texte_clair = input("Texte à chiffrer : ")
texte_chiffre = hill_chiffrement(texte_clair)

print("Texte clair :", texte_clair)
print("Texte chiffré :", texte_chiffre)
