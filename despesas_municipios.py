#%%
import requests
import json
import pandas as pd
import random
from collections import defaultdict
import numpy as np


class Despesas_Municipios_Api():
    def __init__(self):
        self.url_municipios = 'https://transparencia.tce.sp.gov.br/api/json/municipios'
        self.url_despesas_endpoint = 'https://transparencia.tce.sp.gov.br/api/json/despesas'
        print('Iniciando...')

class Gerar_Arquivos(Despesas_Municipios_Api):
    def Arquivo_municipios(self):
        ret_municipio = requests.get(self.url_municipios)
        municipio = json.loads(ret_municipio.content)   
        return municipio

    def Lista_municipios(self):
        municipio_json = self.Arquivo_municipios()
        df_municipios = pd.DataFrame(municipio_json)
        lista_municipios = df_municipios['municipio'].values.tolist()
        mun_lista = lista_municipios
        return mun_lista

    def Arquivo_Despesas_Entrada(self, municipio, ano, mes):
        municipio = municipio
        ano = ano
        mes = mes
        retorno_api = f"{self.url_despesas_endpoint}/{municipio}/{ano}/{mes}"
        ret_despesas = requests.get(retorno_api)
        arquivo_despesas = json.loads(ret_despesas.content)
        np.savetxt(f'banco_despesas_{municipio}_{ano}_{mes}.csv', arquivo_despesas, delimiter = ";", fmt ='% s')
        print("Arquivo de despesas criado com sucesso!")  


    def Escolha_aleatoria(self):
        exercicio = [2014, 2015, 2016, 2017, 2018, 2019]
        mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        aleatorio_mun = random.sample(self.Lista_municipios(), 1)
        aleatorio_ano = random.sample(exercicio, 1)
        aleatorio_mes = random.sample(mes, 1)
        return aleatorio_mun, aleatorio_ano, aleatorio_mes  
        
    def Arquivo_Despesas_Aleatorio(self):
        mun = str(self.Escolha_aleatoria()[0]).strip('[]').replace("'", "")
        ano = str(self.Escolha_aleatoria()[1]).strip('[]')
        mes = str(self.Escolha_aleatoria()[2]).strip('[]')
        retorno_api_aleatorio = f"{self.url_despesas_endpoint}/{mun.strip('')}/{ano}/{mes}"
        ret_despesas_aleatorio = requests.get(retorno_api_aleatorio)
        arquivo_despesas_aleatorio = json.loads(ret_despesas_aleatorio.content)
        np.savetxt(f'banco_despesas_{mun}_{ano}_{mes}.csv', arquivo_despesas_aleatorio, delimiter = ";", fmt ='% s')
        print("Arquivo de despesas criado com sucesso!")   

    def Arquivo_Despesas_Ano_Todo_csv(self, municipio):
        municipio = municipio
        ano = [2014, 2015, 2016, 2017, 2018, 2019]
        mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        lista_ano = list()
        df_despesas_unico = pd.DataFrame()
        
        for i_ano in ano: 
            retorno_api_aleatorio = f"{self.url_despesas_endpoint}/{municipio}/{i_ano}/{mes}"

            for i_mes in mes:
                retorno_api_aleatorio = f"{self.url_despesas_endpoint}/{municipio}/{i_ano}/{i_mes}"
                ret_despesas_aleatorio = requests.get(retorno_api_aleatorio)
                arquivo_despesas_aleatorio = json.loads(ret_despesas_aleatorio.content)
                df_despesas_mes = pd.DataFrame(arquivo_despesas_aleatorio)
                df_despesas_unico = df_despesas_unico.append(df_despesas_mes, ignore_index=True)

            lista_ano.append(i_ano)
            df_despesas_unico.to_csv(f'banco_despesas_{municipio}_{i_ano}.csv', sep=';', index=False)

        print(f'Arquivo de Despesas criado com sucesso! \n Município: {municipio} \n Ano: {lista_ano} \n Mês: {mes}')

























# %%
