# Инкапсуляция - Абстракция

from abc import ABC, abstractmethod
import random


class Hero(ABC):

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #Защищенный атрибут
        self._luck = random.randint(0, 100)
        #Приватный атрибут
        self.__crit_dmg = random.randint(0, 100)

    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f'Привет, {self.name}! \n Мой уровень: {self.lvl}')

    def status(self):
        return print(f'LVL: {self.lvl} \n HP: {self.hp}')

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} критический удар!')
        else:
            return print(f"{self.name} базовый удар!")

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} Успешно защищается!")
        else:
            return print(f"{self.name} не смог защититься!")

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f'{self.name} одыхает и востанавливает здорвье. Новое здоровьне: {self.hp}')

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass



# 3. Множественное наследование
# Python решает такие проблемы с помощью механизма порядка
# разрешения методов (Method Resolution Order, MRO)


# Животные
# class Animal:
#     def make_sound(self):
#         return "Издает звук"
# # Летающие
# class Flyable:
#     def move(self):
#         return "Летит"
# # Плавающие
# class Swimmable:
#     def move(self):
#         return "Плавает"
# # Утка
# class Duck(Animal, Flyable, Swimmable):  # Множественное наследование
#     def make_sound(self):
#         return "Кря-кря!"
#
#
#
# print(Duck().make_sound())
# print(Duck.__mro__)


# Алмазная проблема (Diamond Problem):

# class A:
#     def speak(self):
#         print("Я класс A")
#
# class B(A):
#     def speak(self):
#         super().speak()
#         print("Я класс B")
#
# class C(A):
#     def speak(self):
#         super().speak()
#         print("Я класс C")
#
# class D(B, C):  # D наследует от B и C
#     def speak(self):
#         super().speak()
#         print("Я класс D")
#
# d = D()
# d.speak()
# print(D.__mro__)