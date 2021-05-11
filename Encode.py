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
input = sys.argv[1]
file = open(input, 'rb')
output = open(sys.argv[2], 'wb')
bitstreamin = bitIO.BitReader(file)
bitstreamout = bitIO.BitWriter(output)
freqTabel = [0]*256
while True:
    b = file.read(1)
    if not b:
        break
    freqTabel[b[0]] +=1
file.close()
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

file = open(input, 'rb')
while True:
    b = file.read(1)
    if not b:
        break
    string = list(passwordTabel[b[0]])
    for j in range(len(string)): 
        string[j] = int(string[j]) 
        bitstreamout.writebit(string[j])

file.close()
output.close()
# %%
