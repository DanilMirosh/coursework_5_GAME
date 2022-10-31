from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=100,
    max_stamina=30,
    attack=30,
    stamina=30,
    armor=10,
    skill=FuryPunch(),
) # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов

ThiefClass = UnitClass(
    name="Вор",
    max_health=50,
    max_stamina=70,
    attack=30,
    stamina=30,
    armor=5,
    skill=HardShot(),
) # TODO действуем так же как и с войном

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}