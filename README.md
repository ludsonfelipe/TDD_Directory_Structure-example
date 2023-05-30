# TDD_Directory_Structure
[![Build Status](https://app.travis-ci.com/ludsonfelipe/TDI_Directory_Structure.svg?branch=main)](https://app.travis-ci.com/ludsonfelipe/TDI_Directory_Structure)
[![codecov](https://codecov.io/gh/ludsonfelipe/TDI_Directory_Structure/branch/main/graph/badge.svg?token=W2B38JY5C3)](https://codecov.io/gh/ludsonfelipe/TDI_Directory_Structure)

## Testes com Pytest
Este repositório contém exemplos e informações sobre como utilizar o framework de testes Pytest para testar o seu código.

## O que é o Pytest?
Pytest é um framework de testes em Python que facilita a escrita, organização e execução de testes automatizados. Ele fornece uma sintaxe simples e expressiva para a criação de testes, além de uma série de recursos poderosos, como a detecção automática de testes, geração de relatórios detalhados e integração com outras ferramentas de teste.

Estrutura do repositório
O repositório está organizado da seguinte maneira:
```
|- tests/
   |- test_collect_functions/
        |- test_collect_imc.py
        |- test_collect.py
   |- test_plot_functions/
        |- test_plot_values.py
        |- baseline/
            |- test_imc_plot.png
|- src/
    |- collect_functions/
        |- collect_imc.py
        |- collect.py
    |- plot_functions/
        |- plot_values.py
|- setup.py
|- .travis.yml
|- README.md
|- requirements.txt
```
A pasta tests/ contém os arquivos de teste, cada um correspondendo a um módulo específico do código que está sendo testado. A pasta src se refere aos módulos que serão testados.

Executando os testes
Para executar os testes, você precisa ter o Pytest instalado. Caso ainda não tenha instalado, você pode fazer isso utilizando o seguinte comando.

```pip install pytest```

Após a instalação, você pode executar todos os testes no diretório atual executando o seguinte comando:

```pytest```

Assim seus testes serão executados.
