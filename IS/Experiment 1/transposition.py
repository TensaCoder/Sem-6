def transposition_cipher(text, key):
    key = [int(i) for i in key]
    text = text.replace(" ", "_")
    print("text: ", text)
    columns = len(key)
    rows = (len(text) + columns - 1) // columns
    print("row: ", rows)

    totalLength = rows * columns
    for i in range(totalLength - len(text)):
        text += "_"

    matrix = []
    for i in range(rows):
        matrix.append([])
    for i in range(len(text)):
        matrix[i % rows].append(text[i])

    print("text: ", text)
    # print("matrix: ", matrix)
    for row in matrix:
        print(row)

    result = ""
    temp = ""
    for i in range(columns):
        # print("value of i: ", i)

        temp = ""
        for j in range(rows):
            temp += matrix[j][key.index(i+1)]

        #     print("value of j: ", j)
        # print("value of key: ", key.index(i+1))
        # print()

        result += temp

    return result


def transposition_decipher(cipher_text, key):
    key = [int(i) for i in key]
    print("\ndecipher end key: ", key)
    # cipher_text = cipher_text.replace("_", " ")
    columns = len(key)
    rows = (len(cipher_text) + columns - 1) // columns

    matrix = []
    for i in range(columns):
        matrix.append([])

    for i in range(len(cipher_text)):
        print("key.index(i % columns + 1): ", key.index(i % columns + 1))

        matrix[key.index(i % columns + 1)].append(cipher_text[i])

    # print("matrix: ", matrix)
    for row in matrix:
        print(row)

    result = ""
    for i in range(rows):
        for j in range(columns):
            result += matrix[j][i]
    return result



if __name__ == '__main__':
    text = "hello world"
    key = "4312"
    print("Text  : " + text)
    print("Key   : " + key)
    # print("Cipher: " + transposition_cipher(text, key))
    cipher_text = transposition_cipher(text, key)
    print("Cipher: " + cipher_text)

    print("Decipher: " + transposition_decipher(cipher_text, key))
