"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize with the starting number."""
        self.start = start
        self.current = start

    def generate(self):
        """Return the next serial number."""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Reset the serial number to the original start value."""
        self.current = self.start

    def __repr__(self):
        """Display a readable representation of the object."""
        return f"<SerialGenerator start={self.start} next={self.current}>"
    