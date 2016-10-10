import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

mu = 1.0
def vdp_diff(state,t):
		dydt = state[1]
		dy2dt = mu*(1-state[0]**2)*state[1] - state[0]
		return [dydt, dy2dt]
y0 = [1,2]
t = np.linspace(0, 40, 500)
sol = integrate.odeint(vdp_diff, y0, t)
plt.plot(t,sol)
plt.show()
plt.plot(sol[:,0],sol[:,1])
plt.show()