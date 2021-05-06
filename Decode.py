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
decodednew = open("DelIIITestFilerTilUdlevering/NewKdecoded.txt", 'w')
bitstreamout = bitIO.BitWriter(decoded)
bitstreamin = bitIO.BitReader(file)

freqTable = [0]*256
sum_hyp = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    freqTable[i] = x
    sum_hyp += x
    
# print("Decoded_____________________")
# print(freqTable)




hf = Encode.huffmann(freqTable)
print(sum_hyp)


def bit_traversal(T):
    if type(T) == int:
        global sum_hyp
        sum_hyp -= 1
        return T
    
    b = bitstreamin.readbit()
    

    return bit_traversal(T[b])


def decode(hf):

    while sum_hyp > 0:
        code = bit_traversal(hf)
        decodednew.write(chr(code))

decode(hf.data)
file.close()
decoded.close()
decodednew.close()
