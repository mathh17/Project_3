# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:00:45 2021

@author: Joach
"""

import sys
import bitIO as bit
import PQHeap 
from Element import Element


    
def create_freq_table(path):
    file = open(path, 'rb')
    b = file.read()
    freqTable = [0]*256
    for i in b:
        freqTable[i] +=1
        
    file.close()
    
    return freqTable




#%%




output = bit.BitWriter(outfile)
outfile = open("output.txt", 'wb')
for v in freqTable:
    output.writeint32bits(v)


output.close()



path = "DelIIITestFilerTilUdlevering/readMe.txt"
freqTable = create_freq_table(path)

print(freqTable)