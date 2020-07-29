#!/usr/bin/env python

##########################################################
#                                                        #
#     ____ ___  __/ /_____  ____ ___  ____ _/ /_____ _   #
#    / __ `/ / / / __/ __ \/ __ `__ \/ __ `/ __/ __ `/   #
#   / /_/ / /_/ / /_/ /_/ / / / / / / /_/ / /_/ /_/ /    #
#   \__,_/\__,_/\__/\____/_/ /_/ /_/\__,_/\__/\__,_/     #
#                                                        #
##########################################################

# Python libraries
from sys import argv
from os import listdir, path

# Different automata
from automata.DFA import DeterministicFiniteAutomaton as DFA
from automata.NFA import NondeterministicFiniteAutomaton as NFA
from automata.eNFA import EpsilonNondeterministicFiniteAutomaton as eNFA

# Parse the YML file into a proper automaton
from util.file_loader import load_and_parse

DEFAULT_LANGUAGE_LOCATION = "languages"

# Determine if a file was specified
filename = None
if len(argv) > 1:
    filename = argv[1]
    print("Selecting:", filename)

# Otherwise, get the user to select one
elif path.isdir(DEFAULT_LANGUAGE_LOCATION):
    files = sorted([f for f in listdir(DEFAULT_LANGUAGE_LOCATION) if f.endswith(".yml")])
    selection = ""
    while not selection.isdigit() or not 1 <= int(selection) <= len(files):
        print("Languages found:")
        for f in range(len(files)):
            print(str(f+1) + ")", files[f])
        selection = input("Selection: ")
    
    filename = DEFAULT_LANGUAGE_LOCATION + "/" + files[int(selection)-1]
    print("Selected:", filename, "\n")

# No file specified, no default directory to check
else:
    print("No file provided, nor is the default directory of languages found.")
    exit(-1)

# Load the yml file
loaded_file = load_and_parse(filename)

# Ensure a valid automata type is specified
try:
    if loaded_file["automata"] not in ["DFA", "NFA", "eNFA"]:
        print("Invalid automata type specified.")
        exit(-1)

except KeyError:
    print("No automata type specified.")
    exit(-1)    

# Get the automaton type
automata = loaded_file["automata"]

# Load the corresponding automaton
if automata == "DFA":
    automaton_type = DFA
elif automata == "NFA":
    automaton_type = NFA
else:
    automaton_type = eNFA

automaton = automaton_type(**loaded_file["M"])
print(str(automaton))

# Words already specified
if len(argv) > 2:
    for word in argv[2:]:
        print(word + " accepted:", automaton.accepts(word), "\n")

# Begin a loop to read in words
else:
    
    while True:

        word = input("Enter a word: ")
        if "," in word:
            word = [i.strip() for i in word.split(",")]
        print("Word accepted:", automaton.accepts(word))

        # Aesthetic spacing, ask to continue/exit
        print()
        if input("Exit? (Y/N): ").lower().strip() in ["y", "yes"]:
            break
        print()
