import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


class VdpOscillator:
    """Template class for a Van der Pol oscillator.

    initialise with initial position, initial velocity, time for which it runs,
    Number of time steps, and the parameter mu of the differential equation
    """

    def __init__(self, y=0.0, ydot=1.0, tmax=20.0, nTime=500, mu=1.0):
        self.state = [y, ydot]
        self.mu = mu
        self.tmax = tmax
        self.nTime = nTime

    def vdp_diff(self, state, t):
        """compute the derivative of the given state"""
        dydt = state[1]
        dy2dt = self.mu * (1 - state[0]**2) * state[1] - state[0]
        return [dydt, dy2dt]

    def update_step(self, dt):
        """Compute the state of the system after one time step and update the state
        """
        self.state = integrate.odeint(self.vdp_diff, self.state, [0, dt])[1]


osc = VdpOscillator(1, 2, 40)
dt = osc.tmax / osc.nTime
y = [osc.state]

for i in range(osc.nTime):
    osc.update_step(dt)
    y.append(osc.state)
plt.figure(0)
plt.plot(np.linspace(0, osc.tmax, osc.nTime + 1), y)

plt.figure(1)
plt.plot([y[i][0] for i in range(osc.nTime + 1)], [y[i][1] for i in range(osc.nTime + 1)])

fig1 = plt.figure(2)
ax1 = plt.axes(xlim=(-4, 4), ylim=(-2, 2))
lines = [ax1.plot([], [])[0] for _ in range(2)]

osc1 = VdpOscillator()


def animate(i):
    lines[0].set_data([0, y[i][0]], [0, 0])
    global osc1, dt
    osc1.update_step(dt)
    lines[1].set_data([0, osc1.state[0]], [1, 1])
    return lines


def init():
    """initialize animation"""
    lines[0].set_data([], [])
    lines[1].set_data([], [])
    return lines


anim = animation.FuncAnimation(fig1, animate, init_func=init,
                               frames=osc.nTime, interval=1000 * dt, blit=True)
plt.show()
