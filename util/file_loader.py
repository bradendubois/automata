from yaml import load, FullLoader
from os import path
from collections import ChainMap

def load_and_parse(filename: str):
    
    # Ensure the file exists
    assert path.isfile(filename), "File not found."

    # Load the actual contents of the YML file
    with open(filename) as f:
        preprocessed = load(f, Loader=FullLoader)
    
    
    # Parse each part of the language defined in the YML file into a dictionary
    m = preprocessed["M"]

    # Only really do work parsing the delta transition function
    parsed_delta = dict()
    delta_pre = dict(ChainMap(*m["Delta"]))  # Merge the sequence of dictionaries
    for key in delta_pre:
        # Add the specific value, turning the key into a tuple, value into a set
        parsed_delta[tuple(i.strip() for i in key.split(","))] = set(delta_pre[key]) if isinstance(delta_pre[key], list) else delta_pre[key]

    return {
        "M": {
            "q": set(str(i) for i in m["Q"]),
            "sigma": set(str(i) for i in m["Sigma"]),
            "delta": parsed_delta,
            "q0": m["q0"],
            "f": set(str(i) for i in m["F"])
        },

        "automata": preprocessed["automata"]
    }
