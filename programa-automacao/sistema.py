import pandas as pd # pd = apelido que estou dando para pandas
import win32com.client as win32

def formatar(valor):
    return f'R${valor:,.2f}'

# Importando a base de dados
tabela_vendas = pd.read_excel(r'C:\Users\JOKA\Documents\estudos\python\programa-automacao\Vendas.xlsx') # Armazanando o arquivo excel dentro de uma variável

# Visualizar a base de dados
pd.set_option('display.max_columns', None) # display.max_columns = Mostrar o máximo de colunas / None = Não tem máximo de colunas, me mostre tudo
print(tabela_vendas)

# Faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum() # tabela_vendas[['ID Loja', 'Valor Final']] = Restringindo de 'ID Loja' até 'Valor Final', ignorando os outros / groupby('ID Loja').sum() = Agrupando os shoppings (de modo que cada um apareça 1 vez) e somando o valor final (faturamento)
print(faturamento)

# Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-='*50)

# Ticket Médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame() # Dividindo o valor final somado (dentro da variável faturamento) pela quantidade somada (dentro da variável quantidade) / .to_frame() = Faz a conversão dessa divisão para uma tabela comum, igual as de cima
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'}) # Mudando o nome da tabela de 0 para 'Ticket Médio'
print(ticket_medio)

# Enviar o email com o relatório (código pronto)
outlook = win32.Dispatch('outlook.application') # Tem que ter outlook na máquina
mail = outlook.CreateItem(0) # Criando o email
mail.To = 'joaquimlima0612@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o relatório de vendas por cada loja</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': formatar})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': formatar})}

<p>Qualquer dúvida, estou à disposição.</p>
<p>Att.,</p>
<p>Joaquim</p>
'''

mail.Send()

print('Email Enviado!')