import pytest
from time import sleep
from src.collect_functions import collect

# Testing the greetings

@pytest.fixture(name='greeting',scope='module') # Desse modo podemos usar a função greeting mais de uma vez guardando o resultado dela em cache
def greeting():
    greeting = 'hello'
    sleep(3)
    return greeting


class TestCollectInfo(object):
    def test_enter_params(self, greeting):
        actual = collect.collect_info('jon',60,1.70,greeting) # usando função greeting
        expected = 'hello Name: jon, Weight: 60.0, Height: 1.7, IMC: 21'
        assert actual == expected, f'actual:{actual}, expected:{expected}'
    
    def test_outer(self, greeting):
        actual = collect.collect_info('jon',60,2.0,greeting) # usando dnv
        expected = 'hello Name: jon, Weight: 60.0, Height: 2.0, IMC: 15'
        assert actual == expected, f'actual:{actual}, expected:{expected}'
     