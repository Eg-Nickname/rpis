import random
import numpy as np
import matplotlib.pyplot as plt


def genVolumes(n, samples):
    nums = np.random.uniform(0, 2.0, samples)
    return np.power(nums, n)


# Analitycznie policzona funkcja gęstości
def density(y, n):
    print(n)
    # n += 1
    # n -= 1
    return (1 / (2 * n)) * np.power(y, (float)(1 - n) / (float)(n))


def genPlot(n: int, samples: int, bins: int, ax):
    data = genVolumes(n, samples)
    ax.hist(data, bins, facecolor="#feb24c", alpha=0.7, density=True)
    x_range = np.linspace(0, 2**n, 70)
    y = [density(x, n) for x in x_range]
    pl = ax.plot(x_range, y, color="#f03b20")

    ax.set_xlabel("V")
    ax.set_title("N" + str(n) + "")
    ax.grid(True)
    return pl


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 5)
    fig.suptitle("x^n density functions", fontsize=16)
    fig.set_figwidth(12)
    plt.ylim(0, 1)
    plots = []
    ns = [2, 3, 4, 5, 20]
    lims = [1, 1, 1, 1, 0.000005]
    i = 0
    for ax in axes:
        plots.append(genPlot(ns[i], 1000000, 30, ax))
        ax.set_ylim(0, lims[i])
        i += 1
    # fig.legend(plots, labels=["Expected", "Generated"], loc="upper right")
    plt.tight_layout()
    plt.savefig("histogram" + ".png")
