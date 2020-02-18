from Automaton import Automaton
from DeltaTransition import NonDeterministic


class NonDeterministicFiniteAutomaton(Automaton):
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
        self.delta_function = NonDeterministic(self.delta_mapping)

    def accepts(self, w: str):
        """
        Determine if a word w is accepted in a given automaton
        :param w: The word read to read
        :return: True if the word is accepted, False otherwise
        """
        try:
            return len(self.delta(w) & self.f) > 0
        except KeyError:
            return False

    def delta(self, w: str):
        """
        Determine the state reached in M by the given word.
        :param w: A word over "sigma".
        :return: A set of states in Q.
        """
        return self.delta_function.delta_transition(self.q0, w)
