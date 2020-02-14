import abc  # Abstract Base Class ! Makes something like an interface.


class DeltaTransition(abc.ABC):
    """
    Utilize the ABC to enforce an interface that requires a transition function.
    Exists as sigma in an automaton, M.
    """
    def __init__(self, delta_mapping: dict):
        self.delta_mapping = delta_mapping

    @abc.abstractmethod
    def delta_transition(self, q0: str or set, w: str):
        """
        A transition function for a finite automaton.
        :param q0: The state before reading the given word
        :param w: The word to read
        :return: A state in Q.
        """
        pass


class Deterministic(DeltaTransition):
    """
    The transition function for a deterministic finite automaton, M.
    """
    def __init__(self, delta_mapping: dict):
        super().__init__(delta_mapping)

    def delta_transition(self, q0: str, w):
        if w == "":
            return q0
        else:
            return self.delta_mapping[(self.delta_transition(q0, w[:-1]), w[-1])]


class NonDeterministic(DeltaTransition):
    """
    The transition function for a non-deterministic finite automaton, M.
    """
    def __init__(self, delta_mapping: dict):
        super().__init__(delta_mapping)

    def delta_transition(self, q0: set, w: str):
        if w == "":
            return q0
        else:
            return self.result(self.delta_transition(q0, w[:-1]), w[-1])

    def result(self, q0: set, a: str):
        result_set = set()
        for state in q0:
            result_set.add(self.delta_mapping[(state, a)])
        return result_set


class EpsilonNonDeterministic(NonDeterministic):
    """
    The transition function for an epsilon-transition-supporting NFA, M.
    """
    def __init__(self, delta_mapping: dict):
        super().__init__(delta_mapping)

    def delta_transition(self, q0: set, w: str):
        if w == "":
            return self.epsilon_close(q0)
        else:
            return self.epsilon_close(self.result(self.delta_transition(q0, w[:-1]), w[-1]))

    def epsilon_close(self, q0: set):
        """
        Get the epsilon closure of a given state.
        :param q0: The state to epsilon-close
        :return:
        """
        epsilon_closure = self.result(q0, "epsilon")
        epsilon_closure.add(q0)
        if len(epsilon_closure) > len(q0):
            epsilon_closure = self.epsilon_close(epsilon_closure)
        return epsilon_closure
