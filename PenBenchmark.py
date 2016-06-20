#!/usr/bin/env python

import os
import time
import shutil

s_timePen1 = 0
s_timePen2 = 0

f_timePen1 = 0
f_timePen2 = 0

media_total_pen1 = 0
media_total_pen2 = 0

def Pendrive1():

	print("\nCopia de FicheroPrueba.zip a Pendrive1\n")

	global s_timePen1

	s_timePen1 = 0

	s_timePen1 = time.time() #Para empezar a medir el tiempo antes de la copia


	shutil.copy('/Users/nuria/Desktop/FicheroPrueba.zip', '/Volumes/ADATA UFD/FicheroPrueba.zip') 

	global f_timePen1

	f_timePen1 = 0

	f_timePen1 = time.time() - s_timePen1

	#Para medir el tiempo actual restandole lo que ha tardado de la copia.

	global media_total_pen1

	media_total_pen1 = media_total_pen1 + f_timePen1

	print("\nFicheroPrueba.zip copiado a Pendrive1\n")


def Pendrive2():

	print("\nCopia de FicheroPrueba.zip a Pendrive2\n")

	global s_timePen2

	s_timePen2 = 0

	s_timePen2 = time.time()

	shutil.copy('/Users/nuria/Desktop/FicheroPrueba.zip', '/Volumes/NO NAME/FicheroPrueba2.zip')

	global f_timePen2

	f_timePen2 = 0

	f_timePen2 = time.time() - s_timePen2

	global media_total_pen2

	media_total_pen2 = media_total_pen2 + f_timePen2

	print("\nFicheroPrueba.zip copiado a Pendrive2\n")




#Main

for i in range(5): 

	Pendrive1()

	Pendrive2()

	print("\nTiempo tota:\n")

	print("########################")
	print("Pendrive1")
	print(f_timePen1)
	print("segundos")
	print("########################\n\n")


	print("########################")
	print("Pendrive2")
	print(f_timePen2)
	print("segundos")
	print("########################\n\n")


media_pen1 = 0
media_pen2 = 0

media_pen1 = media_total_pen1 / 5.0 
media_pen2 = media_total_pen2 / 5.0


print("########################")
print("Media copia Pen1")
print(media_pen1)
print("seconds")
print("########################\n\n")


print("########################")
print("Media copia Pen2")
print(media_pen2)
print("segundos")
print("########################\n\n")





