import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

class vdp_oscillator:
	"""Template class for a Van der Pol oscillator. 

	initialise with initial position, initial velocity, time for which it runs, Number of time steps, and the 
	parameter mu of the differential equation
	""" 
	def __init__(self, init_y=0.0, init_ydot=1.0, tmax = 20.0, nTime = 40,mu = 0.0):
		self.state = [init_y, init_ydot]
		self.t = 0.0
		self.mu = mu
		self.tmax = tmax
		self.nTime = nTime
	def vdp_diff(self,state,t):
	"""compute the derivative of the given state"""
		dydt = state[0]
		dy2dt = self.mu*(1-state[0]**2)*state[1] - state[0]
		return [dydt, dy2dt]
	def update_step(self, dt):
	"""compute the state of the system after one time step - dt and update the state of the system"""
		self.state = integrate.odeint(self.vdp_diff, self.state, [0, dt])
		self.t += dt

