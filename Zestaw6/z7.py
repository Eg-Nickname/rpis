import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import gamma


# Generate normal distribiution using Box-Muller transformation
def gen_normal_dist():
    u1 = np.random.uniform(0, 1.0)
    u2 = np.random.uniform(0, 1.0)
    return np.sqrt(np.log((1.0 / u1) ** 2)) * np.sin(2 * np.pi * u2)


# Generate Chi-Square number
def gen_chi(n: int):
    sum = 0
    for _ in range(n):
        sum += gen_normal_dist() ** 2
    return sum


# Generate histogram with numeric generated data and analytical
def genPlot(a: int, samples: int, bins: int):
    data = np.array([gen_chi(a) for _ in range(samples)])
    plt.hist(
        data, bins, facecolor="#feb24c", alpha=0.7, density=True, label="Numeryczne"
    )

    x = np.linspace(0, data.max(), 1000)
    y = ((x / 2) ** (a / 2 - 1) * np.exp(-x / 2)) / (2 * gamma(a / 2))
    plt.plot(x, y, label="Analityczne")

    plt.grid(True)
    plt.title("Rozkład Chi-wadrat n=" + str(a))
    plt.xlabel("x")
    plt.ylabel("Prawdopodobieństwo")
    plt.xlim(-0.1)
    plt.legend()
    plt.savefig("histogram" + ".png")


if __name__ == "__main__":
    genPlot(3, 1000000, 100)
