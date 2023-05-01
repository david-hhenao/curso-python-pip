# Proyecto del curso: Fundamentos de Python
# Estudiante: David Hernando Henao

import random, os, time

#Parámetros y variables

opciones = ("piedra","papel","tijera") #Opciones de la pc
jugadores =("PC","USUARIO","EMPATE")
puntajePC = 0 #Puntaje de la pc
puntajeUsuario = 0 #Puntaje del usuario
ronda = 1 #Ronda inicial
ganador = jugadores[2]

while True:
  #inicio del código
  os.system("clear")
  print("*-*-"*15)
  print("\n\t\t\t\t\t\tRONDA",ronda)
  print()
  print("*-*-"*15)
  print()
  print(f"\t\tPuntuación USUARIO: {puntajeUsuario} \t\tPuntuación PC: {puntajePC}\n\n")

  if puntajePC == 3 or puntajeUsuario == 3:
    os.system("clear")
    print("*-*-"*15)
    print("\n\t\t\t\t\tFIN DEL JUEGO")
    print()
    print("*-*-"*15)
    print()
    print(f"\t\tPuntuación USUARIO: {puntajeUsuario} \t\tPuntuación PC: {puntajePC}\n\n")
    print(f"\t\t\t\t {ganador} GANA LA PARTIDA\n\n")
    print("*-*-"*15)
    time.sleep(3)
    break

  print()
  opcionUsuario = input("Ingrese el la opción: ").lower()

  if not opcionUsuario in opciones:
    if opcionUsuario == "xxx":
      os.system("clear")
      break
    print("\nPor favor ingrese una opción válida")
    time.sleep(2)
    continue

    
  opcionPC = random.choice(opciones)
  print(f"\nOpción PC: {opcionPC}") 
  ronda+=1
  
  if opcionUsuario == opcionPC:
    print("\n\t\t\t\t\t\t\tEMPATE")
    ganador = jugadores[2]
    time.sleep(3)
    continue

  elif opcionUsuario == opciones[0]: #piedra
    if opcionPC == opciones[1]: #papel
      ganador = jugadores[0]
    else: #tijera
      ganador = jugadores[1]
  
  elif opcionUsuario == opciones[1]: #papel
    if opcionPC == opciones[2]: #tijera
      ganador = jugadores[0]
    else: #piedra
      ganador = jugadores[1]

  elif opcionUsuario == opciones[2]: #tijera
    if opcionPC == opciones[0]: #piedra
      ganador = jugadores[0]
    else: #papel
      ganador = jugadores[1]

  if ganador == jugadores[0]:
    puntajePC+=1
  elif ganador == jugadores[1]:
    puntajeUsuario+=1

  if ganador != jugadores[2]:
    print(f"\n\t\t\t\t\t\t{ganador} GANA")
  
  time.sleep(3)