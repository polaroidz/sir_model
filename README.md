# Exercício Programa -  Modelo SIR de propagação de doenças infecciosas

### MAP0131 - Laboratório de Matemática Aplicada (02-2021)

#### Integrantes do Grupo

Bruno Kinsch de Lara Campos - NUSP: 12557376

Diego Magalhães Rodrigues - NUSP: 12704028

#### Descrição

Esse repositório consiste na solução ao Exercío Programa da disciplina de Laboratório de Matemática Aplicada do Curso Bacharelado de Estatística da USP. Nele codificamos o modelo baseado em Equações Diferenciais chamado SIR aos dados coletados pelo Ministério da Saúde, juntamente com os das Secretarias Estaduais de Saúde, sobre a pandemia de Covid-19 no Brasil. Mais precisamente, nesse estudo modelamos a evolução da pandemia no Estado de Goiás no seu primeiro pico que compreendeu os dias entre 17/5/2020 e 08/08/2020.


## Modos de Usar

### Modo - Otimização (Padrão)

Esse modo é usado para otimizar os dados de um certo estado (Goiás, no caso) numa janela epidemiológica. Ele irá minizar o erro quadrático do modelo SIR e no final imprimir na tela os parâmetros **k** e **b** otimizados.

**Parâmetros:**

| Nome       | Descrição                                                    | Valor Padrão |
| ---------- | ------------------------------------------------------------ | ------------ |
| modo       | O modo de execução. Nesse caso, será o **otimizar**.         | Otimizar     |
| estado     | O estado cujo os dados serão otimizados.                     | GO           |
| week_start | É semana epidemiológica inicial do período a ser considerado. | 21           |
| week_end   | É semana epidemiológica final do período a ser considerado.  | 32           |

**Exemplo:**

```
python modelo.py --modo otimizar \
                 --estado GO \
                 --week_start 21 \
                 --week_end 32
```

### Modo - Predição

Esse modo é usado para predizer os dados a partir de uma janela epidemiológica onde a predição começa a partir de um ponto da janela definido por **pred_st** e até n semanas simuladas até **pred_ed**. O resultado é salvo na pasta **output/predicao.png**.

**Parâmetros:**

| Nome       | Descrição                                                    | Valor Padrão |
| ---------- | ------------------------------------------------------------ | ------------ |
| modo       | O modo de execução. Nesse caso, será o **predizer**.         | predizer     |
| estado     | O estado cujo os dados serão otimizados.                     | GO           |
| week_start | É semana epidemiológica inicial do período a ser considerado. | 21           |
| week_end   | É semana epidemiológica final do período a ser considerado.  | 32           |
| pred_st    | Dentro da janela definida por [week_start, week_end] o índice no qual a prediçao começará no gráfico. Antes da predição são os dados reais do estado. | 7            |
| pred_ed    | A partir do pred_st são as semanas que serão previstas usando as saídas do modelo SIR com os parâmetros k, b | 12           |
| k          | Tempo Médio de Recuperação                                   | 0.0714       |
| b          | Taxa de Contágio da Doença                                   | 0.998        |

**Exemplo:**

```
python modelo.py --modo predizer \
                 --estado GO \
                 --week_start 21 \
                 --week_end 32 \
                 --pred_st 7 \
                 --pred_ed 12 \
                 --k 0.0714 \
                 --b 0.998 \
                 --i0 0.01
```

### Modo - Simulação

Esse modo simula a evolução n semanas da pandemia dado os parâmetros do modelo. Todos dados visualizados são as saídas do modelo.

**Parâmetros:**

| Nome    | Descrição                                               | Valor Padrão |
| ------- | ------------------------------------------------------- | ------------ |
| modo    | O modo de execução. Nesse caso, será o **simular**.     | simular      |
| k       | Tempo Médio de Recuperação                              | 0.0714       |
| b       | Taxa de Contágio da Doença                              | 0.998        |
| i0      | Proporção Inicial de Infectados na População            | 0.01         |
| Semanas | A quantidade de semanas que serão simuladas pelo modelo | 12           |

**Exemplo:**

```
python modelo.py --modo simular \
                 --k 0.0714 \
                 --b 0.998 \
                 --i0 0.01 \
                 --semanas 12
```
