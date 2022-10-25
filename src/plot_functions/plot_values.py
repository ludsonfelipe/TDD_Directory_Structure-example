import matplotlib.pyplot as plt


imc_list = [1,2,3,4,5,6]


def imc_plot(imc_list):
    fig, ax = plt.subplots()

    ax.plot(imc_list)
    return fig

