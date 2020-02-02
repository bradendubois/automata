class NoTransition(Exception):
    def __init__(self):
        pass


class InvalidState(Exception):
    def __init__(self):
        pass


class DFA(object):
    """
    A basic Deterministic Finite Automaton.
    """

    def __init__(self, q: set, sigma: set, delta: dict, q0: str, f: set):
        """
        Constructor for a Deterministic Finite Automaton, M.
        :param q: The set of states in M.
        :param sigma: The alphabet of M.
        :param delta: The transition function: a mapping of (x in q, a in sigma) to q.
        :param q0: The initial state.
        :param f: The set of final/accepting states.
        """
        self.q = q
        self.alphabet = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f

    def accepts(self, word: str):
        """
        Determine if a word is accepted by the DFA.
        :param word: A word over the language "sigma"
        :return: True if the word is accepted, False otherwise
        """
        # Ensure the word is over the alphabet of M
        for symbol in word:
            if symbol not in self.alphabet:
                return False

        try:
            return self.result(word) in self.f
        except NoTransition:
            return False

    def result(self, word: str):
        """
        Determine the state reached in M by the given word.
        :param word: A word over "sigma".
        :return: A state in Q if it exists, otherwise "Undefined State".
        """
        # Ensure the word is over the alphabet of M
        for symbol in word:
            if symbol not in self.alphabet:
                return "Word is not over Sigma."

        try:
            return self.transition(self.q0, word)
        except NoTransition:
            return "Undefined State"

    def transition(self, state: str, action: str):
        if state not in self.q:
            raise InvalidState
        elif action == "":
            return state
        else:
            result_state = self.transition(state, action[:-1])
            if (result_state, action[-1]) not in self.delta:
                raise NoTransition
            return self.delta[(result_state, action[-1])]


# Tests

q_test = {"q0", "q1", "q2"}
sigma_test = {"a", "b", "c", "d"}
delta_test = {
    ("q0", "a") : "q1",
    ("q0", "d") : "q0",
    ("q1", "b") : "q2",
    ("q2", "c") : "q0"
}

f_test = { "q0" }

M = DFA(q_test, sigma_test, delta_test, "q0", f_test)

print(M.accepts("ddabcdabcdd"))
