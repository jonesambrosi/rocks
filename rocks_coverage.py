import logging
import subprocess
import os

logger = logging.getLogger()

try:
    import coverage.st3_windows_x64.coverage
    logger.debug("************* ACHOU ****************")
    print("************* ACHOU ****************")
except:
    import coverage
    logger.debug("************* NAO ****************")
    print("************* NAO ****************")


def check_code(path):
    logger.debug("************* START COVERAGE %s ****************", path)
    print("************* START COVERAGE ****************", path)
    ret = run_coverage_subprocess(path)
    logger.debug("************* STOP COVERAGE %s ****************", path)
    print("************* STOP COVERAGE ****************", path)

    return ret


def run_coverage(path):

    logger.debug("Pass %s", path)
    process_env = os.environ.copy()
    process_env["COVERAGE_PROCESS_START"] = path + '\\.coveragerc'

    p = subprocess.Popen(
        # coverage run --source=/mnt/e/test_rocks/ -m unittest discover
        ["python", "-m", "unittest", "discover"],
        cwd=path,
        env=process_env,
        stdout=subprocess.PIPE
    )
    # out, err = p.communicate()
    # logger.debug("Subprocess %s %s", out, err)
    p.wait()
    cov = coverage.Coverage(data_file=path + '\\.coverage',
                            source=path + '\\',
                            concurrency="multiprocessing")
    cov.load()
    cov.combine()

    logger.debug("Get data %s", path)
    print("Get data", path)
    return cov.get_data()


def run_coverage_subprocess(path):

    logger.debug("Pass %s", path)
    process_env = os.environ.copy()
    # process_env["COVERAGE_PROCESS_START"] = path + '\\.coveragerc'
    process_env["COVERAGE_FILE"] = path + '\\.rocks'

    # ["python", "-m", "unittest", "discover"],
    p = subprocess.Popen(
        ["coverage", "run", "--source=%s" %
            path, "-m", "unittest", "discover"],
        cwd=path,
        env=process_env,
        stdout=subprocess.PIPE
    )
    p.wait()
    out, err = p.communicate()
    logger.debug("Subprocess %s %s", out, err)
    print("Subprocess %s %s", out, err)
    cov = coverage.Coverage(data_file=path + '\\.rocks',
                            source=path,
                            concurrency="multiprocessing")
    cov.load()
    cov.combine()

    logger.debug("Get data %s", path)
    print("Get data", path)
    return cov.get_data()


# def tracer_coverage(path):
#     import unittest
#     import trace
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
