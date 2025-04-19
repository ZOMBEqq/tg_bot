import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji(emodji_lenght):
    smile = "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙🥲😚☺️🙂🤗🤩🤔🫡🤨😐😑😶🫥😶‍🌫️🙄😏😣😥😮🤐😯😪😫🥱😴😌😛😜😝🤤😒😓😔😕🫤🙃🫠🤑😲☹️🙁😖😞😟😤😢😭😦😧😨😩🤯😬😮‍💨😰😱🥵🥶😳🤪😵😵‍💫🥴😠😡🤬😷🤒🤕🤢🤮🤧😇🥳🥸🥺🥹🤠🤡"
    emodji = ""
    for i in range(emodji_lenght):
        emodji = random.choice(smile)
    return emodji

import random

def flip_coin(): 
    secret_coin = random.choice(["Орел", "Решка"])
    print("Угадай: Орел или Решка?")
    coin = input("Твой выбор: ").strip().capitalize()
    
    if coin == secret_coin:
        return f"Поздравляю! Ты угадал!"
    else:
        return f"К сожалению, ты проиграл. Я загадал: {secret_coin}."