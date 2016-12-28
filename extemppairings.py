# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:54:50 2015

@author: macbook
"""

import random
Extemp_arr=[]
USX_arr=[]
IX_arr= []
Nov_arr= []
Var_arr=[]

txt=open('extemp_roll.txt', 'r')
sort_by = input("Sort by content or experience?")

if sort_by == "content":
    for columns in ( raw.strip().split() for raw in txt ):  
    USX_arr.append(str(columns[1]))
    IX_arr.append(str(columns[2]))

    def FX_NX():
        print"NX:"
        for extemper in USX_arr:
            while len(USX_arr)>0:    
                extemper = random.choice(USX_arr)
                print(extemper)
                USX_arr.remove(extemper)

        print"IX:"
        for extemper in IX_arr:
            while len(IX_arr)>0:
                extemper = random.choice(IX_arr)
                print(extemper)
                IX_arr.remove(extemper)
    FX_NX()
    
if sort_by == "experience":
    for columns in ( raw.strip().split() for raw in txt ):  
    Nov_arr.append(str(columns[0]))
    Var_arr.append(str(columns[1]))

    def Novice_Varsity():
        print "Novice:"
        for extemper in Nov_arr:
            while len(Nov_arr)>0:    
                extemper = random.choice(Nov_arr)
                print(extemper)
                Nov_arr.remove(extemper)
        print "Varsity:"
        for extemper in Var_arr:
            while len(Var_arr)>0: 
                extemper = random.choice(Var_arr)
                print(extemper)
                Var_arr.remove(extemper)
    Novice_Varsity()
