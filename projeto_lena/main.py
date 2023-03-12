from util import formata_numero, formata_porcent, formata_preco
from typer import Typer
from rich.console import Console
from rich.table import Table
import yahooquery as yq

app = Typer()

@app.command()
def resumo(ticket: str) -> None:
	"""
		Este comando recebe como argumento o ticket de alguma empresa da B3 e
		retorna uma série de indicadores sobre tal ativo.
	"""
	ticket += '.SA'
	dados = yq.Ticker(ticket)
	chaves_dados = dados.financial_data[ticket].keys()
	indicadores = {
		'currentPrice': ('Preço atual', formata_preco),
		'grossProfits': ('Lucro Bruto', formata_numero),
		'totalRevenue': ('Receita Total', formata_numero),
		'totalDebt': ('Endividamento', formata_numero),
		'totalCash': ('Fluxo de Caixa Total', formata_numero),
		'operatingCashflow': ('Fluxo de Caixa Operacional', formata_numero),
		'EBITDA': ('EBTIDA', formata_numero),
		'returnOnEquity': ('Retorno sobre PL', formata_porcent),
		'returnOnAssets': ('Retorno sobre Ativos', formata_porcent),
		'operatingMargins': ('Margem Operacional', formata_porcent),
		'profitMargins': ('Margem de Lucro', formata_porcent),
		'ebitdaMargins': ('Margem do EBITDA', formata_porcent),
		'revenueGrowth': ('Crescimento da Receita', formata_porcent)
	}

	tabela = Table(title = f'{ticket}')
	tabela.add_column('Indicadores', justify = 'center')
	tabela.add_column('Valores', justify = 'center')

	for indic in indicadores:
		if indic in chaves_dados:
			indic_fmt = indicadores[indic][0]
			funcao_fmt = indicadores[indic][1]
			tabela.add_row(f'{indic_fmt}', funcao_fmt(dados.financial_data[ticket][indic]))

	console = Console()
	console.print(tabela)

@app.command()
def comando() -> None:
	pass

app()
