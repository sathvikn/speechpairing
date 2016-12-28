# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:00:32 2015

@author: macbook
"""
import random
OO=[]
OA=[]
Expos=[]
OI=[]
OPP=[]
DI=[]
HI=[]
TI=[]
Duo=[]
IX=[]
NX=[]
Imp=[]

txt=open('postings.txt', 'r')
for columns in ( raw.strip().split() for raw in txt ):
    OO.append(str(columns[1]))
    OA.append(str(columns[2]))
    Expos.append(str(columns[3]))
    OI.append(str(columns[4]))
    OPP.append(str(columns[5]))
    DI.append(str(columns[6]))
    HI.append(str(columns[7]))
    TI.append(str(columns[8]))
    Duo.append(str(columns[9]))
    IX.append(str(columns[10]))
    NX.append(str(columns[11]))
    Imp.append(str(columns[12]))
#OO
print "Original Oratory"
print "Section:"
count=0
for speaker in OO:
    while len(OO)>=0:
        count+=1
        speaker=random.choice(OO)
        print str(speaker)
        OO.remove(speaker)
        if count%6==0:
            print"Section:"
#OA
print "Original Advocacy"
print "Section:"
count=0
for speaker in OA:
    while len(OA)>=0:
        count+=1
        speaker=random.choice(OA)
        print str(speaker)
        OA.remove(speaker)
        if count%6==0:
            print "Section:"
#Expos
print "Expository"
print "Section:"
count=0
for speaker in Expos:
    while len(Expos)>=0:
        count+=1
        speaker=random.choice(Expos)
        print(str(speaker))
        Expos.remove(speaker)
        if count%6==0:
            print "Section:"
#OI
print "Oratorical Interp"
print "Section:"
count=0
for speaker in OI:
    while len(OI)>=0:
        count+=1
        speaker=random.choice(OI)
        print(str(speaker))
        OI.remove(speaker)
        if count%6==0:
            print "Section:"
    
#OPP
print "Original Poetry and Prose"
print "Section:"
count=0
for speaker in OPP:
        while len(OPP>=0):
            count+=1
            speaker=random.choice(OPP)
            print(str(speaker))
            OPP.remove(speaker)
            if count%6==0:
                print "Section:"
#HI
print"Humerous Interp"
print "Section:"
count=0
for speaker in HI:
    while len(HI>=0):
        count+=1
        speaker=random.choice(HI)
        print str(speaker)
        HI.remove(speaker)
        if count%6==0:
            print "Section:"
#DI
print "Dramatic Interp"
for speaker in DI:
    while len(DI>=0):
        speaker=random.choice(DI)
        print str(speaker)
        DI.remove(speaker)
        if count%6==0:
            print "Section:"
#TI
print "Thematic Interp"
for speaker in TI:
    while len(TI>=0):
        speaker=random.choice(TI)
        print str(speaker)
        TI.remove(speaker)
        if count%6==0:
            print "Section:"
#Duo
print "Duo Interp"
for speaker in Duo:
    while len(Duo>=0):
        speaker=random.choice(Duo)
        print str(speaker)
        Duo.remove(speaker)
        if count%6==0:
            print "Section:"
#IX
print "International Extemp"
for speaker in IX:
    while len(IX>=0):
        speaker=random.choice(IX)
        print str(speaker)
        IX.remove(speaker)
        if count%6==0:
            print "Section:"
#NX
print "US Extemp"
for speaker in NX:
    while len(NX>=0):
        speaker=random.choice(NX)
        print str(speaker)
        NX.remove(speaker)
        if count%6==0:
            print "Section:"
#IMP
print "Impromptu"
for speaker in Imp:
    while len(Imp>=0):
        speaker=random.choice(Imp)
        print str(speaker)
        Imp.remove(speaker)
        if count%6==0:
            print "Section:"
    

    