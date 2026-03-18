import numpy as np
from src.kernel.compute_kernel import energy

xs = np.linspace(0.5, 3.0, 8)
t_values = [0.0, 1.0, 2.0]
f = np.array([x - np.mean(xs) for x in xs], dtype=float)

E = energy(f, xs, t_values)
print("energy =", E)
assert np.isfinite(E)
