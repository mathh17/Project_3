"""
@author: Mathias Ã˜stergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""
#%%
import sys
import Encode
import bitIO


#%%
file = open("DelIIITestFilerTilUdlevering/Koutput.txt", 'rb')
decoded = open("DelIIITestFilerTilUdlevering/newestdecoded2.txt", 'wb')

bitstreamin = bitIO.BitReader(file)
#bitstreamout = bitIO.BitWriter(decoded)

freqTable = [0]*256
sum_hyp = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    freqTable[i] = x
    sum_hyp += x

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
    while sum_hyp > 0:
        code = bit_traversal(hf)
        decoded.write(bytes([code]))

        if sum_hyp < 5000:
            print(code)

        
decode(hf.data)
file.close()
decoded.close()
print("hello")
# %%
