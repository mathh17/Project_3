# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:59:23 2021

@author: Joach
"""
from Element import Element

"""
Creates a password object from a frequency table 

"""
class passwordTable:
    
    def __init__(self, freqTable):
        self.freqTable = freqTable
        self.passwordTable = [0]*256
"""
Builds a passwordtable from a huffmantree
    huffmann_tree: a huffmantree of type Element
    returns a passwordtable with codes for each item in the huffmantree

"""       
    def build_password_table(self, huffmann_tree):
        if sum(self.freqTable) != 0: 
            passwordTable.inorder(self, huffmann_tree.data,"")
        return self.passwordTable
    
    def inorder(self, T,password):
        if type(T) == int:
            self.passwordTable[T] = password
        else:
            passwordTable.inorder(self, T[0], password + str(0))
            passwordTable.inorder(self, T[1], password + str(1))