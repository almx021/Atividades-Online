def calcular(vivos, salto):
	s = salto

	while len(vivos) > 1:
		if s >= len(vivos):
			s = s % len(vivos)

		vivos.pop(s)
		s += (salto)

	return vivos[0]

casos = int(input())

for i in range(casos):
	n, k = map(int, input().split())

	vivos = list(i + 1 for i in range(n))

	print('Case {}: {}'.format((i + 1), calcular(vivos, k - 1)))