from vdp_osc import VdpOscillator
import numpy as np
import matplotlib.animation as animation
import csv
import matplotlib.pyplot as plt
import os


with open(os.path.join(".", "input.csv"), 'r') as f:
    inputfile = csv.reader(f, delimiter=",")
    next(inputfile)
    input_data = next(inputfile)
    state = [0, 0]
    mu, state[0], state[1], tmax, nTime = [float(str.strip(i))
                                           for i in input_data]

nTime = int(nTime)
osc = VdpOscillator(state, mu)
y = osc.get_trajectory(tmax, nTime)

fig1 = plt.figure(0)
ax1 = plt.axes(xlim=(-4, 4), ylim=(-2, 2))
line = ax1.plot([], [])[0]


def animate(i):
    """ Function that is called at each iteration of the animation.
    Sets the current position of the line
    """
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

# lines = [ax1.plot([], [])[0] for _ in range(2)]
# osc1 = VdpOscillator()

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
