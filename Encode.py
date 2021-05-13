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

"""
Makes a priority quoue from a frequency table
Takes 1 argument
    C: a frequency table
    returns a priority quoue 

"""
def PQHeaper(C):
    pq = PQHeap.createEmptyPQ()
    for i in range(len(C)):
        if C[i]!=0:
            e = Element(C[i], i)
            PQHeap.insert(pq, e)
    return pq

"""
Makes a huffman tree from a frequency table using a priority quoue 
Takes 1 argument
    C: a frequency table
    returns a huffmantree

"""
# 
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

"""
Makes frequency table from filepath
Takes 1 argument
    path: a string with the path for the inputfile
    returns a list of character frequancies from the path file 

"""
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


"""
Writes freqTable in encoded output file, and then appends the passwords for each 
character in the input file.

 Takes 5 arugments
     outname: A string with the path and the name of the output file
     inname: A string with the path and the name of the input file
     freqtable: A list of char frequencies from file
     ht: a huffmantree made from elements from Element Class
     passwordTable: A list of passwordstrings as strings expressed in 0's and 1's
"""

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

inname = "DelIIITestFilerTilUdlevering/empty.txt"
outname = "DelIIITestFilerTilUdlevering/emptyEncoded.txt"
freqTable = makeFreqTable(inname)
ht = huffmann(freqTable)
pswt = pt(freqTable)
passwordTable = pswt.build_password_table(ht)
writefile(outname, inname, freqTable, ht, passwordTable)



        
        



# %%
