import random
import numpy as np
import matplotlib.pyplot as plt
import math

# Feneratetes numbers from FPG distribiution
def genFromFGP() -> float:
    # Calculated from inverse of distribiution function and normal dist
    uniform_dist = random.random()
    # x in (0, 1/6] sqrt(6x)-1
    if uniform_dist <= 1.0/6.0:
        return math.sqrt(6*uniform_dist)-1
    # X in (1/6, 5/6] 3x-1/2
    elif uniform_dist <= 5.0/6.0:
        return 3*uniform_dist - 1.0 / 2.0
    # x in (5/6,1] 3 - sqrt(6-6x)
    else:
        # random_fgp = 3
        return 3 - math.sqrt(6-6*uniform_dist)

# Generate fgp samples
def genFGP_range(sample_count: int) -> list[float]:
    return [genFromFGP() for _ in range(sample_count)]

# density function of FGP
def density(x: float) -> float:
    if x <= -1:
        return 0
    elif x <= 0:
        return x/3 + 1/3
    elif x <= 2:
        return 1/3
    elif x <=3:
        return (-x)/3 + 1
    else:
        return 0

# Plot hisogram of sampled data
def genPlot(samples: int, bins: int, ax):
    data = genFGP_range(samples)
    ax.hist(data, bins, facecolor='#feb24c', edgecolor='black', alpha=0.7, density=True) 
    x_range = np.linspace(-1.5, 3.5, 100)
    y = [density(x) for x in  x_range]
    pl = ax.plot(x_range, y, color='#f03b20')

    ax.set_xlabel('X')
    ax.set_ylabel('Probability')
    ax.set_title('FGP Samples='+str(samples)+'')
    ax.grid(True)
    return pl


if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    fig.suptitle('FGP Distribiution Histograms', fontsize=20)
    fig.set_figwidth(10)
    pl1 = genPlot(1000, 30, ax1)
    pl2 = genPlot(100000, 30, ax2)
    fig.legend([pl1, pl2], labels=["Expected", "Generated"], loc="upper right")
    plt.savefig('histogram'+'.png')

