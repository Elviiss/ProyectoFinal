#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webbrowser

def menu():
	os.system("cls")
	print('''
 _______  ___  ____   ____   ____
|___ ___|/   \|    \ |    \ |  __|
   | |  |  _  | ``_/ | ``_/ | |__
   | |  | |_| |   \  |   \  |  __|
   | |  |     | |\ \ | |\ \ | |__
   |_|   \___/|_| \_\|_| \_\|____|
	''')
	global opcMenu
	print("\t1. Jugar")
	print("\t2. Donar")
	print("\t3. Salir")
	opcMenu = input("\nBienvenido. Elige una opción: ")

	if opcMenu=="1":
		juego()
	elif opcMenu=="2":
		webbrowser.open("http://google.com")
		menu()
	elif opcMenu=="3":
		input("Hasta luego")
		exit()
	else:
		input("Opción no válida")
		menu()


def juego():
	os.system("cls")
	print("\nTe encuentras en una habitación pequeña, de unos 10 metros cuadrados. Parece un trastero. Las estanterías están cubiertas de polvo. Parece que nadie las ha limpiado en mucho tiempo. Detrás tuya hay una pequeña ventana con barrotes, y delante tuya hay una puerta.\n")
	print("\t1. Mirar por la ventana")
	print("\t2. Salir por la puerta\n\n")
	opcion1 = input("Elige una opción: ")

	if opcion1=="1":
		mirarVentana()
	elif opcion1=="2":
		puerta()
	else:
		input("Opción no válida")
		juego()


def mirarVentana():
	os.system("cls")
	print("\nMiras por la ventana y ves a un montón de soldados durmiendo en unas sillas, en un patio bastante grande. Todos tienen algún tipo de arma. No parecen muy amigables.\n")
	print("\t1. Llamarles la atención para preguntarles dónde estás")
	print("\t2. Callarte para que no se despierten\n\n")
	opcion2 = input("Elige una opción: ")

	if opcion2=="1":
		muerte1()
	elif opcion2=="2":
		input("Permaneces callado")
		juego()
	else:
		input("Opción no válida")
		mirarVentana()


def puerta():
	os.system("cls")
	print("\nTe encuentras en un pasillo alargado. Hay dos puertas; una al final del pasillo, al norte, y otra al principio, al sur. En medio del pasillo hay un cartel que señala con una flecha hacia el norte.\n")
	print("\t1. Atravesar la puerta norte")
	print("\t2. Atravesar la puerta sur\n\n")
	opcion3 = input("Elige una opción: ")

	if opcion3=="1":
		muerte2()
	elif opcion3=="2":
		ganar()
	else:
		input("Opción no válida")
		puerta()


def muerte1():
	os.system("cls")
	print("\nLos soldados se despiertan sobresaltados, y al verte, empiezan a gritar en una lengua extraña. Uno de ellos coge un rifle y te dispara.\n")
	fin()


def muerte2():
	os.system("cls")
	print("\nAtraviesas la puerta y te encuentras en un patio lleno de guardias dormidos, que se despiertan y empiezan a gritar en una lengua extraña. Uno de ellos coge un rifle y te dispara.\n")
	fin()


def ganar():
	os.system("cls")
	print("\nAtraviesas la puerta y te encuentras con un túnel en el que decides meterte. Tras andar durante 15 minutos, empiezas a ver luz al final del túnel. Al salir, te das cuenta de que estás fuera de la torre.\n\n")
	print("¡HAS GANADO!\n")
	input("Pulsa [ENTER] para volver al menu")
	menu()


def fin():
	print('''
 ____   _____   _    _
|  __| |__ __| | \  | |
| |__    | |   |  \ | |
|  __|   | |   | |\`  |
| |     _| |_  | | \  |
|_|    |_____| |_|  \_|
		''')
	input("Pulsa [ENTER] para volver al menu")
	menu()


menu()