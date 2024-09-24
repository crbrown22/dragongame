wizard = "wizard"
elf = "elf"
human = "human"

wizard_hp = 70
elf_hp = 100
human_hp = 150


wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    character = input("Choose Your Charcter ")
    if character == ("1"):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == ("2"):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == ("3"):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("Unknown Character")
print(f"You Chose the {character} \n Hit Points {my_hp} \n Damage {my_damage}")
while True:
    dragon_hp = dragon_hp - my_damage
    print(
        f"The {character} has damaged the dragon! \n dragon's hit point value is {dragon_hp}")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp-dragon_damage
    print(
        f"The dragon has damaged the {character} \n The {character} hit point value is {my_hp}")
    if my_hp <= 0:
        print(f"The {character} has lost the battle")
        continue
