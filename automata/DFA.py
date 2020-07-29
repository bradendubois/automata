

class DeterministicFiniteAutomaton:

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

    def __str__(self) -> str:
        msg = "M\n"
        msg += "Q: {}\n".format(", ".join(sorted(list(self.q))))
        msg += "Sigma: " + ", ".join(sorted(list(self.sigma))) + "\n"
        msg += "Delta:\n"
        for t in self.delta:
            msg += "  delta({}, {}) = {}\n".format(*t, self.delta[t]) 
        msg += "q0: {}\n".format(self.q0)
        msg += "F: {}\n".format(", ".join(sorted(list(self.f))))

        return msg

    def _delta(self, q: str, w: str) -> set:

        if w == "":
            return q
        else:
            return self.delta[(self._delta(q, w[:-1]), w[-1])]
    
    def accepts(self, w: str):
        try:
            result = self._delta(self.q0, w)
        except KeyError:
            result = set()
        print("delta({}, {}): {}".format(self.q0, w if w else '""', result))
        return result in self.f
