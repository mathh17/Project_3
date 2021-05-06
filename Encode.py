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
b = file.read()
print(len(b))
#bit_written = bitstreamout.BitWriter(file)
freqTabel = [0]*256
for i in b:
    freqTabel[i] +=1

print("Encoded freTable _______________________________________")
print(freqTabel)
for i in range(len(freqTabel)):
    bitstreamout.writeint32bits(freqTabel[i])

def PQHeaper(C):
    pq = PQHeap.createEmptyPQ()
    for i in range(len(C)):
        if C[i] != 0:
            e = Element(C[i], i)
            PQHeap.insert(pq, e)
    return pq

def huffmann(C):
    pq = PQHeaper(C)
    n = len(pq)
    Q = pq
    for i in range(0, n-1):
        x = PQHeap.extractMin(Q)
        y = PQHeap.extractMin(Q)
        z = Element(x.key + y.key,[x.data,y.data])

        PQHeap.insert(Q,z)
    return PQHeap.extractMin(Q)


ht = huffmann(freqTabel)

passwordTabel = [0]*256

def inorder(T,password):
    if type(T) == int:
        passwordTabel[T] = password
    else:
        inorder(T[0], password + str(0))
        inorder(T[1], password + str(1))

inorder(ht.data, "")
bytecounter = 0
#print(passwordTabel)
for i in b:
    string = list(passwordTabel[i])
    for j in range(len(string)):
        string[j] = int(string[j])
        bitstreamout.writebit(string[j])
file.close()
# %%
