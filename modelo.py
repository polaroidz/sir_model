import math

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

class SIR_Model(object):
    """
    Classe que encapsula o Modelo SIR proposto.

    ...

    Attributes
    ----------
    dados : np.array(np.float64)
        Os dados usados para o calculo do erro quadrático e para
        plotar a simulação a partir do modelo.
    b : float
        Taxa de Contágio da Doença (default 0.998)
    k : float
        Tempo Médio de Recuperação (default 1/4)
    i : float
        Proporção Inicial de Infectados na População (default 0.001)

    Methods
    -------
    predizer(semanas)
    grafico_simulado(semanas)
    grafico_predicao(semanas_predicao)
    erro_quadratico()    
    """
    
    def __init__(self, dados, b = 0.998, k = 1/14, i = 0.001):
        self.dados = dados
        
        self.b = b
        self.k = k
        self.i = i
        
    def predizer(self, semanas):
        """Retorna os dados previstos pelo modelo para as semanas
        informadas no argumento do método.

        Parameters
        ----------
        semanas : int
            número de semanas a serem simulados.        
        """
        i = self.i
        s = 1 - i
        dt = 1

        b = self.b
        k = self.k

        resultado = []

        for t in range(semanas):
            # Aplica o método de Euler para gerar os valores com base 
            # nas semanas.
            st, it = -b*s*i, (b*s - k)*i
            s, i = s + st*dt, i + it*dt

            resultado.append((s,i))

        resultado = np.array(resultado)

        return resultado
    
    def grafico_simulado(self, semanas):
        resultado = self.predizer(semanas)
    
        plt.figure(figsize=(9, 5))

        plt.title("Modelo SIR")
        
        plt.plot(resultado[:,0], label='s(t): Suscetíveis')
        plt.plot(resultado[:,1], label='i(t): Infectados')

        plt.xlabel('Semana Epidemiológica', fontsize=12)
        plt.ylabel('Proporção', fontsize=12)
        
        plt.legend()

        return plt
        
    def grafico_predicao(self, semanas_predicao):
        semanas_dados = len(self.dados)
        
        resultado = self.predizer(semanas_dados + semanas_predicao)        
        resultado[:semanas_dados,1] = self.dados
        
        plt.figure(figsize=(9, 5))
        
        plt.title("Extrapolação dos Dados Reais usando o Modelo")
        
        plt.plot(resultado[:,1], label='i(t): Resultado do Modelo')
        plt.plot(self.dados, label='i(t): Dados Reais')
        
        plt.xlabel('Semana Epidemiológica', fontsize=12)
        plt.ylabel('Proporção de Infectados', fontsize=12)

        plt.legend()

        return plt
    
    def erro_quadratico(self):
        """Calcula o erro quadrático entre os dados fornecidos e o simulado
        pelo modelo dado os parâmetros iniciais (b, k, i).     
        """

        semanas = len(self.dados)
        
        pred = self.predizer(semanas)    
        eq = np.sum((pred[:, 1] - self.dados)**2)
    
        return eq

def simular(k, b, i_0, semanas):
    print(f"Simulando {semanas} semanas com os parametros:")
    print(f"k = {k}, b = {b} e i_0 = {i_0}")

    modelo = SIR_Model([], b=b, k=k, i=i_0)

    plt = modelo.grafico_simulado(semanas)

    plt.savefig("output/simulado.png")

def predizer(dados, k, b, pred_st, pred_ed):
    i_0 = dados[0]
    k = 0.2
    b = 0.515516

    modelo = SIR_Model(dados[:pred_st], b=b, k=k, i=i_0)

    plt = modelo.grafico_predicao(pred_ed - pred_st)

    plt.savefig("output/predicao.png")

def otimizar(dados):
    i_0 = dados[0]

    min_erro = math.inf
    b_model  = 0.998 # taxa de contatio
    k_model  = 1/14 # tempo de recuperacao

    print("Otimizando modelo aos dados usando erro quadrático...")    

    for k in np.linspace(1/15, 1/5, 100):
        for b in np.linspace(0, 5, 1000):
            modelo = SIR_Model(dados, b=b,k=k,i=i_0)
            
            erro = modelo.erro_quadratico()
            
            if erro < min_erro:
                k_model = k
                b_model = b

                min_erro = erro

    modelo = SIR_Model(dados, k = k_model, b = b_model, i=i_0)

    print("\n=================\n")
    print(f"Infectados iniciais: i_0 = {i_0}")
    print(f"Parâmetros Otimizados: k = {k_model}, b = {b_model}")
    print(f"Erro Quadrátio Minímo: {min_erro}")
    print("\n=================\n")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "-m", 
        "--modo", 
        type=str, 
        default="otimizar", 
        required=False,
        choices=["otimizar", "predizer", "simular"]
    )

    parser.add_argument(
        "-e", 
        "--estado", 
        type=str, 
        default="GO", 
        required=False
    )

    parser.add_argument(
        "-st", 
        "--week_start", 
        type=int, 
        default=21, 
        required=False
    )

    parser.add_argument(
        "-ed", 
        "--week_end", 
        type=int, 
        default=32, 
        required=False
    )

    parser.add_argument(
        "-s", 
        "--semanas", 
        type=int, 
        default=5, 
        required=False
    )

    parser.add_argument(
        "-ps", 
        "--pred_st", 
        type=int, 
        default=7, 
        required=False
    )

    parser.add_argument(
        "-pe", 
        "--pred_ed", 
        type=int, 
        default=7+5, 
        required=False
    )

    parser.add_argument(
        "-k",  
        type=float, 
        default=1/14, 
        required=False
    )

    parser.add_argument(
        "-b",  
        type=float, 
        default=0.998, 
        required=False
    )

    parser.add_argument(
        "-i0",  
        type=float, 
        default=0.0199734, 
        required=False
    )


    args = parser.parse_args()

    estado  = args.estado
    week_st = args.week_start
    week_ed = args.week_end
    modo    = args.modo
    k, b, i_0 = args.k, args.b, args.i0
    pred_st = args.pred_st
    pred_ed = args.pred_ed
    semanas = args.semanas

    filepath = './cases-brazil-states.csv'

    brasil_data = pd.read_csv(filepath)

    df = brasil_data[brasil_data["state"] == estado]

    df_agg = df.groupby(["epi_week"]).agg({
        "newCases": "sum",
        "newDeaths": "sum",
        "recovered": "max",
        "totalCases": "max"
    })

    df_agg["recovered"] = df_agg["recovered"].fillna(0)

    df_sub = df_agg.loc[week_st:week_ed]

    print(f"Processado dados entre as semanas epidemiológicas {week_st} e {week_ed}")

    POP = df_sub.loc[week_ed]["totalCases"]
    POP = int(POP)

    print(f"Considerando População total como: {POP}")

    df_sub["S"] = POP - df_sub["totalCases"]
    df_sub["I"] = df_sub["totalCases"] - df_sub["recovered"]
    df_sub["R"] = df_sub["recovered"]

    df_sub["s"] = df_sub["S"] / POP
    df_sub["i"] = df_sub["I"] / POP
    df_sub["r"] = df_sub["R"] / POP

    dados = df_sub["i"].to_numpy()

    if modo == "simular":
        simular(k, b, i_0, semanas)
    elif modo == "predizer":
        predizer(dados, k, b, pred_st, pred_ed)
    else:
        otimizar(dados)

    print("FIM")