#AES

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def chiffrer_AES(texte_clair, cle):
    cipher = AES.new(cle, AES.MODE_CBC)
    texte_clair_bytes = texte_clair.encode()
    texte_clair_padded = pad(texte_clair_bytes, AES.block_size)
    texte_chiffre = cipher.encrypt(texte_clair_padded)
    return cipher.iv, texte_chiffre

def dechiffrer_AES(iv, texte_chiffre, cle):
    cipher = AES.new(cle, AES.MODE_CBC, iv)
    texte_dechiffre_padded = cipher.decrypt(texte_chiffre)
    texte_dechiffre = unpad(texte_dechiffre_padded, AES.block_size)
    return texte_dechiffre.decode()

cle = get_random_bytes(16)  
message = input("Message confidentiel : ")

iv, chiffre = chiffrer_AES(message, cle)
print("Message chiffré :", chiffre)

clair = dechiffrer_AES(iv, chiffre, cle)
print("Message déchiffré :", clair)

#RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generer_cles_RSA():
    cle_privee = RSA.generate(2048)
    cle_publique = cle_privee.publickey()
    return cle_privee, cle_publique

def chiffrer_RSA(message, cle_publique):
    cipher = PKCS1_OAEP.new(cle_publique)
    message_bytes = message.encode()
    return cipher.encrypt(message_bytes)

def dechiffrer_RSA(chiffre, cle_privee):
    cipher = PKCS1_OAEP.new(cle_privee)
    return cipher.decrypt(chiffre).decode()


cle_privee, cle_publique = generer_cles_RSA()
message = input("Message confidentiel : ")

chiffre = chiffrer_RSA(message, cle_publique)
print("Message chiffré :", chiffre)

clair = dechiffrer_RSA(chiffre, cle_privee)
print("Message déchiffré :", clair)
