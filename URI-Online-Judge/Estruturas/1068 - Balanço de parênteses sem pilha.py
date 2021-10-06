while True:
	try:
		contador = 0
		N = input()

		for i in N:
			if i == '(':
				contador += 1
			elif i == ')':
			    if contador == 0:
			        contador = -1
			        break
			    contador -= 1

		if contador == 0:
			print('correct')
		else:
			print('incorrect')

	except EOFError:
		break