"""
@author: Mathias Ã˜stergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""
#%%
import sys
import bitIO as bit
import PQHeap 
from Element import Element

#file = open("C:/Users/oeste/OneDrive/Uni/data_2_semester/Algoritmer/Project_3/
file = open("DelIIITestFilerTilUdlevering/readMe.txt", 'rb')

b = file.read()
#print(len(b))
bit_class = bit.BitWriter(file)
freqTabel = [0]*255
for i in b:
    freqTabel[i] +=1

pq = []
for i in range(len(freqTabel)):
    e = Element(freqTabel[i], [i])
    PQHeap.insert(pq, e)
    
while len(pq) > 0:
    # Udtag det Element fra prioritetskøen, som har mindste key.
    e = PQHeap.extractMin(pq)
    # Tilgå og print dets felter key og data.
    extractedKey = e.key
    extractedData = e.data
    print(extractedKey)
    print(extractedData)




def huffmann(C):
    n = len(C)
    Q = C
    for i in range(0, n-1):
        x = PQHeap.extractMin(Q).key
        y = PQHeap.extractMin(Q).key
        z = Element(x+y,[[x],[y]])
        PQHeap.insert(Q,z)
    return PQHeap.extractMin(Q)



huffmann(pq)


file.close()
# %%

from Element import Element
import PQHeap


el1 = Element(1000, [97])

pq = []
PQHeap.insert(pq,el1)

e = PQHeap.extractMin(pq)
extractedKey = e.key
extractedData = e.data
print(extractedKey)
print(extractedData)