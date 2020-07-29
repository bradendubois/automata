from automata.NFA import NondeterministicFiniteAutomaton as NFA

class EpsilonNondeterministicFiniteAutomaton(NFA):

    def __init__(self, q: set, sigma: set, delta: dict, q0: str, f: set):
        super().__init__(q, sigma, delta, q0, f)
        
    def _delta(self, q: set, w: str or list) -> set:
        
        if len(w) == 0:
            return self._epsilon(q)
        else:
            return set().union(*[self._epsilon(self.delta[(s, w[-1])]) for s in self._delta(q, w[:-1]) if (s, w[-1]) in self.delta])

    def _epsilon(self, q: set):

        return q | set().union(*[self._epsilon(self.delta[(s, "epsilon")]) for s in q if (s, "epsilon") in self.delta])
