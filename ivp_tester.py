import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def fun2(t, variables):
    v_1, v_2, theta, phi = variables
    dv_1 = np.cos(theta) * np.sin(theta) * v_2 ** 2
    dv_2 = -2 * (np.cos(theta) / np.sin(theta)) * v_1 * v_2
    d_theta = v_1
    d_phi = v_2
    return [dv_1, dv_2, d_theta, d_phi]


def event(t, U):
    return U[0] + 1

event.terminal = True


V = [1, 1, 1, 1]
tstart = 0
tend = 6
t_start = 0
t = np.arange(0, tend, 0.05)    # create array for t
ts = []
ys = []

while True:
    sol = solve_ivp(fun2, (tstart, tend), V, events=event)
    ts.append(sol.t)
    ts.append(sol.y)
    print(ts[-1])
    if sol.status == 1:
        tstart = sol.t[-1]
        # Reset initial state
        V = sol.y[:, -1].copy()
    else:
        break
