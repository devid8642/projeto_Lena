def formata_numero(numero: int | float) -> str:
	numero = str(int(numero))
	numero_formatado = []
	count = 0

	for c in range(len(numero) - 1, -1, -1):
		numero_formatado.insert(0, numero[c])
		count += 1
		if (count % 3 == 0):
			numero_formatado.insert(0, ' ')

	del numero
	numero = ''

	for c in numero_formatado:
		numero += c

	return f'R${numero.strip()}'

def porcent(valor: float) -> str:
	return f'{round(valor * 100, 2):.2f}%'
