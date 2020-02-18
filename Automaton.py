import abc
import Exceptions


class Automaton(abc.ABC):

    def __init__(self, q: set, sigma: set, delta_mapping: dict, q0: str or set, f: set):
        """
        The basic definition of a finite automaton, M
        :param q: A set of states in M
        :param sigma: The alphabet of M
        :param delta_mapping: The transition function of M
        :param q0: The initial state of M: must be in Q
        :param f: The final states of M: must be a subset of Q
        """

        # Enforce F as a subset of Q
        for s in f:
            if s not in q:
                raise Exceptions.InvalidSubset()

        # Enforce the initial state to be in Q
        #if q0 not in q:
        #    raise Exceptions.InvalidSubset()

        self.q = q
        self.sigma = sigma
        self.delta_mapping = delta_mapping
        self.q0 = q0
        self.f = f

    @abc.abstractmethod
    def accepts(self, w: str):
        """
        Determine if a word w is accepted in a given automaton
        :param w: The word read to read
        :return: True if the word is accepted, False otherwise
        """
        pass

    @abc.abstractmethod
    def delta(self, w: str):
        """
        Get the result state, or set of states, after reading a word in M.
        :param w: The word to read
        :return: A state, or set of states, if w is accepted; empty string or empty set otherwise.
        """
        pass
