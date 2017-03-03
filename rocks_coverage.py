import logging
import subprocess
import os
import unittest

log = logging.getlog()

try:
    log.debug("Import coverage")
    import coverage
except:
    log.error("Import coverage error")


def check_code(path):
    log.debug("START COVERAGE %s", path)
    ret = run_coverage_subprocess(path)
    log.debug("START COVERAGE %s", path)

    return ret


def run_coverage_subprocess(path):

    log.debug("Pass %s", path)

    cov = coverage.Coverage(data_file=path + '/.rocks',
                            auto_data=True, source=[path],
                            concurrency='multiprocessing')
    cov.start()

    list_tests = unittest.TestLoader().discover(start_dir=path)
    suite = unittest.TestSuite(tests=list_tests)

    result = unittest.TestResult()
    log.debug("Count tests: %s", suite.countTestCases())
    suite.run(result)

    log.debug('Result: %s', result)

    cov.stop()
    cov.save()

    # cov = coverage.Coverage(data_file=path + '\\.rocks', concurrency='multiprocessing')
    # cov.load()

    log.debug("Get data %s", path)

    return cov


# def tracer_coverage(path):
#     import unittest
#     import trace'
#     # from os.path import dirname, abspath
#     from collections import defaultdict
#     # from re import compile, match

#     # eoc = compile(r'^\s*# end of coverage')

#     t = trace.Trace(count=1, trace=0)
#     t.runfunc(unittest.main, exit=False)
#     r = t.results()

#     linecount = defaultdict(int)
#     for line in r.counts:
#         if line[0] == __file__:
#             linecount[line[1]] = r.counts[line]

#     with open(__file__) as f:
#         for linenumber, line in enumerate(f, start=1):
#             # if eoc.match(line):
#             #     break
#             print("%02d %s" % (linecount[linenumber], line), end='')
