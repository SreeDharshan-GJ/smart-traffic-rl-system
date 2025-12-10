#!/usr/bin/env python
"""Unit tests for traffic simulator"""

import unittest
from backend.app.services.traffic_simulator import (
    TrafficSimulator, QLearningAgent, TrafficState
)


class TestTrafficState(unittest.TestCase):
    """Test TrafficState class"""

    def setUp(self):
        self.state = TrafficState(10, 5, 8, 12)

    def test_total_queue(self):
        self.assertEqual(self.state.get_total_queue(), 35)

    def test_average_queue(self):
        self.assertEqual(self.state.get_average_queue(), 8.75)

    def test_longest_queue_direction(self):
        self.assertEqual(self.state.get_longest_queue_direction(), 3)  # West

    def test_queue_imbalance(self):
        self.assertEqual(self.state.get_queue_imbalance(), 7)  # 12 - 5


class TestQLearningAgent(unittest.TestCase):
    """Test Q-Learning agent"""

    def setUp(self):
        self.agent = QLearningAgent()

    def test_initialization(self):
        self.assertEqual(self.agent.num_states, 256)
        self.assertEqual(self.agent.num_actions, 4)
        self.assertEqual(self.agent.epsilon, 0.1)

    def test_state_to_index(self):
        """Test state discretization"""
        state = TrafficState(0, 0, 0, 0)
        index = self.agent.state_to_index(state)
        self.assertEqual(index, 0)

        state = TrafficState(30, 30, 30, 30)
        index = self.agent.state_to_index(state)
        self.assertEqual(index, 255)  # Max index

    def test_select_action(self):
        state = TrafficState(10, 10, 10, 10)
        action = self.agent.select_action(state)
        self.assertIn(action, [0, 1, 2, 3])

    def test_epsilon_decay(self):
        initial_epsilon = self.agent.epsilon
        self.agent.decay_epsilon()
        self.assertLess(self.agent.epsilon, initial_epsilon)
        self.assertGreaterEqual(self.agent.epsilon, self.agent.epsilon_min)

    def test_q_values_flat(self):
        q_values = self.agent.get_q_values_flat()
        self.assertEqual(len(q_values), 256 * 4)


class TestTrafficSimulator(unittest.TestCase):
    """Test traffic simulator"""

    def setUp(self):
        self.simulator = TrafficSimulator()

    def test_initialization(self):
        self.assertIsNotNone(self.simulator.agent)

    def test_traffic_state_initialization(self):
        state = self.simulator.initialize_traffic_state()
        self.assertIsInstance(state, TrafficState)
        self.assertTrue(3 <= state.north_queue <= 18)
        self.assertTrue(3 <= state.south_queue <= 18)

    def test_next_state_simulation(self):
        state = TrafficState(10, 10, 10, 10)
        next_state = self.simulator.simulate_next_state(state, 0)
        self.assertIsInstance(next_state, TrafficState)

    def test_reward_calculation(self):
        state1 = TrafficState(20, 20, 20, 20)
        state2 = TrafficState(10, 10, 10, 10)
        reward = self.simulator.calculate_reward(state1, state2, 0)
        self.assertIsInstance(reward, float)

    def test_rl_simulation(self):
        """Test RL simulation runs successfully"""
        results = self.simulator.simulate_traffic_rl(2)
        
        self.assertEqual(results['episodes'], 2)
        self.assertIn('avgWaitTime', results)
        self.assertIn('avgThroughput', results)
        self.assertIn('totalReward', results)
        self.assertIn('qValues', results)
        self.assertIn('states', results)
        self.assertGreater(len(results['states']), 0)

    def test_fixed_simulation(self):
        """Test fixed control simulation runs successfully"""
        results = self.simulator.simulate_traffic_fixed(2)
        
        self.assertEqual(results['episodes'], 2)
        self.assertIn('avgWaitTime', results)
        self.assertIn('avgThroughput', results)
        self.assertIsNone(results['totalReward'])
        self.assertIsNone(results['qValues'])

    def test_simulate_method(self):
        """Test simulate method dispatcher"""
        results_rl = self.simulator.simulate('RL', 2)
        results_fixed = self.simulator.simulate('Fixed', 2)
        
        self.assertIsNotNone(results_rl['totalReward'])
        self.assertIsNone(results_fixed['totalReward'])

        with self.assertRaises(ValueError):
            self.simulator.simulate('Unknown', 2)


if __name__ == '__main__':
    unittest.main()
