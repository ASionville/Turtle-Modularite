from random import sample

def couleur_aleatoire():
	'''
	renvoie un code composé d'un # suivi de 6 lettres ou chiffres
	Ce code correspond à une couleur codée en héxadécimal
	'''

	hexa = '0123456789ABCDEF'
	return('#' + ''.join(sample(hexa, 6)))