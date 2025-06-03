import random

cartas = [
    {"nome": "Leão", "forca": 8, "velocidade": 6, "inteligencia": 4},
    {"nome": "Elefante", "forca": 9, "velocidade": 3, "inteligencia": 7},
    {"nome": "Cobra", "forca": 4, "velocidade": 9, "inteligencia": 5}
]

carta_jogador = random.choice(cartas)
carta_maquina = random.choice(cartas)

print("Sua carta:", carta_jogador)
atributo = input("Escolha um atributo (forca, velocidade, inteligencia): ")

if carta_jogador[atributo] > carta_maquina[atributo]:
    print("Você venceu!")
elif carta_jogador[atributo] < carta_maquina[atributo]:
    print("Você perdeu!")
else:
    print("Empate!")

print("Carta da máquina:", carta_maquina)
