import pytest
from src.plot_functions import plot_values

# proccess to test figures
"""
Decidir argumentos de test
Chamar a função para os argumentos
Converter a figura para PNG
Checkar se a imagem está boa (se não alterar a função)
Salvar a imagem
"""
"""
Na função executa-la
E transformar a imagem png
"""

@pytest.mark.mpl_image_compare
def test_imc_plot():
    value = [1,2,3,4,5,6]
    return plot_values.imc_plot(value)