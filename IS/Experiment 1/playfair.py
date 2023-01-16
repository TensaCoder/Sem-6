rowMatrix = [['a', 'b', 'c', 'd', 'e'],
             ['f', 'g', 'h', 'i', 'k'],
             ['l', 'm', 'n', 'o', 'p'],
             ['q', 'r', 's', 't', 'u'],
             ['v', 'w', 'x', 'y', 'z']]

# create column matrix by transposing of matrix
columnMatrix = [[], [], [], [], []]
for i in range(len(rowMatrix)):
    columnMatrix[0].append(rowMatrix[i][0])
    columnMatrix[1].append(rowMatrix[i][1])
    columnMatrix[2].append(rowMatrix[i][2])
    columnMatrix[3].append(rowMatrix[i][3])
    columnMatrix[4].append(rowMatrix[i][4])


def SameRow(letterPair):
    # check for same row
    for rowLetters in rowMatrix:
        # for i in range(len(letterPair)):
        if (rowLetters.count(letterPair[0]) > 0) and (rowLetters.count(letterPair[1]) > 0):
            # print(letterPair)
            return True

    return False


def sameColumn(letterPair):
    # check for same column
    for rowLetters in columnMatrix:
        if (rowLetters.count(letterPair[0]) > 0) and (rowLetters.count(letterPair[1]) > 0):
            # print(letterPair)
            return True

    return False


def sameSubstitution(matrix, letterPair):
    # select the next letter in the right in the row and perform mod 5 operation if the limit
    # of the row is reached then start from the beginning of the row
    for matrixRow in matrix:
        for i in range(len(letterPair)):
            if matrixRow.count(letterPair[i]) > 0:
                index = matrixRow.index(letterPair[i])
                if index == 4:
                    index = 0
                else:
                    index += 1
                letterPair[i] = matrixRow[index]

    return letterPair


def substitution(matrix, letterPair):
    letterPairIndices = []
    for char in letterPair:
        for i in range(len(matrix)):
            if char in matrix[i]:
                j = matrix[i].index(char)
                letterPairIndices.append([i, j])

    # print(letterPairIndices)

    # swap the letter pair indices only the rows
    letterPairIndices[0][0], letterPairIndices[1][0] = letterPairIndices[1][0], letterPairIndices[0][0]

    # swap the letter pair indices only the columns
    # letterPairIndices[1][1], letterPairIndices[0][1] = letterPairIndices[0][1], letterPairIndices[1][1]

    # print(letterPairIndices)

    for indices in letterPairIndices:
        letterPair[letterPairIndices.index(
            indices)] = matrix[indices[0]][indices[1]]

    return letterPair


def playFair(plaintext):
    intermediateCipher = []
    lengthOfPlaintext = len(plaintext)
    i = 0

    print("Plain Text: ",plaintext)
    
    # Add buffer to the end to make even number of character
    if lengthOfPlaintext % 2 != 0:
        plaintext = plaintext + 'z'

    # Add buffer incase two neighboring characters are the same
    while i < lengthOfPlaintext:
        if plaintext[i] != plaintext[i+1]:
            intermediateCipher.append([plaintext[i], plaintext[i+1]])
            i += 2
        else:
            intermediateCipher.append([plaintext[i], 'z'])
            i += 1

    # print(intermediateCipher)

    # Check for same row or same column
    for letterPair in intermediateCipher:
        if SameRow(letterPair):
            letterPair = sameSubstitution(rowMatrix, letterPair)
            # print("same row")
        elif sameColumn(letterPair):
            # print("same column")
            letterPair = sameSubstitution(columnMatrix, letterPair)
        else:
            # print('Not same row or same column')
            letterPair = substitution(rowMatrix, letterPair)

    # print("Cipher text: ", intermediateCipher)

    cipherText = ''
    for letterPair in intermediateCipher:
        for char in letterPair:
            cipherText += char
        
    print("Cipher text: ", cipherText)


def main():
    # plaintext = input("Enter the plaintext: ")
    plaintext = 'hello'
    playFair(plaintext)


if __name__ == "__main__":
    main()


# plaintext = 'aflkmlo'
# playFair(plaintext)

# print(rowMatrix[0].index("b"))

# print(substitution(rowMatrix, ['a', 'i']))
