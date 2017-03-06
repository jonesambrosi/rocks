import logging
from datetime import datetime
from trace import Trace
from nose2.events import Plugin


log = logging.getLogger('nose2.plugins.timertest')


DIVISOR = 76


class TimerTest(Plugin):
    configSection = 'timertest'
    commandLineSwitch = ('T', 'timer-test', 'Timer test')
    t = Trace(count=1, trace=0)
    r = None

    times = []

    def startTestRun(self, event):
        log.debug('Start Test run %s', event)
        # self.t.runfunc(event, exit=False)
        # r = self.t.results()

    def stopTestRun(self, event):
        log.debug('Stop Test run %s', event)
        print("\nSummary")
        print("=" * DIVISOR)
        print("Total Time: {}".format(event.timeTaken))
        print("=" * DIVISOR + "\n")

    def startTest(self, event):
        log.debug('Start Test %s', event)
        self.times.append({
            "name": "{}".format(event.test.id()),
            "time_start": datetime.fromtimestamp(event.startTime),
            "result": event.result,
            "total_time": 0.0
        })

    def stopTest(self, event):
        log.debug('Stop Test  %s', event)
        item = [X for X in self.times if X['name'] == event.test.id()]
        if item:
            item[0]["total_time"] = (
                datetime.fromtimestamp(event.stopTime) -
                item[0]["time_start"]).total_seconds()

    def afterSummaryReport(self, event):
        from colorterm import Table, colorterm

        table = Table('Taken', 'Method',
                      column_separator=' | ',
                      header_convert=colorterm.white)
        for T in self.times:
            log.debug('%s: %s', T["name"], T["total_time"])
            table.add_row({
                'Taken': {
                    'value': '{:.7f}'.format(T["total_time"]),
                    'convert': self.color(T["total_time"]),
                    'align': 'right'
                },
                'Method': T['name']
            })

        print(table.display())
        print("\n" + "=" * DIVISOR)

    def color(self, value):
        from colorterm import colorterm
        if value <= 0.5:
            return colorterm.green
        elif 0.5 < value <= 1.0:
            return colorterm.yellow
        elif 1.0 < value:
            return colorterm.red

    # def beforeSummaryReport(self, event):
    #     log.debug('.')
