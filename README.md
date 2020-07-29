# automata

A small CLI automata project, supporting DFAs, NFAs, and eNFAs.

```
     ____ ___  __/ /_____  ____ ___  ____ _/ /_____ _  
    / __ `/ / / / __/ __ \/ __ `__ \/ __ `/ __/ __ `/  
   / /_/ / /_/ / /_/ /_/ / / / / / / /_/ / /_/ /_/ /   
   \__,_/\__,_/\__/\____/_/ /_/ /_/\__,_/\__/\__,_/     
```

## Requirements

The project is built in **Python 3**, and uses the following libraries:

- ``sys``
- ``os``
- ``yaml``

Install Python 3 [here](https://python.org).

## Installation

Clone the project from the Github repository:

```shell_script
https://github.com/bradendubois/automata/
cd automata
```

Then, just run the ``main.py`` file in Python:

```shell_script
python main.py
```

or:

```shell_script
./main.py
```

## Usage

There is a default directory of languages supplied, ``languages``, that can be added to. This directory is read on launch, and the user will be queried to select a file in it.

Alternatively, if a file is specified (in the ``languages`` directory or otherwise), the above step will be bypassed and the specified file will selected.

```shell_script
python main.py languages/l1.yml
```

Then, the main loop begins, which requests a word given as input, and it will query whether the automaton specified accepts the word, and if so, what state(s) the automaton may be in.

## Language Files

A few basic automaton definitions are included in ``languages``; any can be added to this directory as long as they are properly formatted.


The following language, ``languages/l1.yml``, will be given as an example.

```yml
automata: DFA

M:

    Q: 
        - q0
        - q1
        - q2

    Sigma: 
        - a
        - b
        - c
        - d

    Delta:
        - "q0, a": q1
        - "q0, d": q0
        - "q1, b": q2
        - "q2, c": q0

    q0: q0

    F: 
        - q0
```

- ``automata``: Must be one of [``DFA``, ``NFA``, ``eNFA``], to specify what type of automaton will interpret it.
- ``M``: The actual automaton definition, *M*. 
  - ``Q``: A set (a sequence in **YAML**) of states.
  - ``Sigma``: The input alphabet.
  - ``Delta``: A set of "state, symbol" to state pairs.
  - ``q0``: The start state; in Q.
  - ``F``: A set of final states; a subset of Q. 

The above language is for a DFA; the definitions for an NFA and eNFA is slightly different. 

The following example is ``languages/l4.yml``, an eNFA:

```yml
automata: eNFA

M:
    
    Q: 
        - q0
        - q1
        - q2
        - q3
        - q4
    
    Sigma: 
        - 1
        - 0

    Delta:
        - "q0, 0":
            - q0
            - q1
        
        - "q1, epsilon":
            - q2
        
        - "q2, epsilon":
            - q3

        - "q3, 1":
            - q4

    q0: q0
    
    F:
        - q4
```

- ``Delta`` now has a set of "state, symbol"s that map to a set of possible states.
- ``epsilon`` is a reserved symbol which enables the representation of an epsilon transition.

**Note**: Symbols in ``Sigma`` can be multiple characters in length: to enter a word with multi-length symbols, use commas for separation.

For example:
- ``0101``: 0, 1, 0, 1.
- ``a,b,cd``: a, b, cd
- ``a, aa, aaaa``: a, aa, aaaa

## Acknowledgements

- I got the neat ASCII art spelling "automata" from [patorjk.com](http://patorjk.com/software/taag/#p=display&f=Slant&t=automata).
- Automata theory is a great subject for anyone in computer science if they are so mathematically-inclined. I highly recommend anyone take one if capable, and loved Automata and Formal Languages at the University of Saskatchewan.
