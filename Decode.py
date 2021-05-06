"""
@author: Mathias Østergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""

import sys
import Encode
import bitIO

#%%
file = open("DelIIITestFilerTilUdlevering/Koutput.txt", 'rb')
decoded = open("DelIIITestFilerTilUdlevering/Kdecoded.txt", 'wb')
bitstreamout = bitIO.BitWriter(decoded)
bitstreamin = bitIO.BitReader(file)

freqTable = [0]*256
sum_hyp = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    freqTable[i] = x
    sum_hyp += x
    
print("Decoded_____________________")
print(freqTable)




hf = Encode.huffmann(freqTable)
print(sum_hyp)


def bit_traversal(T, sum_hyp):
    if type(T) == int:
        print(T)
        print(sum_hyp)
        return T, sum_hyp
    
    b = bitstreamin.readbit()
    print(b)
    sum_hyp -= 1
    bit_traversal(T[b], sum_hyp)


def decode(hf, sum_hyp):
    while sum_hyp > 0:
        code, sum_hyp = bit_traversal(hf, sum_hyp)
        decoded.write(bytes(code))

decode(hf.data, sum_hyp)
file.close()
decoded.close()
