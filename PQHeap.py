# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:58:53 2021

@author: Mathias Østergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""
# Joachim 
# Fjerner elementet i A med laveste prioritet og returnerer det
import element as el

def extractMin(A):
    if len(A) < 1: 
        print("Error heap underflow")
        return -1
    min_e = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    min_heapify(A,0)
    return min_e
    
# Joachim
# Tilføjer e til A i prioritetskøen med laveste prioritet
def insert(A, e):
    i = len(A)
    A.append(e)
    while(i > 0 and A[parent(i)] > A[i]):
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
    
# Joachim - er det seriøst det de mener? 
# returnerer en tom prioritetskø 
def createEmptyPQ():
    return []
    
    
# Mathias  
# returnerer forældren
def parent(i):
    return int((i-1)/2)
    
# Mathias
# returner det venstre child
def left(i):
    return 2*i + 1
    
# Mathias
# returner det højre child
def right(i):
    return 2*i + 2
    
    
# Mathias
# laver minimums heap i listen
def min_heapify(A,i):
    l = left(i)
    r = right(i)
    if(l <= (len(A)-1) and A[l] < A[i]):
        least = l
    else: least = i
    if r <= (len(A)-1) and A[r] < A[least]:
        least = r
    if least != i:
        A[i],A[least] = A[least],A[i]
        min_heapify(A,least)
    

    
    
def heap_min(A):
    return A[0]
    
# Andreas - Den returere ikke det helt rigtige
# indsætter en ny nøgle på en given plads. 
# derefter genoprettes max-heap orden.  
  
def heap_increase_key(A,i,key):
    if key < A[i]:
        print('error - new key is smaller then current key')
    else:
        A[i] = key
        
        while (i > 1 and A[parent(i)] < A[i]):
            A[i], A[parent(i)] = A[parent(i)], A[i]
            i = parent(i)
    return A
    

e1 = el(5,10)
