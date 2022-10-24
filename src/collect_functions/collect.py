from src.collect_functions.collect_imc import *


def collect_info(name, weight, height, greetings='hello'):
    name = collect_name(name)
    weight, height = collect_metrics(weight, height)

    imc = weight/(height**2)
    return f'{greetings} Name: {name}, Weight: {weight}, Height: {height}, IMC: {round(imc)}'

