import logging
import sys
from io import BytesIO

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.checkcode')
stream = BytesIO()
sys.stderr = stream


class CheckCode(Plugin):
    configSection = 'checkcode'
    commandLineSwitch = (None, 'check-code', 'Say hello!')

    def startTestRun(self, event):
        log.info('Start Test run %s', event)

    def startTest(self, event):
        log.info('Start')

    def afterSummaryReport(self, event):
        log.info('[Coverage] %s', event)
        log.info('[Output] %s', stream.getvalue().decode('UTF-8'))

    def beforeSummaryReport(self, event):
        log.info('[Coverage] 1 %s', event)
        log.info('[Coverage] 2 %s', event.stopTestEvent)
        log.info('[Coverage] 3 %s', event.stopTestEvent.result)
