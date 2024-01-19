"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    Attributes
    -------------
    start: int
        serial number to start with
    """

    def __init__(self, start):
        self.start = start
        self.orig_num = start

    def __repr__(self):
        return f"start={self.start}"

    def generate(self):
        """Class method which will increment to next serial number and return"""
        self.start += 1
        return self.start
    
    def reset(self):
        """Reset start number back to initial number passed in"""
        self.start = self.orig_num


