#%%
from inspect import ClassFoundException
from  despesas_municipios import Gerar_Arquivos

entrada = int(input("Para gerar o arquivo csv com as despesas por munícipio, escolha uma das seguintes opções: \
                Opção 1: Escolher município, ano e mês \
                Opção 2: Gerar de modo aleatório \
                Opção 3: Escolher município e gerar os arquivos de todos os anos e meses em csv \
                Digite 1, 2 ou 3"))

repetir = True

while repetir == True: 
    if entrada == 1:
        municipio = input('Digite o municipio. Exemplo: sao-paulo')
        ano = int(input('Digite algum ano entre 2014 a 2019'))
        mes = int(input('Digite o mês em númerico. Exemplo: 1 para janeiro, 2 para fevereiro, etc'))
        Despesas = Gerar_Arquivos()
        Despesas.Arquivo_Despesas_Entrada(municipio, ano, mes)
    elif entrada == 2:
        Despesas = Gerar_Arquivos()
        Despesas.Arquivo_Despesas_Aleatorio()
    elif entrada == 3:
        Despesas = Gerar_Arquivos()
        Despesas.Arquivo_Despesas_Ano_Todo_csv('atibaia') 
    opcao = int(input("Deseja gerar outro arquivo? Digite 1 sim ou 2 para encerrar"))
    if opcao == 1:
        repetir = True
    else: 
        repetir = False

    



# %%
