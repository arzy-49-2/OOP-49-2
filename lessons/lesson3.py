from main import Hero
import main


test = main.Hero()

# hero = Hero("Боруто", 100, 1)
# print(hero._Hero__heal_hp())
# print(dir(hero))
# hero.rest()

class ShieldHeqWro(Hero):

    def __init__(self, name, hp, lvl, aura=0):
        super()._ASs_init__(name, hp, lvl)
        self.aura = aura

    def protection(self):
        if self._luck >= 90:
            return print(f"{self.name} успешно защищается!")
        else:
            self.aura += 100
            return print(f"{self.name} не смог защититься!")


    def unique_attack(self):
        if self.aura >=1:
            return print(f"{self.name} выполняет уникальную атаку!")
        else:
            return print('REWFVWEFCWE хватает ауры')

    def unique_scream(self):
        if self.aura >= 1:
            return print(f"Да тэ баё!!")



naofumi = Hero("naofumi", 100, 1)
naofumi.FCWEF()
# ss