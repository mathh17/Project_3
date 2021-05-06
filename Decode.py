"""
@author: Mathias Ã˜stergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""

import sys
import Encode
import bitIO

#%%
file = open("DelIIITestFilerTilUdlevering/Koutput.txt", 'rb')
decoded = open("DelIIITestFilerTilUdlevering/Kdecoded.txt", 'wb')


bitstreamin = bitIO.BitReader(file)

freqTable = [0]*256
sum_hyp = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    freqTable[i] = x
    sumhyp += x

# print("Decoded__")
# print(freqTable)




hf = Encode.huffmann(freqTable)


def bit_traversal(T):
    if type(T) == int:
        global sum_hyp
        sum_hyp -= 1
        return T
    b = bitstreamin.readbit()
    return bit_traversal(T[b])


def decode(hf):
    last_char = 0
    while sum_hyp > 0:
        code = bit_traversal(hf)
        if code == 10 and last_char == 10:
            print(code)
        decoded.write(bytes(code))
        last_char = code

decode(hf.data)
file.close()
decoded.close()
print("hello")