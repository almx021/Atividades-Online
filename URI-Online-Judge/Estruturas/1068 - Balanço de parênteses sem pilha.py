while True:
	try:
		p1 = 0
		N = input()

		for x in N:
			if x == '(':
				p1 += 1
			elif x == ')':
			    if p1 == 0:
			        p1 -= 1
			        break
			    p1 -= 1

		if p1 == 0:
			print('correct')
		else:
			print('incorrect')

	except EOFError:
		break