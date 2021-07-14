import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import conversion_formulas

ts = []
ys = []

# u_list = [0, 1, 2]
# breaking = False


# Define event function and make it a terminal event
def event(t, u, r_s):
    # u_list.append(u[1])
    # if u_list[-3] == u_list[-2] == u_list[-1] == u[1]:
    #    global breaking
    #    breaking = True
    #    print('Yeet')
    #    print(u[1])
    X, Y, Z = conversion_formulas.spherical_to_cartesian(u[1], u[2], u[3])
    return Z - 10


def event2(t, u, r_s):
    return r_s - u[1]


event.terminal = True


def fun3(t, variables, r_s):
    t, r, theta, phi, v_zero, v_one, v_two, v_three = variables
    d_v_zero = - r_s / (r * (r - r_s)) * v_zero * v_one
    d_v_one = - (r_s * (r - r_s) / (2.0 * r ** 3)) * v_zero ** 2 + (r_s / (2 * r * (r - r_s))) * v_one ** 2 + \
                  (r - r_s) * (v_two ** 2 + np.sin(theta) ** 2 * v_three ** 2)
    d_v_two = - (2.0 / r) * v_two * v_one + np.sin(theta) * np.cos(theta) * v_three ** 2
    d_v_three = -(2.0 / r) * v_one * v_three - 2 * (np.cos(theta) / np.sin(theta)) * v_two * v_three
    d_t = v_zero
    d_r = v_one
    d_theta = v_two
    d_phi = v_three
    return [d_t, d_r, d_theta, d_phi, d_v_zero, d_v_one, d_v_two, d_v_three]


def python_solver_with_termination(t, tend, V, r_s):
    sol = solve_ivp(fun3, (0, tend), V, method='LSODA', events=event, args=(r_s,), t_eval=t)
    ts.append(sol.t)
    ys.append(sol.y)
    if sol.status == 1:
        t = sol.t[-1]
        u = sol.y[:, -1].copy()
        return sol.y
    else:
        print('lost geodesic')
        return None

