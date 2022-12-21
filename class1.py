class Hero:
    def __init__(self, name, abiliti):
        self.name = name
        self.abiliti = abiliti
class Hero_super(Hero):
    def __str__(self):
        return f'{self.name}'
    def D(self):
        print('it is super hero')
