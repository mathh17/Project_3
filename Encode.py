"""
@author: Mathias Østergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""
#%%
import sys
import bitIO as bit
file = open("C:/Users/oeste/OneDrive/Uni/data_2_semester/Algoritmer/Project_3/DelIIITestFilerTilUdlevering/KingJamesBible.txt", 'rb')
b = file.read()
print(len(b))
bit_class = bit.BitWriter(file)
freqTabel = [0]*255
for i in b:
    freqTabel[i] +=1
print(freqTabel)

file.close()
# %%

import PQHeap as pq

def huffmann(C):
    n = len(C)
    Q = C
    for i in range(1, n-1):
        x = pq.extractMin(Q)
        y = pq.extractMin(Q)
        z = x + y
        pq.insert(Q,z)
        return pq.extractMin(Q)
    

# %%

import Element as el


el1 = el(1000)