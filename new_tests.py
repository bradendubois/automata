from DFA import DeterministicFiniteAutomaton

from time import sleep

# Tests

# Test 1 - Basic circular automaton

language_1 = [
    {"q0", "q1", "q2"},          # Q
    {"a", "b", "c", "d"},        # Sigma
    {
        ("q0", "a"): ("q1"),     # Delta
        ("q0", "d"): ("q0"),
        ("q1", "b"): ("q2"),
        ("q2", "c"): ("q0")
    },
    "q0",
    {"q0"}
]

# Test 2 - Automata from CMPT 364

language_2 = [
    {"q0", "q1", "q2", "q3", "q4", "q5"},
    {"a", "b"},
    {
        ("q0", "a"): "q1",
        ("q0", "b"): "q3",
        ("q1", "b"): "q2",
        ("q2", "a"): "q5",
        ("q3", "a"): "q5",
        ("q3", "b"): "q4",
        ("q4", "a"): "q3",
    },
    "q0",
    {"q5"}
]

# All strings over {0, 1} ending in 101
language_3 = [
    {"q0", "q1", "q2", "q3"},
    {"1", "0"},
    {
        ("q0", "0"): {"q0"},
        ("q0", "1"): {"q0", "q1"},
        ("q1", "0"): {"q2"},
        ("q2", "1"): {"q3"}
    },
    "q0",
    {"q3"}
]

# "aa"+ - epsilon-only test
language_4 = [
    {"q0", "q1", "q2", "q3"},
    {"a"},
    {
        ("q0", "a"): {"q0", "q1"},
        ("q1", "a"): {"q1"},
        ("q1", "epsilon"): {"q2"},
        ("q2", "a"): {"q2", "q3"},
        ("q3", "a"): {"q3"}
    },
    {"q3"}
]

# DFA_M = DeterministicFiniteAutomaton(language_1[0], language_1[1], language_1[2], "q0", language_1[3])
# NFA_M = NonDeterministicFiniteAutomaton(language_1[0], language_1[1], language_1[2], {"q0"}, language_1[3])
# eNFA_M = EpsilonNonDeterministicFiniteAutomaton(language_1[0], language_1[1], language_1[2], {"q0"}, language_1[3])

word = "dabcdabcabcdddd"


q, sigma, delta, q0, f = language_1
dfa = DeterministicFiniteAutomaton(q, sigma, delta, q0, f)

print(dfa.accepts(word))
"""
for i in range(100):
    result = DFA_M.accepts(word)
    print("T", end="") if result else print("F", end="")
"""

# print(DFA_M.accepts(word))
# print(NFA_M.accepts(word))
# print(eNFA_M.accepts(word))
