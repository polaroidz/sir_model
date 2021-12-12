# Exercício Programa -  Modelo SIR de propagação de doenças infecciosas

### MAP0131 - Laboratório de Matemática Aplicada (02-2021)

#### Integrantes do Grupo

Bruno Kinsch de Lara Campos - NUSP: 12557376

Diego Magalhães Rodrigues - NUSP: 12704028

#### Descrição

Esse notebook consiste na solução ao Exercío Programa da disciplina de Laboratório de Matemática Aplicada do Curso Bacharelado de Estatística da USP. Nele codificamos o modelo baseado em Equações Diferenciais chamado SIR aos dados coletados pelo Ministério da Saúde, juntamente com os das Secretarias Estaduais de Saúde, sobre a pandemia de Covid-19 no Brasil. Mais precisamente, nesse estudo modelamos a evolução da pandemia no Estado de Goiás no seu primeiro pico que compreendeu os dias entre 17/5/2020 e 08/08/2020.


## Modos de Usar


### Modo - Otimização (Padrão)

```
python modelo.py --modo otimizar \
                 --estado GO \
                 --week_start 21 \
                 --week_end 32
```

### Modo - Predição

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

```
python modelo.py --modo simular \
                 --k 0.0714 \
                 --b 0.998 \
                 --i0 0.01 \
                 --semanas 12
```

