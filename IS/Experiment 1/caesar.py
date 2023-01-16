def caesarEncrypt(plainText, shift):
    cipherText = ''

    for char in plainText:

        if (char.isupper()):
            cipherText += chr((ord(char) - 65 + shift) % 26 + 65)

        else:
            cipherText += chr((ord(char) - 97 + shift) % 26 + 97)

    return cipherText


text = "ATTACKATONCE"
shift = 4
print ("Text  : " + text)
print ("Shift : ", shift)
print ("Cipher: " + caesarEncrypt(text, shift))