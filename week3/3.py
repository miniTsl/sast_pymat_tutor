class MomentumRunner:
    def __init__(self):
        self.mean = 0
        self.var = 0
        # you may add some other things
        # ...

    # implement some other methods to meet the requirements
    def some_other_methods(self, something):
        pass


if __name__ == "__main__":
    m1 = MomentumRunner()
    m2 = MomentumRunner()

    # return 3.5 and 2.916667
    mean, var = m1(1, 2, 3, 4, 5, 6)
    # return 4 and 4
    mean, var = m1(7)

    # return 8 and 0
    mean, var = m2(8)

    m = m1 + m2
    # return 5 and 6.66667
    mean, var = m(9)
