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
        return f'{self.name} has fed.'
        self.drank_blood_today = True 


