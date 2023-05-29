import numpy as np
import matplotlib.pyplot as plt

k = 1
T = 1


def f(x):
    """Piecewise defined function"""
    result = np.zeros_like(x)

    for i, xi in enumerate(x):
        if 0 <= xi <= 1 / 6:
            result[i] = 12 * xi - 1
        elif 1 / 6 < xi <= 0.5:
            result[i] = -1.5 * xi + 1.25
        elif 0.5 < xi <= 5 / 6:
            result[i] = 1.5 * xi - 0.25
        elif 5 / 6 < xi <= 1:
            result[i] = -12 * xi + 11

    return result


def fourier(N):
    """Calculating Fourier series"""
    T = 1
    n = 1000
    x = np.linspace(0, T, n)

    a0 = 2 / T * np.trapz(f(x), dx=T / n)
    ak = np.zeros(N)
    bk = np.zeros(N)
    for i in range(1, N + 1):
        ak[i - 1] = 2 / T * np.trapz(f(x) * np.cos(2 * np.pi * x * i / T), dx=T / n)
        bk[i - 1] = 2 / T * np.trapz(f(x) * np.sin(2 * np.pi * x * i / T), dx=T / n)

    p = np.zeros_like(x) + a0 / 2
    for i in range(1, N + 1):
        p += ak[i - 1] * np.cos(2 * np.pi * x * i / T) + bk[i - 1] * np.sin(2 * np.pi * x * i / T)

    df = np.sqrt(1 / T * np.trapz((f(x) - p) ** 2, dx=T / n))
    print('Standard deviation', df)

    plt.plot(x, f(x), label='f(x)')
    plt.plot(x, p, label=f'Fourier series {N=}')
    plt.legend()
    plt.text(0, -1, f'{df=}')
    plt.show()


fourier(300)
