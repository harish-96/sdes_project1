import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


class VdpOscillator:
    """Template class for a Van der Pol oscillator.

    initialise with initial position, initial velocity, time for which it runs,
    Number of time steps, and the parameter mu of the differential equation
    """

    def __init__(self, y=0.0, ydot=1.0, mu=1.0):
        """Initialize the class with y, ydot and mu.
        These are optional arguments"""
        self.state = [y, ydot]
        self.mu = mu

    def vdp_diff(self, state, t):
        """compute the derivative of the given state"""
        dydt = state[1]
        dy2dt = self.mu * (1 - state[0]**2) * state[1] - state[0]
        return [dydt, dy2dt]

    def update_step(self, dt):
        """Compute the state of the system after one time step and update it"""
        self.state = integrate.odeint(self.vdp_diff, self.state, [0, dt])[1]

    def get_trajectory(self, tmax=20.0, nTime=500, **kwargs):
        """Returns an array containing the position and its derivative

        Takes as input the time for which trajectory is calculated,
        Number of time steps and an optional keyword argument for state
        which defaults to the instance state"""
        if "state" in kwargs:
            self.state = kwargs["state"]
        y = [self.state]
        for i in range(nTime):
            self.update_step(tmax / nTime)
            y.append(self.state)
        return y


osc = VdpOscillator()
osc1 = VdpOscillator()
tmax = 20
nTime = 500
y = osc.get_trajectory(tmax, nTime)

fig1 = plt.figure(0)
ax1 = plt.axes(xlim=(-4, 4), ylim=(-2, 2))
line = ax1.plot([], [])[0]

# lines = [ax1.plot([], [])[0] for _ in range(2)]

# def animate(i):
#     lines[0].set_data([0, y[i][0]], [0, 0])
#     global osc1, dt
#     osc1.update_step(tmax / nTime)
#     lines[1].set_data([0, osc1.state[0]], [1, 1])
#     return lines

# def init():
#     """initialize animation"""
#     lines[0].set_data([], [])
#     lines[1].set_data([], [])
#     return lines

# anim = animation.FuncAnimation(fig1, animate, init_func=init,
#                                frames=nTime, blit=True,
#                                interval=100 * tmax / nTime)


def animate(i):
    line.set_data([0, y[i][0]], [0, 0])
    return line,


def init():
    """initialize animation"""
    line.set_data([], [])
    return line,


anim = animation.FuncAnimation(fig1, animate, init_func=init,
                               frames=nTime, blit=True,
                               interval=100 * tmax / nTime)

plt.figure(1)
plt.plot(np.linspace(0, tmax, nTime + 1), y)

plt.figure(2)
plt.plot([y[i][0] for i in range(len(y))],
         [y[i][1] for i in range(len(y))])

plt.show()
