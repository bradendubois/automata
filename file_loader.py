from yaml import load, FullLoader
from os import path
from collections import ChainMap

def load_yaml(filename: str):
    
    assert path.isfile(filename), "File not found."

    with open(filename) as f:
        preprocessed = load(f, Loader=FullLoader)
    
    
    l_pre = preprocessed["language"]
    
    l = dict()

    l["language"] = dict()
    l["language"]["q"] = set(l_pre["Q"])
    l["language"]["sigma"] = set(l_pre["Sigma"])
    
    delta = dict()
    delta_pre = dict(ChainMap(*l_pre["Delta"]))
    for key in delta_pre:
        delta[tuple(i.strip() for i in key.split(","))] = delta_pre[key]

    l["language"]["delta"] = delta
    l["language"]["q0"] = l_pre["q0"]
    l["language"]["f"] = set(l_pre["F"])

    l["automata"] = preprocessed["automata"]

    return l