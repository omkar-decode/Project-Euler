import time
start_time = time.clock()


from langdetect import detect
from langdetect import detect_langs

# the language detection isn't 100% accurate and hence, selects multiple results as possibly English (3 in this case)

def IsEnglish (text):
    detection = detect_langs(text)
    if (len(detection) == 1 and detect(text) == "en"):
        return True

    return False

def Decrypt (encrypted, key):
    n = len(encrypted)
    m = len(key)
    index = 0; pos = 0

    flag = 0
    decrypted = []; ascii = []
    while (index < n):
        xorVal = (encrypted[index]) ^ (key[pos])

        if (xorVal>=32 and xorVal<=122):
            ascii.append(xorVal)
            decrypted.append(chr(xorVal))
        else:
            flag = 1
            break

        pos = (pos+1) % m
        index += 1

    if (flag == 0):
        text = ("".join(decrypted))

        if (IsEnglish(text)):
            return [sum(ascii), text]

    return -1


if __name__ == "__main__":

    fp = open("p059_cipher.txt", "r")
    lines = fp.read().split('\n')

    encryptedText = map(int, lines[0].split(","))
    decryptedSum = []

    for i in xrange(97, 123):
        for j in xrange(97, 123):
            for k in xrange(97, 123):

                key = [i, j, k]
                val = Decrypt(encryptedText, key)

                if (val != -1):
                    decryptedSum.append(val)


    p = len(decryptedSum)
    for i in xrange(p):
        print decryptedSum[i]
        print ""


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"    
    

