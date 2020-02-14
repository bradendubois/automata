class InvalidSubset(Exception):
    """
    Raised when a set is incorrectly asserted to be the subset of another.
    Example: When F is not a subset of Q.
    """
    def __init__(self):
        pass
