import logging
import subprocess
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s %(name)s[%(lineno)d]: %(message)s",
)

logger = logging.getLogger(__name__)


def check_code(path):

    logger.debug("************* START COVERAGE ****************")
    ret = run_coverage_subprocess(path)
    logger.debug("************* STOP COVERAGE ****************")

    return ret


def run_coverage_subprocess(path):
    logger.debug("Pass")
    import coverage
    # try:

    # except Exception as ex:
    #     logger.debug("Import Error import coverage: %s", ex)

    # try:
    #     import rocks.coverage
    # except Exception as ex:
    #     logger.debug("Import Error coverage: %s", ex)

    # try:
    #     import coverage
    # except Exception as ex:
    #     logger.debug("Import Error coverage: %s", ex)

    p = subprocess.Popen(
        ["python", "-m", "unittest", "discover"],
        cwd=path,
        stdout=subprocess.PIPE
    )
    out, err = p.communicate()
    # p.communicate()
    p.wait()
    logger.debug("Subprocess %s %s", out, err)

    cov = coverage.Coverage(data_file=path + '/.coverage',
                            source=path + '/',
                            concurrency="multiprocessing")

    cov.load()
    cov.combine()

    logger.debug("Get data")
    return cov.get_data()
