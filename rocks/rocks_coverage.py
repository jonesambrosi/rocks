import logging
import subprocess
import os
from multiprocessing import Process
# from nose2 import discover

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s %(name)s[%(lineno)d]: %(message)s",
)

logger = logging.getLogger(__name__)


def check_code(path):

    logger.debug("************* START COVERAGE ****************")
    ret = run_coverage_subprocess(path)
    logger.debug("************* STOP COVERAGE ****************")

    return [ret]


def run_coverage_subprocess(path):
    import coverage
    p = subprocess.Popen(
        ["python", "-m", "unittest", "discover"],
        cwd=path
    )
    p.communicate()
    p.wait()

    cov = coverage.Coverage(data_file=path + '/.coverage',
                            source=path + '/',
                            concurrency="multiprocessing")
    cov.load()
    cov.combine()

    return cov
