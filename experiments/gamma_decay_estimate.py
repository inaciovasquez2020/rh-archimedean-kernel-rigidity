import numpy as np
from src.kernel.compute_kernel import kernel, weight

def gamma(rho_t, rho_tp, xs):
    val = 0.0
    for x in xs:
        for y in xs:
            w = weight(x) * weight(y)
            val += kernel(x, y, [rho_t]) * np.conj(kernel(x, y, [rho_tp])) * w
    return np.abs(val)

xs = np.linspace(0.5, 5.0, 20)
t_vals = np.linspace(1, 20, 10)

results = []
for i,t in enumerate(t_vals):
    for j,tp in enumerate(t_vals):
        if i != j:
            g = gamma(t, tp, xs)
            results.append((abs(t-tp), g))

results.sort()

for d,g in results[:10]:
    print("Δt =", d, "Gamma ≈", g)
