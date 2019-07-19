class Vampires: 
    in_coffin = True 
    drank_blood_today = False
    coven = []

    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    @classmethod
    def new_vamp(self, name, age): 
        new_vamp = Vampire(name, age)
        cls.coven.append(new_vamp)

    @classmethod
    def drink_blood(self,name):
        self.drank_blood_today = True 
        return f'{self.name} has fed.'
    
    @classmethod
    def sunrise(cls):
        for vampire in coven[]
            if self.drank_blood_today = False:
                in_coffin = False 
    
    @classmethod
    def sunset (cls): 
        for vamp in cls.coven:
            vamp.in_coffin = False
            vamp.drank_blood_today = False
    

        
    



