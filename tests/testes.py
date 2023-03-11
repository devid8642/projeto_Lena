from projeto_lena.util import formata_numero

def testa_formata_numero() -> None:
	assert formata_numero(0) == 'R$0'
	assert formata_numero(12.45) == 'R$12' 
	assert formata_numero(455) == 'R$455'
	assert formata_numero(4555555) == 'R$4 555 555'
	assert formata_numero(0.42342) == 'R$0'
