import numpy as np

def weight(x, alpha=0.0):
    return np.exp(-x) * (x ** alpha)

def basis_function(x, t):
    return x**(0.5 + 1j*t)

def kernel(x, y, t_values):
    s = 0.0 + 0.0j
    for t in t_values:
        phi_x = basis_function(x, t)
        phi_y = basis_function(y, t)
        s += phi_x * np.conj(phi_y)
    return s.real

def energy(f, xs, t_values):
    E = 0.0
    for i,x in enumerate(xs):
        for j,y in enumerate(xs):
            w = weight(x)*weight(y)
            K = kernel(x,y,t_values)
            E += K * (f[i]-f[j])**2 * w
    return E.real
