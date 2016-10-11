import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

def vdp_diff(state,t,mu):
		dydt = state[1]
		dy2dt = mu*(1-state[0]**2)*state[1] - state[0]
		return [dydt,dy2dt]

def update_state(y0 = [0,1], dt = 0.1, func = vdp_diff, mu = 1):
	global state 
	state = integrate.odeint(lambda state,t: func(state,t,mu), y0, [0,dt])[1]
	#print(state)

def solve_ode(func = vdp_diff, mu = 1, y0 = [0,1], t = np.linspace(0,10,100)):
	sol = integrate.odeint(lambda state,t: func(state,t,mu), y0, t)
	print(sol)
	plt.plot(t,sol)
	plt.show()
	plt.plot(sol[:,0],sol[:,1])
	plt.show()

#state = np.hstack((1,2))
state = [0, 1]
y = []
for i in range(100):
	update_state(state)
	print(state)
	y.append(state)
plt.plot(y)
plt.show()
print(state)
solve_ode()