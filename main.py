#entrar no word
#copiar o texto do arquivo modelo
#identificar as areas de preenchimento
#mudar os dados
#variaveis: 
    # nome_vendedor
    # nacionalidade_vendedor
    # estado_civil_vendedor 
    # cpf_vendedor
    # rg_vendedor
    # endereço_completo_vendedor

    # nome_comprador
    # nacionalidade_comprador
    # estado_civil_comprador 
    # cpf_comprador
    # rg_comprador
    # endereço_completo_comprador

    # marca_veiculo
    # cor_veiculo
    # placa_veiculo
    # valor_renavam
    # valor_chassi
    # km_var
    # ano_veiculo

    # valor_total_veiculo
    # valor_total_veiculo_extenso
    # valor_entrada
    # valor_entrada_extenso
    # instituicao_financiamento
    # numero_parcelas
    # valor de valor_cada_parcela
    # valor_cada_parcela_extenso
    # data_vencimento 

import pandas as pd
from pyautogui import click, press, hotkey, PAUSE, write
from time import sleep

def preencher_loc(item):
    cod = tabela.loc[linha, item]
    print(cod)
    hotkey('ctrl', 'u')
    write(str(item))
    sleep(3)
    press('tab')
    write(str(cod))
    sleep(3)
    for n in range(3):
        press('tab')
        sleep(1)
    for n in range(2):
        press('enter')
        sleep(1)
    for n in range(6):
        press('tab')
        sleep(1)
    press('enter')
    sleep(4)

PAUSE = 1
#entrar no word
def entrar_word():
    press("win")
    write("word")
    press("enter")
    sleep(2)

entrar_word()
hotkey("alt", "f4")
entrar_word()
hotkey('ctrl', 'a')
for n in range(3):
    press('tab')
press('enter')
sleep(4)

click(663,392)
hotkey('ctrl', 't')
hotkey('ctrl', 'c')
sleep(5)
hotkey('ctrl', 'o')
hotkey('ctrl', 'v')

tabela = pd.read_excel("dados.xlsx")
for linha in tabela.index:
    for coluna in tabela.columns:
        preencher_loc(coluna)
hotkey('ctrl', 'b')
press('tab')
for n in range(4):
    hotkey('shift', 'down')
press('enter')
vendedor = tabela.loc[1,"nome_vendedor"]
comprador = tabela.loc[1, "nome_comprador"]
write('Contrato de Compra e venda - ',vendedor, " - ", comprador )
press('tab')
hotkey('shift', 'rigth')
for n in range(6):
    hotkey('shift', 'down')
press('enter')