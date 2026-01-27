"""
Parallel Minority Game - Instantaneous Strategy
"""

import numpy as np
import matplotlib.pyplot as plt
from ran2_generator import Ran2Generator


D = 500
NRUN = 1500
TMAX = 10000
G_VALUES = [0.75, 0.82, 0.875, 0.9, 0.925, 0.95, 0.975,
            1.01, 1.02, 1.035, 1.05, 1.07, 1.1, 1.13, 1.15]

GC = 1.0
NU = 2.0
DELTA = 0.5


def shuffle(array, size, rng, seed):
    for i in range(size - 1, 0, -1):
        j = int(rng.ran2(seed) * (i + 1))
        array[i], array[j] = array[j], array[i]


def simulate_instantaneous(g, rng, seed):
    N = int(g * D)
    activity = np.zeros(TMAX)
    fractions = np.zeros(TMAX)

    for _ in range(NRUN):
        population = [0] * D
        first_choice = [0] * N
        second_choice = [0] * N
        location = [0] * N

        sites = list(range(D))
        shuffle(sites, D, rng, seed)

        for i in range(N):
            if i < D:
                first_choice[i] = sites[i]
            else:
                first_choice[i] = int(rng.ran2(seed) * D)

            while True:
                second_choice[i] = int(rng.ran2(seed) * D)
                if second_choice[i] != first_choice[i]:
                    break

        for i in range(N):
            location[i] = first_choice[i] if rng.ran2(seed) < 0.5 else second_choice[i]
            population[location[i]] += 1

        for t in range(TMAX):
            act = 0
            crowded = 0
            for i in range(D):
                if population[i] > 1:
                    act += population[i] - 1
                    crowded += 1

            activity[t] += act / N
            fractions[t] += crowded / D

            flip = [0] * N
            for i in range(N):
                curr_pop = population[location[i]]
                if curr_pop <= 1:
                    continue

                if location[i] == first_choice[i]:
                    alt_pop = population[second_choice[i]]
                else:
                    alt_pop = population[first_choice[i]]

                if curr_pop > alt_pop:
                    p = ((curr_pop - alt_pop) / 2.0) / curr_pop
                    if rng.ran2(seed) < p:
                        flip[i] = 1

            for i in range(N):
                if flip[i]:
                    population[location[i]] -= 1
                    if location[i] == first_choice[i]:
                        location[i] = second_choice[i]
                    else:
                        location[i] = first_choice[i]
                    population[location[i]] += 1

    return activity / NRUN, fractions / NRUN


def main():
    rng = Ran2Generator()
    seed = [-937126283]
    
    time = np.arange(TMAX)
    all_activity = {}
    all_fractions = {}

    print("Running simulations...")
    for g in G_VALUES:
        print(f"  g = {g}")
        act, frac = simulate_instantaneous(g, rng, seed)
        all_activity[g] = act
        all_fractions[g] = frac

    colors = plt.cm.rainbow(np.linspace(0, 1, len(G_VALUES)))

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    for idx, g in enumerate(G_VALUES):
        ax1.loglog(time[1:], all_activity[g][1:], color=colors[idx])
        ax2.loglog(time[1:], all_fractions[g][1:], color=colors[idx])

    ax1.set_title('Activity vs Time')
    ax2.set_title('Fraction vs Time')

    g_plot = [g for g in G_VALUES if abs(g - GC) > 1e-6]
    
    for idx, g in enumerate(g_plot):
        a = all_activity[g]
        f = all_fractions[g]
        
        eps = abs(g - GC)
        x = time * (eps ** NU)
        y_act = a * (time ** DELTA)
        y_frac = f * (time ** DELTA)
        
        ax3.loglog(x, y_act, color=colors[idx])
        ax4.loglog(x, y_frac, color=colors[idx])

    ax3.set_xlabel(r'$t |g - g_c|^{\nu}$')
    ax3.set_ylabel(r'$A(t) t^{\delta}$')
    ax3.set_title('Activity Collapse')

    ax4.set_xlabel(r'$t |g - g_c|^{\nu}$')
    ax4.set_ylabel(r'$F(t) t^{\delta}$')
    ax4.set_title('Fraction Collapse')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
