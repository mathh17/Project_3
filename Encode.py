"""
@author: Mathias Østergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""
#%%
import sys
import bitIO
import PQHeap 
from Element import Element

file = open("DelIIITestFilerTilUdlevering/KingJamesBible.txt", 'rb')
output = open("DelIIITestFilerTilUdlevering/Koutput.txt", 'wb')
bitstreamin = bitIO.BitReader(file)
bitstreamout = bitIO.BitWriter(output)
b = file.read(1)
#print(len(b))
bit_written = bitstreamout.BitWriter(file)
freqTabel = [0]*256
for i in b:
    freqTabel[i] +=1
    
    


for i in freqTabel:
    if freqTabel[i] != 0:
        bitstreamout.writeint32bits(freqTabel[i])

pq = PQHeap.createEmptyPQ()
for i in range(len(freqTabel)):
    if freqTabel[i] != 0:
        e = Element(freqTabel[i], [i])
        PQHeap.insert(pq, e)

    

def huffmann(C):
    n = len(C)
    Q = C
    for i in range(0, n-1):
        x = PQHeap.extractMin(Q)
        y = PQHeap.extractMin(Q)
        z = Element(x.key + y.key,[[x],[y]])
        PQHeap.insert(Q,z)
    return PQHeap.extractMin(Q)

ht = huffmann(pq)
print(ht.key)


huffmann(pq)


file.close()
# %%
