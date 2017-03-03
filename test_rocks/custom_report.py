import logging
from unittest import TestResult

logger = logging.getLogger(__name__)


class CustomTestReport(TestResult):

    def __init__(self, change_callback=None):
        super(CustomTestReport, self).__init__()
        logger.warning('__init__')
        self.running = False
        self.change_callback = change_callback
        self.success = 0

    def startTest(self, test):
        super(CustomTestReport, self).startTest(test)
        logger.warning('startTest')
        self.running = True
        if self.change_callback:
            self.change_callback({
                "errors": len(self.errors),
                "failures": len(self.failures),
                "skipped": len(self.skipped),
                "expectedFailures": len(self.expectedFailures),
                "unexpectedSuccesses": len(self.unexpectedSuccesses),
                "testsRun": self.testsRun,
                "success": self.success
            })

    def stopTest(self, test):
        super(CustomTestReport, self).stopTest(test)
        logger.warning("stopTest %s", test)
        self.running = False

    def startTestRun(self):
        super(CustomTestReport, self).startTestRun()
        logger.warning("startTestRun")
        self.running = True

    def stopTestRun(self):
        super(CustomTestReport, self).stopTestRun()
        logger.warning("stopTestRun")
        self.running = False

    def addError(self, test, err):
        super(CustomTestReport, self).addError(test, err)
        logger.warning("[E] %s %s", test, err)

    def addFailure(self, test, err):
        super(CustomTestReport, self).addFailure(test, err)
        logger.warning("[F] %s %s", test, err)

    def addSuccess(self, test):
        super(CustomTestReport, self).addSuccess(test)
        logger.warning("[S] %s", test)
        self.success += 1

    def addSkip(self, test, reason):
        super(CustomTestReport, self).addSkip(test, reason)
        logger.warning("[s] %s %s", test, reason)

    def addExpectedFailure(self, test, err):
        super(CustomTestReport, self).addExpectedFailure(test, err)
        logger.warning("[EF] %s %s", test, err)

    def addUnexpectedSuccess(self, test):
        super(CustomTestReport, self).addUnexpectedSuccess(test)
        logger.warning("[US] %s", test)

    def addSubTest(self, test, subtest, outcome):
        super(CustomTestReport, self).addSubTest(test, subtest, outcome)
        logger.warning("[ST] %s %s %s", test, subtest, outcome)
