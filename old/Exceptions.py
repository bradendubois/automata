class InvalidSubset(Exception):
    """
    Raised when a set is incorrectly asserted to be the subset of another.
    Example: When F is not a subset of Q.
    """
    def __init__(self):
        pass


class NonSigmaSymbol(Exception):
    """
    Raised when a symbol over a word w is not a symbol over sigma.
    Example: w = 101a, sigma = { 0, 1 }
    """
    def __init__(self, symbol: str, sigma: set):
        print("A word was issued containing symbol {}, which is not over {}.".format(symbol, sigma))
