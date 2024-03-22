# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:23:07 2024

@author: user
"""
# obyektga qiymat qo'shish, qiymatni o'zgartirish

class Talaba:
    def __init__(self, ism, fam, tyil):
        self.ism = ism
        self.fam = fam
        self.tyil = tyil
        self.bosqich = 1 #qiymat qo'shildi
        
    
    # obyektda ko'p amallar method orqali amalga oshiriladi   
    def get_info(self):
        return f"Ism: {self.ism}\nFamiliya: {self.fam}\nKurs: {self.bosqich}"
    
    # method
    def bosqichni_oshir(self):
        if(self.bosqich < 4):
            self.bosqich += 1
            
    def get_name(self):
        return self.ism
        
        
        
class Fan:
    """ Fan nomli klass """
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        self.davomiyligi = 0
        
    def set_davomiylik(self, vaqt):
        """ Fan davoliyligini belgilash """
        self.davomiyligi = vaqt
    
    def add_student(self, student):
        """ Fanga Talaba qo'shish """
        self.talabalar.append(student)
        self.talabalar_soni += 1
        
    def get_info(self):
        return f"Fan nomi: {self.nomi} \nTalabalar soni: {self.talabalar_soni} \nDavomiyligi: {self.davomiyligi} semestr"
        

# obyekt yaratish
fan1 = Fan("matematika")
fan1.set_davomiylik(3)

talaba1 = Talaba("Hasan", "Turdimurotov", 2002)

fan1.add_student(talaba1)

print(fan1.talabalar[0].get_info())
print(fan1.get_info())



        
    