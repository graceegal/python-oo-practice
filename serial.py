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
        """Create a serial generator, starting at start"""
        self.start = start
        self.count = start

    def __repr__(self):
        return f"SerialGenerator start={self.start}, current={self.count}"

    def generate(self):
        """Increment serial by 1. Returns serial number"""
        self.count += 1
        return self.count - 1

    def reset(self):
        """Resets the serial number back to the start value"""
        self.count = self.start

