from util import formata_numero, porcent
from typer import Typer
from rich import print
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
	dados = yq.Ticker(ticket)
	preco_atual = dados.financial_data[ticket]['currentPrice']
	lucro_bruto = dados.financial_data[ticket]['grossProfits']
	receita_total = dados.financial_data[ticket]['totalRevenue']
	endividamento = dados.financial_data[ticket]['totalDebt']
	fluxo_de_caixa_total = dados.financial_data[ticket]['totalCash']
	fluxo_de_caixa_op = dados.financial_data[ticket]['operatingCashflow']
	fluxo_de_caixa_livre = dados.financial_data[ticket]['operatingCashflow']
	ebitda = dados.financial_data[ticket]['ebitda']
	retorno_sobre_PL = dados.financial_data[ticket]['returnOnEquity']
	retorno_sobre_ativos = dados.financial_data[ticket]['returnOnAssets']
	margem_operacional = dados.financial_data[ticket]['operatingMargins']
	margem_de_lucro = dados.financial_data[ticket]['profitMargins']
	margem_ebitda = dados.financial_data[ticket]['ebitdaMargins']
	crescimento_de_receita = dados.financial_data[ticket]['revenueGrowth']

	tabela = Table(title = f'{ticket}')
	tabela.add_column('Indicadores', justify = 'center')
	tabela.add_column('Valores', justify = 'center')

	tabela.add_row('Preço Atual', f'R${preco_atual:.2f}')
	tabela.add_row('Lucro Bruto', formata_numero(lucro_bruto))
	tabela.add_row('Receita Total', formata_numero(receita_total))
	tabela.add_row('Endividamento Total', formata_numero(endividamento))
	tabela.add_row('Fluxo de Caixa Total', formata_numero(fluxo_de_caixa_total))
	tabela.add_row('Fluxo de Caixa Livre', formata_numero(fluxo_de_caixa_livre))
	tabela.add_row('Fluxo de Caixa Operacional', formata_numero(fluxo_de_caixa_op))
	tabela.add_row('EBITDA', formata_numero(ebitda))
	tabela.add_row('Retorno Sobre PL', porcent(retorno_sobre_PL))
	tabela.add_row('Retorno Sobre Ativos', porcent(retorno_sobre_ativos))
	tabela.add_row('Margem Operacional', porcent(margem_operacional))
	tabela.add_row('Margem de Lucro', porcent(margem_de_lucro))
	tabela.add_row('Margem EBITDA', porcent(margem_ebitda))
	tabela.add_row('Crescimento de Receita', porcent(crescimento_de_receita))

	console = Console()
	console.print(tabela)

@app.command()
def comando() -> None:
	pass

app()
