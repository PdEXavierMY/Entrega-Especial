from random import choice, sample

#El choice es para coger algo aleatorio de dentro de una lista,
#y samplees lo mismo que choice pero para coger mas de una cosa aleatoria

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

#Empieza el juego aquí
print("Empieza el Black Jack")
lista_cartas = list(cartas)

#Jugador

main_jugador = sample(lista_cartas,2)
score_jugador = sum(cartas[carta] for carta in main_jugador)
print("Te han tocado las siguientes cartas:, {} {} >> su score es {}".format(main_jugador[0],main_jugador[1],score_jugador))

#Banca

main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],main_banca[1],score_banca))