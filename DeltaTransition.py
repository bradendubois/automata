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
            return_set = set()
            for state in self.delta_transition(self.result(q0, w[-1]), w[:-1]):
                if (state, w[-1]) in self.delta_mapping:
                    sub_states = self.delta_mapping[(state, w[-1])]
                    for i in sub_states:
                        return_set.add(i)
            return return_set

    def result(self, q0: set, a: str):
        return_set = set()
        for s in q0:
            if (s, a) in self.delta_mapping:
                result = self.delta_mapping[(s, a)]
                for state in result:
                    return_set.add(state)
        return return_set


class EpsilonNonDeterministic(NonDeterministic):
    """
    The transition function for an epsilon-transition-supporting NFA, M.
    """
    def __init__(self, delta_mapping: dict):
        super().__init__(delta_mapping)

    def delta_transition(self, q0: set, w: str):
        if w == "":
            return q0
        else:
            return_set = set()
            for state in self.epsilon_close(self.delta_transition(self.result(q0, w[-1]), w[:-1])):
                if (state, w[-1]) in self.delta_mapping:
                    sub_states = self.delta_mapping[(state, w[-1])]
                    for i in sub_states:
                        return_set.add(i)
            return return_set

    def epsilon_close(self, q0: set):
        """
        Get the epsilon closure of a given state.
        :param q0: The state to epsilon-close
        :return:
        """
        epsilon_closure = self.result(q0, "epsilon")
        for s in q0:
            epsilon_closure.add(s)
        if len(epsilon_closure) > len(q0):
            epsilon_closure = self.epsilon_close(epsilon_closure)
        return epsilon_closure
