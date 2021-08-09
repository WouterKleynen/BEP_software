import numpy as np
from scipy.integrate import solve_ivp
import conversion_formulas
import time


# Stop at Z > 10
def event_reach_Z_10(t, u, r_s, Z_end):
    event_reach_Z_10.terminal = True
    X, Y, Z = conversion_formulas.spherical_to_cartesian(u[1], u[2], u[3])
    return Z - Z_end


def event_fall_within_r_s(t, u, r_s, Z_end):
    event_fall_within_r_s.terminal = True
    if u[1] < r_s:
        print('Yeet')
    return r_s - u[1]


def fun3(t, variables, r_s, Z_end):
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


def python_solver_with_termination(t, tend, V, r_s, Z_end):
    sol = solve_ivp(fun3, (0.0, 2*tend), V, method='RK45', events=(event_fall_within_r_s, event_reach_Z_10), args=(r_s, Z_end), t_eval=t)
    if sol.status == 1:
        if len(sol.t_events[0]) > 0:
            return sol.y
        if len(sol.t_events[1]) > 0:
            return sol.y
    if sol.status == 0:
        return None
        # print('Z = 10 was NOT reached, but the proces was finised')
        # return sol.y # -> Toggle this on to see all geodesics including lost ones




