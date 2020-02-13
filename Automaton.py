import abc


class Automaton(abc.ABC):

    def __init__(self, q: set, sigma: set, delta: dict, q0: str or dict, f: set):
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f

        # Add exceptions

    @abc.abstractmethod
    def accepts(self, w: str):
        pass

    @abc.abstractmethod
    def delta_transition(self, w: str):
        pass


