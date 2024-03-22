# -*- coding: utf-8 -*-
"""
Vorislik

@author: user
"""


''' Super Class '''

class Shaxs:
    
    def __init__(self, ism, familiya, passport, tyil):
        
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        
        info = f"{self.ism}  {self.familiya}.  "
        info += f"Passport seriya: {self.passport}"
        return info
    
    def get_age(self, yil):

        return yil - self.tyil
    

""" Voris Class """

class Talaba(Shaxs):
    
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    