import logging
from trace import Trace
from nose2.events import Plugin


log = logging.getLogger('nose2.plugins.timertest')


class TimerTest(Plugin):
    configSection = 'timertest'
    commandLineSwitch = ('T', 'timer-test', 'Timer test')
    t = Trace(count=1, trace=0)
    r = None

    def startTestRun(self, event):
        log.info('Start Test run %s', event)
        # self.t.runfunc(event, exit=False)
        # r = self.t.results()

    def stopTestRun(self, event):
        log.info('Stop Test run %s', event)
        # r = self.t.results()

    # def startTest(self, event):
    #     log.info('.')

    # def afterSummaryReport(self, event):
    #     log.info('.')

    # def beforeSummaryReport(self, event):
    #     log.info('.')
