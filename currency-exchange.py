# -*- coding: utf-8 -*-

import urllib2
import ast

def run():
	print("::::::::::::::::::::::::::::::::::::::")
	print(":: C U R R E N C Y  E X C H A N G E ::")
	print("::::::::::::::::::::::::::::::::::::::\n")
	print("¿Que deseas cambiar?\n1) MXN a USD\n2) USD a MXN")
	valor = int(raw_input("->"))
	ammount = int(raw_input("Cantidad a cambiar-> "))
	exchange(valor, ammount)

def exchange(valor, ammount):
	#response = urlopen("https://api.fixer.io/latest")
	if valor == 1:
		b = "MXN"
		f = "USD"
	elif valor == 2:
		b = "USD"
		f = "MXN"
	path = "https://api.fixer.io/latest?base=%s" %(b)
	response = urllib2.urlopen(path)
	data = response.read()
	drt = ast.literal_eval(data)
	print("_____________________________________\n")
	print(" Tarifa al día: {}".format(drt["date"]))
	result = ammount * drt["rates"][f]
	print(" Su cambio es ${} {}".format(result, f))
	print("_____________________________________")
	

if __name__ == '__main__':
	run()