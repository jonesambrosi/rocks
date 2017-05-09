import unittest
from process import cover


class TestReadingStructures(unittest.TestCase):
    """Reading
    """

    def test_when_compile_code_return_lines_pass(self):

        cov = cover.check_code('~/development/rocks-test')

        data = cov.get_data()

        assert data is not None
        assert data.line_counts() != {}
