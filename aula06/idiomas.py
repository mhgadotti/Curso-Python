import unittest

# dicionario de idiomas

esp = {1: 'uno', 2: 'dos', 3: 'tres'}
ing = {1: 'one', 2: 'two', 3: 'three'}
por = {1: 'um', 2: 'dois', 3: 'três'}
linguas = {'espanhol': esp, 'ingles': ing, 'portugues': por}

def check_numero(numero):
	return int == type(numero)

def check_lingua(lingua):
	return lingua in linguas

def check_numero_existente(numero):
	return numero in esp

def check_numero_extenso(numero):

	try:

		if not check_numero(numero) or not check_lingua(lingua):
			return False

		return linguas[lingua][numero]

	except:

		return False	

class Idiomas(unittest.TestCase):

	def teste_valida_numero(self):
		self.assertTrue(check_numero(2))
	def teste_valida_texto(self):
		self.assertFalse(check_numero('A'))
	def teste_valida_nome(self):
		self.assertFalse(check_numero(None))
	def teste_valida_lingua(self):
		self.assertTrue(check_lingua('espanhol'))
	def teste_valida_lingua(self):
		self.assertFalse(check_lingua('francês'))
	def teste_valida_numero_existente(self):
		self.assertTrue(check_numero(3))
	def teste_valida_numero_inexistente(self):
		self.assertFalse(check_numero(10))
	def teste_numero_ingles(self):
		self.assertEqual(check_numero_extenso(2, 'ingles'), 'two')
	def teste_numero_espanhol(self):
		self.assertEqual(check_numero_extenso(2, 'espanhol'), 'dos')
	def teste_numero_portugues(self):
		self.assertEqual(check_numero_extenso(2, 'portugues'), 'dois')
	def teste_numero_inexistente(self):
		self.assertFalse(check_numero_extenso(100, 'portugues'), 'cem')

if __name__ == '__main__':
		unittest.main()	


imput(int("Digite um numero de um a cinco"))
imput(str("Digite seu idioma"))

