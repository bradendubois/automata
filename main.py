import yaml
from DFA import DeterministicFiniteAutomaton as DFA
from NFA import NondeterministicFiniteAutomaton as NFA
from file_loader import load_yaml
from sys import argv
from os import listdir, path

DEFAULT_LANGUAGE_LOCATION = "languages"

# Determine if a file was specified
filename = None
if len(argv) > 1:
    filename = argv[1]
    print("Selecting:", filename)

# Otherwise, get the user to select one
if path.isdir(DEFAULT_LANGUAGE_LOCATION):
    files = sorted([f for f in listdir(DEFAULT_LANGUAGE_LOCATION) if f.endswith(".yml")])
    selection = ""
    while not selection.isdigit() or not 1 <= int(selection) <= len(files):
        for f in range(len(files)):
            print(str(f+1) + ")", files[f])
        selection = input("Selection: ")
    filename = DEFAULT_LANGUAGE_LOCATION + "/" + files[int(selection)-1]

# Load the yml file
loaded = load_yaml(filename)

# Ensure a valid automata type is specified
try:
    if loaded["automata"] not in ["DFA", "NFA", "eNFA"]:
        print("Invalid automata type specified.")
        exit(-1)

except KeyError:
    print("No automata type specified.")
    exit(-1)    

# Get the automaton type
automata = loaded["automata"]

# Load the corresponding automaton
if automata == "DFA":
    automaton_type = DFA
elif automata == "NFA":
    automaton_type = NFA
else:
    automaton_type = eNFA

automaton = automaton_type(**loaded["language"])


print(automaton.accepts("00001110101"))