from automata.DFA import DeterministicFiniteAutomaton as DFA

class NondeterministicFiniteAutomaton(DFA):

    def __init__(self, q: set, sigma: set, delta: dict, q0: str, f: set):
        super().__init__(q, sigma, delta, q0, f)
        
    def _delta(self, q: set, w: str or list) -> set:
        
        if len(w) == 0:
            return q
        else:
            return set().union(*[self.delta[(s, w[-1])] for s in self._delta(q, w[:-1]) if (s, w[-1]) in self.delta])

    def accepts(self, w: str or list):
        try:
            result = self._delta({self.q0}, w)
        except KeyError:
            result = set()
        print("delta({}, {}): {}".format(self.q0, w if w else '""', result))
        return result & self.f != set()
