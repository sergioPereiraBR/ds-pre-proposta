
class Once:
    """Simple object that evaluates to True once, and then always False."""

    def __init__(self) -> None:
        self.done = False

    def __bool__(self) -> bool:
        if self.done:
            return False
        else:
            self.done = True
            return True