from pandas import plotting 
from matplotlib import pyplot as plt

def plot_matrix(data):
    plotting.scatter_matrix(data, figsize=(10, 10), alpha=0.5)
    plt.show()