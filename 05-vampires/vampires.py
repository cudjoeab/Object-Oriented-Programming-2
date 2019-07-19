class Vampire: 
    in_coffin = True 
    drank_blood_today = False
    coven = []

    def __init__(self, name, age): 
        self.name = name 
        self.age = age
    
    def __str__(self):
        return f'VAMPIRE name: {self.name}, age:{self.age}, location: {Vampire.in_coffin}, drank today?: {Vampire.drank_blood_today}.'

    
    def new_vamp(self, name, age): 
        new_vamp = Vampire(name, age)
        self.coven.append(new_vamp)
        print(f'Welcome {self.name}, age: {self.age}')

    
    def drink_blood(self):
        self.drank_blood_today = True 
        return f'{self.name} has fed.'
    
    @classmethod
    def sunrise(cls):
        for vampire in cls.coven:
            if vamp.drank_blood_today == False:
                vamp.in_coffin = False 
    
    @classmethod
    def sunset (cls): 
        for vamp in cls.coven:
            vamp.in_coffin = False
            vamp.drank_blood_today = False
    
    def go_home(self):
        print(f'{self.name} has returned to their coffin.')
        self.in_coffin = True
    
bill = Vampire('Bill', 417)
eric = Vampire('Eric', 1325)
pam = Vampire('Pam', 240)
tara = Vampire('Tara', 27)

print(bill)
print(eric)
print(pam)
print(tara)

Vampire.sunset()
print(bill.drink_blood())
print(tara.drink_blood())

tara.go_home()







        
    



