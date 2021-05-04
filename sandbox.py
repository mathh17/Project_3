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

infile = open("DelIIITestFilerTilUdlevering/readMe.txt", 'rb')
outfile = open("outputfile.txt", 'wb')

# Create the BitReader/BitWriter using these files as input/output.
bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)

# First read a full int (i.e., four bytes) from the input file using the
# library method readint32bits.
i = bitstreamin.readint32bits()
print("I:", i)
i = bitstreamin.readint32bits()
# Print the value on screen (probably multi-digit integer, if run on a
# textfile, since four bytes representing some chars are the bit pattern of
# some 32 bit integer).
print("I:", i)

# Write the int again to output file (as same four bytes, so bytes should
# appear again in output file exactly as they were in input file) using the
# library method writeint32bits().
bitstreamout.writeint32bits(i)

# Now read the last bits of input file. Do this bit by bit using the library
# method readbit(). At the same time write them again on the output file using
# the library method writebit(). Note the while-expression going through the
# file until no more bits are available (signaled by readsucces() returning
# false).
bits = ""
while True:
    x = bitstreamin.readbit()
    if not bitstreamin.readsucces():  # End-of-file?
        break
    bitstreamout.writebit(x)
    bits += str(x)

    
print(len(bits)/8)
# Write two bits MORE to output file. This will be padded by the library with
# six 0 bits when closing and flushing the output stream, hence give the
# character '@' (which in ASCII has pattern 01000000).
#
# NOTE: this is ONLY to illustrate the effect of writing a number of bits which
# is not a multiple of eight. In Encode in the project, you should NOT add
# these two bits. However, when writing Huffman codes, you may naturally end up
# in a similar situation (because Huffman codes are not multiples of eight),
# which you should be aware of (you must in Decode avoid reading the bits
# padded by the library when closing the output stream in Encode).
bitstreamout.writebit(0)
bitstreamout.writebit(1)

# Flush the BitWriter (automatically padding output with 0-bits until a full
# number of bytes (i.e, a multiple of eight bits) have been written, as
# described above) and close the files.
bitstreamout.close()
bitstreamin.close()