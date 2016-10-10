import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

class vdp_oscillator:
	def __init__(self, init_y=0.0, init_ydot=1.0, tmax = 20.0, t0 = 0.0, nTime = 40,mu = 0.0):
		self.state = [init_y, init_ydot]
		self.t = t0
		self.mu = mu
		self.tmax = tmax
		self.nTime = nTime


