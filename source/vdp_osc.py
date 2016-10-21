import numpy as np
import scipy.integrate as integrate


class VdpOscillator:
    """Template class for a Van der Pol oscillator.

    Initialise with initial position, initial velocity, time for which it runs,
    Number of time steps, and the parameter mu of the differential equation
    """

    def __init__(self, state=[0, 1], mu=1.0):
        """Initialize the class with y, ydot and mu.
        These are optional arguments"""
        if type(mu) not in [type(2), type(2.0)]\
           or type(state[0]) not in [type(2), type(2.0)]\
           or type(state[1]) not in [type(2), type(2.0)]:
            raise TypeError("Expected a numeric type")
        if len(state) == 2:
            self.state = state
        else:
            raise TypeError("Expected list of",
                            "length 2 received %d" % (len(state)))
        self.mu = mu

    def vdp_diff(self, state, t):
        """compute the derivative of the given state"""
        dxdt = state[1]
        dx2dt = self.mu * (1 - state[0]**2) * state[1] - state[0]
        return [dxdt, dx2dt]

    def update_step(self, dt):
        """Compute the state of the system after one time step and update it"""
        self.state = integrate.odeint(self.vdp_diff, self.state, [0, dt])[1]
        return self.state

    def get_trajectory(self, tmax=20.0, nTime=500, **kwargs):
        """Returns an array containing the position and its derivative

        Takes as input the time for which trajectory is calculated,
        Number of time steps and an optional keyword argument for state
        which defaults to the instance state"""
        if "state" in kwargs:
            self.state = kwargs["state"]
        x = [np.asarray(self.state)]
        for i in range(nTime):
            self.update_step(tmax / nTime)
            x.append(self.state)
        return x
