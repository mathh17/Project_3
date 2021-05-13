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
file = open(sys.argv[1], 'rb')
decoded = open(sys.argv[2], 'wb')

bitstreamin = bitIO.BitReader(file)

"""
Build and popluate frequency table
"""
freqTable = [0]*256
sum_hyp = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    freqTable[i] = x
    sum_hyp += x

"""
Call to Huffman Tree from Encode file to make sure its the same algorithm
"""
hf = Encode.huffmann(freqTable)

"""
Recursively traverses the Huffman tree to find the characters stored in leaves
T: Tree
"""
def bit_traversal(T):
    if type(T) == int:
        global sum_hyp
        sum_hyp -= 1
        return T
    b = bitstreamin.readbit()
    return bit_traversal(T[b])

"""
Decodes the Huffman tree
hf: Huffman Tree
"""
def decode(hf):
    while sum_hyp > 1:
        code = bit_traversal(hf.data)
        decoded.write(bytes([code]))

if sum(freqTable) != 0: 
    decode(hf)

file.close()
decoded.close()
# %%
