# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:36:38 2020

@author: user
"""
for i in range(1,10):
    for j in range(1,10):
        if j==9:
            print(j,'*',i,'=',i*j)
        else:
            print(j,'*',i,'=',i*j,end=' ')