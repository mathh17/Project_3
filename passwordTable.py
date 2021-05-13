# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:59:23 2021

@author: Joach
"""

class passwordTable:
    
    def __init__(self):
        self.passwordTable = [0]*256
        
    def build_password_table(self, huffmann_tree):
        passwordTable.inorder(self, huffmann_tree,"")
        return self.passwordTable
    
    def inorder(self, T,password):
        if type(T) == int:
            self.passwordTable[T] = password
        else:
            passwordTable.inorder(self, T[0], password + str(0))
            passwordTable.inorder(self, T[1], password + str(1))