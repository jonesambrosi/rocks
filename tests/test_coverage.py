import unittest
from rocks import rocks_coverage


class TestReadingStructures(unittest.TestCase):
    """Reading
    """

    def test_when_compile_code_return_lines_pass(self):

        data = rocks_coverage.check_code("")

        assert data is not None
