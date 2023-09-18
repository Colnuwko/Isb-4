import matplotlib.pyplot as plt
import Gen_num
from time import time


def create_graph(data: dict) ->list:
    cores = [1, 2, 3, 4, 5, 6, 7, 8]
    times = []
    for i in cores:
        start = time()
        Gen_num.num_selection(data, i)
        times.append(time() - start)
    return times

def show_plt(cores: list, times: list):
    plt.plot(cores, times)
    plt.xlabel("ядра, шт")
    plt.ylabel("Время, сек")
    plt.show()
