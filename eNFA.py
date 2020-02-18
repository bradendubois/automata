from Automaton import Automaton
from NFA import NonDeterministicFiniteAutomaton
from DeltaTransition import EpsilonNonDeterministic


class EpsilonNonDeterministicFiniteAutomaton(NonDeterministicFiniteAutomaton):
    """
    A basic Non-Deterministic Finite Automaton.
    """

    def __init__(self, q: set, sigma: set, delta_mapping: dict, q0: set, f: set):
        """
        Constructor for a Non-Deterministic Finite Automaton, M.
        :param q: The set of states in M.
        :param sigma: The alphabet of M.
        :param delta_mapping: The transition function: a mapping of (x in q, a in sigma) to q.
        :param q0: The initial state.
        :param f: The set of final/accepting states.
        """
        super().__init__(q, sigma, delta_mapping, q0, f)
        self.delta_function = EpsilonNonDeterministic(self.delta_mapping)

