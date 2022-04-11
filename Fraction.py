class Fraction:

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError("The numerator must be an int!")
        if not isinstance(denominator, int):
            raise TypeError("The denominator must be an int!")
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0.")
        else:
            self.numerator = numerator
            self.denominator = denominator

    def divide(self):
        return self.numerator / self.denominator

    def __str__(self):
        return str(self.numerator)+str(self.denominator)

    def __add__(self, other):
        return self.numerator + self.denominator

    def __sub__(self, other):
        return self.numerator - self.denominator

    def inverse(self):
        return self.denominator / self.numerator

