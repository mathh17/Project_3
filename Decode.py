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
# file = open(sys.argv[1], 'rb')
# decoded = open(sys.argv[2], 'wb')
# encodedName = sys.argv[1]
# decodedName = sys.argv[2]

encodedName = "DelIIITestFilerTilUdlevering/readMeEncoded.txt"
decodedName = "DelIIITestFilerTilUdlevering/readMeDecoded.txt"

file = open(encodedName, 'rb')
decoded = open(decodedName, 'wb')


bitstreamin = bitIO.BitReader(file)

freqTable = [0]*256
sum_hyp = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    freqTable[i] = x
    sum_hyp += x
hf = Encode.huffmann(freqTable)

def bit_traversal(T):
    if type(T) == int:
        global sum_hyp
        if sum_hyp < 10:
            print(f"________________Sum_hyp:{sum_hyp}___________")
        sum_hyp -= 1
        
        return T
    b = bitstreamin.readbit()
    if sum_hyp < 10:
        print(b)
    return bit_traversal(T[b])
print("__________________________decode table____________________")
print(freqTable)

def decode(hf):
    while sum_hyp > 0:
        code = bit_traversal(hf)
        decoded.write(bytes([code]))

if sum(freqTable) != 0: 
    decode(hf)

file.close()
decoded.close()
# %%
