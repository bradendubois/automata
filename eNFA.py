
class EpsilonNondeterministicFiniteAutomaton:

    def __init__(self, q: set, sigma: set, delta: dict, q0: str, f: set):
        
        # Store all properties of our Automaton
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f
        
        # Enforce definitions
        assert q0 in q, "q0 is not in Q!"
        assert f.issubset(q), "F is not a subset of Q!"
        
    def _delta(self, q: set, w: str) -> set:
        
        if w == "":
            return self._epsilon(q)
        else:
            return set().union(*[self._epsilon(self.delta[(s, w[-1])]) for s in self._delta(q, w[:-1]) if (s, w[-1]) in self.delta])

    def accepts(self, w: str):
        try:
            result = self._delta({self.q0}, w)
            print("delta({}, {}): {}".format(self.q0, w, result))
            return result & self.f != set()
        except KeyError:
            return False
    
    def _epsilon(self, q: set):

        return q | set().union(*[self._epsilon(self.delta[(s, "epsilon")]) for s in q if (s, "epsilon") in self.delta])
