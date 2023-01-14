# def transposition_cipher(text, key):
#     key = [int(i) for i in key]
#     text = text.replace(" ", "_")
#     print("text: ", text)
#     columns = len(key)
#     rows = (len(text) + columns - 1) // columns
#     print("row: ", rows)

#     totalLength = rows * columns
#     for i in range(totalLength - len(text)):
#         text += "_"

#     matrix = []
#     for i in range(rows):
#         matrix.append([])
#     for i in range(len(text)):
#         matrix[i % rows].append(text[i])

#     print("text: ", text)
#     # print("matrix: ", matrix)
#     for row in matrix:
#         print(row)

#     result = ""
#     temp = ""
#     for i in range(columns):
#         # print("value of i: ", i)

#         temp = ""
#         for j in range(rows):
#             temp += matrix[j][key.index(i+1)]

#         #     print("value of j: ", j)
#         # print("value of key: ", key.index(i+1))
#         # print()

#         result += temp

#     return result


# def transposition_decipher(cipher_text, key):
#     key = [int(i) for i in key]
#     print("\ndecipher end key: ", key)
#     # cipher_text = cipher_text.replace("_", " ")
#     columns = len(key)
#     rows = (len(cipher_text) + columns - 1) // columns

#     matrix = []
#     for i in range(columns):
#         matrix.append([])

#     for i in range(len(cipher_text)):
#         print("key.index(i % columns + 1): ", key.index(i % columns + 1))

#         matrix[key.index(i % columns + 1)].append(cipher_text[i])

#     # print("matrix: ", matrix)
#     for row in matrix:
#         print(row)

#     result = ""
#     for i in range(rows):
#         for j in range(columns):
#             result += matrix[j][i]
#     return result



# if __name__ == '__main__':
#     text = "hello world"
#     key = "4312"
#     print("Text  : " + text)
#     print("Key   : " + key)
#     # print("Cipher: " + transposition_cipher(text, key))
#     cipher_text = transposition_cipher(text, key)
#     print("Cipher: " + cipher_text)

#     print("Decipher: " + transposition_decipher(cipher_text, key))


def Matrix(width, string):
    r = 0
    c = 0
    matrix = [[]]
    for pos, ch in enumerate(string):
        matrix[r].append(ch)
        c += 1
        if c >= width:
            c = 0
            r += 1
            matrix.append([])
    return matrix

def encrypt(string,key):
    matrix=Matrix(len(n),string)
    y=" "
    for num in range (len(key)):
        col = key.index(num+1)
        for row in range(len(matrix)):
            if len(matrix[row]) > col:
                y+=matrix[row][col]
    z=y
    return z


def decmatrix(k,key):
    width=len(key)
    height=len(k) // width
    if height * width <len(k):
        height+=1
    length=len(k)
    matrix = []
    totaladd = 0
    for r in range(height):
        matrix.append([])
        for c in range(width):
            if totaladd >= length:
                break
            matrix[r].append('')
            totaladd += 1

    pos = 0
    for num in range(len(key)):
        column = key.index(num+1)
        row = 0
        while (row < len(matrix)) and (len(matrix[row]) > column):
            matrix[row][column] = k[pos]
            row += 1
            pos += 1
    return matrix

def decrypt(k, key):
    matrix = decmatrix(k,key)
    a = ""
    for r in range(len(matrix)):
        for c in range (len(matrix[r])):
            a += matrix[r][c]
    b=a
    return b

if __name__ == '__main__':
    print("Herschel Menezes C1-151\n")
    # string=input("Enter the string : ")
    string = "enemy attack tonight"
    # n=input("Enter the key :")
    n='31452'
    key =list(n)
    key=[int(i) for i in key]

    k = encrypt(string,key)
    print("The Encrypted message is : {}".format(k))
    m=input("\nEnter the Encrypted message : ")
    l=decrypt(m,key)
    print('The Decrypted message is : {}'.format(l))
