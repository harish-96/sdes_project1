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
x = osc.get_trajectory(tmax, nTime)

fig1 = plt.figure(0)
ax1 = plt.axes(xlim=(-4, 4), ylim=(-2, 2))
ax1.set_title('An animation of the Van der Pol oscillator')
ax1.set_xlabel('Spatial x-axis')
ax1.set_ylabel('Spatial y-axis')
line = ax1.plot([], [])[0]


def animate(i):
    """ Function that is called at each iteration of the animation.
    Sets the current position of the line
    """
    line.set_data([0, x[i][0]], [0, 0])
    return line,


def init():
    """initialize animation"""
    line.set_data([], [])
    return line,


anim = animation.FuncAnimation(fig1, animate, init_func=init,
                               frames=nTime, blit=True,
                               interval=100 * tmax / nTime)

if not os.path.exists('../output'):
    os.mkdir('../output')

anim.save('../output/vanderpol_animation.mp4', fps=30,
          extra_args=['-vcodec', 'libx264'])

pos, vel = zip(*x)
plt.figure(1)
plt.plot(np.linspace(0, tmax, nTime + 1), pos, label='Position')
plt.plot(np.linspace(0, tmax, nTime + 1), vel, label='Velocity')
plt.title('The position and velocity of the Van der Pol oscillator'
          'for the\n initial conditions $\mu$ = '
          '%.2f, $x = %.2f$ and $\dot{x} = %.2f$' % (mu, state[0], state[1]))

plt.xlabel('Time')
plt.ylabel('$x$, $\dot{x}$', fontsize=18)
plt.legend()
plt.xlim([0, tmax])
plt.ylim([-3, 3])
plt.savefig("../output/trajectory.png")

plt.figure(2)
plt.plot(pos, vel)
plt.title('The phase portrait of the Van der Pol oscillator'
          'for the\n initial conditions $\mu$ = '
          '%.2f, $x = %.2f$ and $\dot{x} = %.2f$' % (mu, state[0], state[1]))

plt.xlabel('Time')
plt.ylabel('$x$, $\dot{x}$', fontsize=18)
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.savefig("../output/phase_portrait.png")
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
