def simpleCipher(encrypted, k):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    decrypted = ""

    for index in encrypted:
        position = alphabet.index(index)
        new_position = (position - k)
        char = alphabet[new_position]
        decrypted += char
    return decrypted


encrypted = "VTAOG"
k = 2
print(simpleCipher(encrypted, k))
