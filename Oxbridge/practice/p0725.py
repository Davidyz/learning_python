class Fraction:
    """
    Author: Davidyz
    Date: 25, 7, 2018
    你们啊，Naive!
    """

    def __init__(self, numerator, dominator):
        self.__numerator = numerator
        self.__dominator = dominator

    def get_numerator(self):
        return self.__numerator

    def get_dominator(self):
        return self.__dominator

    def set_numerator(self, value):
        self.numerator = value

    def set_dominator(self, value):
        self.dominator = value


if __name__ == "__main__":
    F1 = Fraction(2, 5)

    try:
        print(F1.__numerator)
        print(F1.__dominator)
    except AttributeError:
        print("Private attributes!")

    print(F1.get_numerator())
    print(F1.get_dominator())
