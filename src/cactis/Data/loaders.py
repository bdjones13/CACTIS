import numpy as np
import importlib.resources as ir

# def load_lorenz63():
#     # point to the package where the file lives
#     with ir.files("cactis.Data.Lorenz63").joinpath("lorenz_10k_raw.npy").open("rb") as f:
#         l63 = np.load(f).T[:, 10000:100000]
#     return l63

# def load_lorenz96():
#     with ir.files("cactis.Data.Lorenz96").joinpath("lorenz96_raw.txt").open("r") as f:
#         return np.loadtxt(f)

# def load_cdv():
#     with ir.files("cactis.Data.CDV").joinpath("cdv_deterministic.npy").open("r") as f:
#         return np.fromfile(f).reshape(6,-1)#[:3,10000:90000] #6x2000000, use first three dimensions and cut down on length a lot


def load_jetlat():
    with ir.files("cactis.Data.JetLat").joinpath("JetLat.txt").open("r") as f:
        return  np.loadtxt(f, delimiter = ",").T #3x9809 this one is either already reduced by Kristian et al or just fine as is
    

def lorenz63(state, sigma=10.0, rho=28.0, beta=8/3):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

def rk4_step(f, state, dt, *args, **kwargs):
    k1 = f(state, *args, **kwargs)
    k2 = f(state + 0.5*dt*k1, *args, **kwargs)
    k3 = f(state + 0.5*dt*k2, *args, **kwargs)
    k4 = f(state + dt*k3, *args, **kwargs)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

def simulate_lorenz(initial_state, T=50.0, dt=0.01, sigma=10.0, rho=28.0, beta=8/3):
    n_steps = int(np.ceil(T / dt))
    ts = np.linspace(0, n_steps*dt, n_steps+1)
    traj = np.zeros((n_steps+1, 3))
    traj[0] = initial_state
    state = np.array(initial_state, dtype=float)
    for i in range(n_steps):
        state = rk4_step(lorenz63, state, dt, sigma, rho, beta)
        traj[i+1] = state
    return ts, traj

def load_lorenz63(initial=[1.3, 1.5, 17.0]):
    _, traj = simulate_lorenz(initial_state=initial)
    return traj.T