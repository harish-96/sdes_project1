import unittest
import math
import numpy as np
from vdp_osc import VdpOscillator


class TestVanderPol(unittest.TestCase):

    def setUp(self):
        self.osc = VdpOscillator()

    def test_VdpOscillator_raises_exception_for_non_numeric_values(self):
        self.assertRaises(TypeError, VdpOscillator, "sb", "uir")

    def test_VdpOscillator_raises_exception_for_incorrect_initialisarion(self):
        self.assertRaises(TypeError, VdpOscillator, [0, 1, 1], 1.0)

    def test_update_state_leaves_state_unchanged_after_zero_time(self):
        np.testing.assert_array_almost_equal(self.osc.state,
                                             self.osc.update_step(0))

    def test_get_trajectory_leaves_state_unchanged_after_zero_time(self):
        self.assertListEqual(self.osc.state,
                             list(self.osc.get_trajectory(0, 3)[0]))

    def test_get_trajectory_returns_sine_for_zero_mu(self):
        temp = VdpOscillator(mu=0).get_trajectory(5, 5)
        np.testing.assert_array_almost_equal(
            [temp[i][0] for i in range(len(temp))],
            [math.sin(i) for i in np.linspace(0, 5, 6)])


if __name__ == '__main__':
    unittest.main()
