import unittest
from rocks.process import tracer


class TestTraceFile(unittest.TestCase):
    """Tracing data for times and execution
    """

    def test_when_compile_code_return_lines_pass(self):

        tr = tracer.trace_code('/mnt/e/some_code', code="""
import trac_check_code_tracer
a = trac_check_code_tracer.A()
for x in range(10):
    a.repeat()

a.sleeping()
""")

        assert tr is not None
        print(tr)
