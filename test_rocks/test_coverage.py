import unittest
from class_a import A


class TestSimple(unittest.TestCase):
    """Simple test coverage"""

    def test_pass(self):
        assert True

    # def test_fail(self):
    #     assert False

    # def test_fail_2(self):
    #     assert 2 == 1

    def test_init(self):
        a = A()

        assert a.return_true()

    def test_sleeping_half_second(self):
        a = A()
        a.sleeping_half_second()

        assert True

    def test_sleeping(self):
        a = A()
        a.sleeping()

        assert True

    def test_sleeping_more_one_seconds(self):
        a = A()
        a.sleeping_more_one_seconds()

        assert True

    # def test_exception(self):
    #     a = A()

    #     assert a.raise_exc("DDD")

    #     return

    #     # Check code not reached in coverage
    #     d = 1 + 2 + 3
