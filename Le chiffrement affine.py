def chiffrement_affine(texte, a, b):
    texte = texte.upper().replace(" ", "")
    texte_chiffre = ""

    for lettre in texte:
        if lettre.isalpha():  
            x = ord(lettre) - 65  
            y = (a * x + b) % 26  
            lettre_chiffree = chr(y + 65)
            texte_chiffre += lettre_chiffree
        else:
            texte_chiffre += lettre  

    return texte_chiffre


texte_clair = input("Texte à chiffrer : ")
a_entry=int(input("Veuillez choisir un coefficient : "))
b_entry=int(input("Veuillez choisir une constante : "))
texte_chiffre = chiffrement_affine(texte_clair, a=a_entry, b=b_entry)

print("Texte chiffré :", texte_chiffre)
