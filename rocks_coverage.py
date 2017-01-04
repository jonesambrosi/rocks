import logging
import unittest

logger = logging.getLogger()

try:
    logger.debug("Import coverage")
    import coverage
except:
    logger.error("Import coverage error")


def check_code(path):
    logger.debug("START COVERAGE %s", path)
    ret = run_coverage_subprocess(path)
    logger.debug("START COVERAGE %s", path)

    return ret


def run_coverage_subprocess(path):

    logger.debug("Pass %s", path)

    cov = coverage.Coverage(data_file=path + '/.rocks',
                            auto_data=True, source=[path],
                            concurrency='multiprocessing')
    cov.load()
    cov.start()

    list_tests = unittest.TestLoader().discover(start_dir=path)
    suite = unittest.TestSuite(tests=list_tests)

    result = unittest.TestResult()
    logger.debug("Count tests: %s", suite.countTestCases())
    suite.run(result)

    logger.debug('Result: %s', result)

    cov.stop()
    cov.save()

    logger.debug("Get data %s", path)

    return cov

