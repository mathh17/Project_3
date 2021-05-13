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
from passwordTable import passwordTable as pt


def PQHeaper(C):
    pq = PQHeap.createEmptyPQ()
    for i in range(len(C)):
        if C[i]!=0:
            e = Element(C[i], i)
            PQHeap.insert(pq, e)
    return pq

# Makes a huffman tree from a frequency table 
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


# Makes frequency table from filepath
def makeFreqTable(path):
    file = open(path, 'rb')
    freqTabel = [0]*256
    while True:
        b = file.read(1)
        if not b:
            break
        freqTabel[b[0]] +=1
    file.close()
    return freqTabel



# Writes freqTable in 32bits to encoded output file
def writefile(outname, inname, freqTable, ht, passwordTable):
    output = open(outname, 'wb')
    bitstreamout = bitIO.BitWriter(output)
    
    for i in range(len(freqTable)):
        bitstreamout.writeint32bits(freqTable[i])

    file = open(inname, 'rb')    
    while True:
        b = file.read(1)
        if not b:
            break
        string = list(passwordTable[b[0]])
        print(string)
        for j in range(len(string)): 
            string[j] = int(string[j]) 
            bitstreamout.writebit(string[j])
    file.close()
    output.close()
    
    

# inname = sys.argv[1]
# outname = sys.argv[2]

inname = "DelIIITestFilerTilUdlevering/readMe.txt"
outname = "DelIIITestFilerTilUdlevering/readMeEncoded.txt"
freqTable = makeFreqTable(inname)
ht = huffmann(freqTable)
pswt = pt()
passwordTable = pswt.build_password_table(ht.data)   
writefile(outname, inname, freqTable, ht, passwordTable)



        
        



# %%
