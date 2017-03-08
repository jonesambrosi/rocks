import logging
import unittest
import config

from custom_report import CustomTestReport

logger = logging.getLogger(__name__)


def change(info):
    print(info)

test = unittest.defaultTestLoader

res = test.discover('.')
result = CustomTestReport(change)
res.run(result)

logger.debug(res)
logger.debug(result)
logger.debug(result.errors)
logger.debug(result.failures)
logger.debug(result.failfast)
logger.debug(result.skipped)
logger.debug(result.skipped)
