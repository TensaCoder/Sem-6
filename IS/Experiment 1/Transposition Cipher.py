import random
import copy
import math

class TransposCipher():
    def __init__(self, key, plaintext,repeat=1):
        if set(str(key)) == set([str(i) for i in range(1,len(str(key))+1)]) and len(str(key)) == int(max(str(key))):#checking if key is correct
            self.key = key
        else:
            raise ValueError("The key entered is incorrect. It should contain all digits from 1 to n, where n is no. of digits of key. Pls try again")
        self.repeat = repeat
        self.plaintext = plaintext.replace(' ','')#removing blank spaces

    def create_block(self):
        cols = len(str(self.key))#cols = no. of digits in key
        block = []
        i = 0
        while i<len(self.plaintext):
            if i+cols < len(self.plaintext):#append all rows without padded chars
                block.append(list(self.plaintext[i:i+cols]))
                
            else:
                l1 = list(self.plaintext[i:len(self.plaintext)])#l1 has remaining elements in plaintext
                for k in range(cols-len(l1)):#remaining random chars from a-z is padded in l1
                    l1.append(chr(random.randint(97,122)))
                block.append(l1)#l1 row is appended
            i+=cols
        return block

    def cipher(self):
        out = ''
        for i in range(len(str(self.key))):#if key=536, ['5','3','6']
            i = int(list(str(self.key)).index(str(i+1)))#we need to print the column labelled as 1 first, not the 3rd colum if key = 312
            for j in range(len(self.block)):
                out += (self.block[j][i])
        return out

    def encrypt(self):#the method which will be called to encrypt
        for i in range(self.repeat):
            self.block = self.create_block()
            self.plaintext = self.cipher()
        return self.plaintext

    def column_block(self):
        self.collen = math.ceil(len(self.plaintext)/len(str(self.key)))#length of each column
        colblock = []
        kl = len(str(self.key))#no. of digits in key
        for i in range(kl):#we are assuming the columns to be in the list. List contains 'kl' column elements not rows
            colblock.append(list(self.plaintext[i*self.collen:(i+1)*self.collen]))#We append collen number of elements to colblock everytime
        
        temp = copy.deepcopy(colblock)#since we modify colblock it will change temp also, hence we need to use deepcopy
        for i in range(kl):#rearranging the columns according to the key
            colblock[i] = temp[int((str(self.key))[i])-1]#Simply changing the ith column of colblock with the (key[i]-1) column in colblock reverses the columns
        self.colblock = colblock
        return colblock

    def decrypt(self):#the method to be called to decrypt
        for i in range(self.repeat):#decrypting the ciphertext repeat no. of times
            self.colblock = self.column_block()
            out = ''
            for i in range(self.collen):#We are printing the rows from the list of columns which we have
                for j in range(len(str(self.key))):
                    out += self.colblock[j][i]
            self.plaintext = out
                
        return self.plaintext


msg = input("Enter the plaintext: ")
n = int(input("Enter the number of times you want to re-encrypt: "))
key = int(input("Enter the key: "))

t1 = TransposCipher(key,msg,n)
encrypted = t1.encrypt()

print("The ciphertext is: " + encrypted)

print("\nThe rectangular block is: ")
for i in t1.block:#use t1.block only after executing t1.run()
    for j in i:
        print(j, end=' ')
    print()

t2 = TransposCipher(key,encrypted,n)
decrypted = t2.decrypt()
print("The decryption is: "+decrypted)

