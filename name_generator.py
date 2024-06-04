#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:47:55 2024

@author: madeleinerobertson
"""

import random


def random_naam(namenBestand):
    
    regels=[]
    with open(namenBestand) as file:
        while line := file.readline():
            regel = line.rstrip()
            
            regels.append(regel)              
            
    keuze = random.sample(regels, k=1); 
    
    naamregel = keuze[0]
    naam=naamregel[:-2]
    gender = keuze[0].lstrip().split(" ")[1]
            
    return(keuze[0], naam, gender)



def write_recente_namen(recentBestand, namenBestand, herhaalNummer):
    
    keuzenaam = random_naam(namenBestand);
    naam = keuzenaam[1]
    naamEnGender = keuzenaam[0]
    
    regel = str(naam+"\n");
    
    recenteNamen = open(recentBestand, "r").readlines();

    
    if regel not in recenteNamen: 

        recenteNamen.append(regel);
        f = open(recentBestand, "a");
       
        f.write(regel);
        
        with open(recentBestand, 'w') as f:
            if len(recenteNamen)>=herhaalNummer:
                f.writelines(recenteNamen[len(recenteNamen)-herhaalNummer:])
                
            else: 
                f.writelines(recenteNamen)
                        
        f.close()        
        
        return(keuzenaam)
        
    else:
        print("al geweest")
        return False



def naam_generator(recentBestand, namenBestand, herhaalNummer):
    
    output = False
    while output == False:
        output = write_recente_namen(recentBestand, namenBestand, herhaalNummer)
        
    print(output[0])

    return(output)

naam_generator("RecenteNamenLijst.txt", "NamenLijst.txt", 3)
