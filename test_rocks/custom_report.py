import logging
from unittest import TestResult

logger = logging.getLogger(__name__)


class CustomTestReport(TestResult):

    def __init__(self, change_callback=None):
        super(CustomTestReport, self).__init__()
        logger.debug('__init__')
        self.running = False
        self.change_callback = change_callback
        self.success = 0

    def startTest(self, test):
        super(CustomTestReport, self).startTest(test)
        logger.debug('startTest')
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
        logger.debug("stopTest %s", test)
        self.running = False

    def startTestRun(self):
        super(CustomTestReport, self).startTestRun()
        logger.debug("startTestRun")
        self.running = True

    def stopTestRun(self):
        super(CustomTestReport, self).stopTestRun()
        logger.debug("stopTestRun")
        self.running = False

    def addError(self, test, err):
        super(CustomTestReport, self).addError(test, err)
        logger.debug("[E] %s %s", test, err)

    def addFailure(self, test, err):
        super(CustomTestReport, self).addFailure(test, err)
        logger.debug("[F] %s %s", test, err)

    def addSuccess(self, test):
        super(CustomTestReport, self).addSuccess(test)
        logger.debug("[S] %s", test)
        self.success += 1

    def addSkip(self, test, reason):
        super(CustomTestReport, self).addSkip(test, reason)
        logger.debug("[s] %s %s", test, reason)

    def addExpectedFailure(self, test, err):
        super(CustomTestReport, self).addExpectedFailure(test, err)
        logger.debug("[EF] %s %s", test, err)

    def addUnexpectedSuccess(self, test):
        super(CustomTestReport, self).addUnexpectedSuccess(test)
        logger.debug("[US] %s", test)

    def addSubTest(self, test, subtest, outcome):
        super(CustomTestReport, self).addSubTest(test, subtest, outcome)
        logger.debug("[ST] %s %s %s", test, subtest, outcome)
