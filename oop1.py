     # -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:24:52 2024

@author: user
"""

# OOP 1

class Talaba:
    def __init__(self, ism, fam, tyil):
        self.ism = ism
        self.fam = fam
        self.tyil = tyil
        
    def tanishtir(self):
        return f"Ismim {self.ism}"

talaba1 = Talaba("Hasan", "Turdimurotov", 2002)

print(talaba1.tanishtir()) 