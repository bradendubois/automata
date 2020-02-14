from Automaton import Automaton
import Exceptions
import DeltaTransition
from typing import Type
from DeltaTransition import Deterministic


class DeterministicFiniteAutomaton(Automaton):
    """
    A basic Deterministic Finite Automaton.
    """

    def __init__(self, q: set, sigma: set, delta_mapping: dict, q0: str, f: set):
        """
        Constructor for a Deterministic Finite Automaton, M.
        :param q: The set of states in M.
        :param sigma: The alphabet of M.
        :param delta_mapping: The transition function: a mapping of (x in q, a in sigma) to q.
        :param q0: The initial state.
        :param f: The set of final/accepting states.
        """
        super().__init__(q, sigma, delta_mapping, q0, f)
        self.delta_function = Deterministic(self.delta_mapping)

    def delta(self, w: str):
        """
        Determine the state reached in M by the given word.
        :param w: A word over "sigma".
        :return: A state in Q if it exists, otherwise "Undefined State".
        """
        return self.delta_function.delta_transition(self.q0, w)
