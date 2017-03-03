import time


class A(object):

    def __init__(self):
        self.value = "Some Value"

    def return_true(self):
        return True

    def raise_exc(self, val):

        if val == "TDD":
            return True

        raise ValueError(val)

    def repeat(self):
        return 1

    def sleeping_half_second(self):
        time.sleep(0.5)  # Warning running, show extra info warning

    def sleeping(self):
        time.sleep(1)  # Long running, show extra info slow

    def sleeping_more_one_seconds(self):
        # Long running greater than 1 seconds, show extra info slower
        time.sleep(1.1)
