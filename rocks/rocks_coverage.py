import logging
import sys
import coverage
import subprocess
import os
from nose2 import discover


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s %(name)s[%(lineno)d]: %(message)s",
)

logger = logging.getLogger(__name__)


def check_code(path):

    logger.debug("************* START COVERAGE ****************")

    # ret = run_coverage('/mnt/e/test_rocks')
    ret = run_coverage_subprocess(path)

    # cov.html_report()
    # print("Feito", ret)
    logger.debug("************* STOP COVERAGE ****************")

    return [ret]


# def run_coverage(path):

#     cov = coverage.Coverage(data_file='{}/.coverage'.format(path))
#     cov.start()

#     # this is where your python file exists
#     sys.path.append(path)

#     args = [
#         "{}/test_me.py".format(path),
#         "-s", path,
#         # "--top-level-dir",
#         # "/mnt/e/test_rocks/",
#         "--verbose"]

#     discover(argv=args)
#     # a = 1
#     # if a == 1:
#     #     print(1)

#     cov.stop()
#     cov.save()
#     # ret = cov.analysis2("test_me.TestA.test_init")
#     ret = []

#     return ret


def run_coverage_subprocess(path):

    my_env = os.environ.copy()
    my_env["COVERAGE_PROCESS_START"] = "/mnt/e/rocks/.coveragerc"

    cov = coverage.Coverage(source='/mnt/e/test_rocks', concurrency="multiprocessing")
    # coverage.process_startup()
    p = subprocess.Popen(
        ["python", "-m", "unittest", "discover"], cwd=path,
        env=my_env
    )

    p.communicate()
    cov.combine()

    return cov.get_data()


if __name__ == '__main__':
    check_code("")
