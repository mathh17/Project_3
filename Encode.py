"""
@author: Mathias Østergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""
#%%
import sys
import bitIO as bit
file = open("C:/Users/oeste/OneDrive/Uni/data_2_semester/Algoritmer/Project_3/DelIIITestFilerTilUdlevering/oneByte.txt", 'rb')
b = file.read()
print(len(b))
bit_class = bit.BitReader(file)
bit_class.read(b)
file.close()
# %%
