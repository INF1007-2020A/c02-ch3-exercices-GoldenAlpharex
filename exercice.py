#!/usr/bin/env python
import math

def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	power = voltage**2 / resistance
	return power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y

	# Calculer le produit scalaire
	# Vérifier si == 0
	# Retourner vrai si == 0, faux sinon.
	if v1[0]*v2[0] + v1[1]*v2[1] == 0:
		return True
	else:
		return False

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	total = 0
	amount = 0
	for v in values: # La variable v contient une valeur de la liste.
		if v >= 0:
			total += v
			amount += 1
	return total / amount
	
	
		
def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0
	while value != 0:
		if value >= 20:
			twenties = value // 20
			value = value % 20
		elif value >= 10:
			tens = value // 10
			value = value % 10
		elif value >= 5:
			fives = value // 5
			value = value % 5
		elif value >= 1:
			ones = value
			value = 0

	return (twenties, tens, fives, ones)

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
