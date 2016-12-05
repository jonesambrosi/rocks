import sublime
import trace
import logging
import sys
try:
    from StringIO import StringIO as StringIO
except (ImportError, ValueError):
    from io import StringIO as StringIO


logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

tracker_out_last = StringIO()
tracker_out = StringIO()
rocks_tracker = trace.Trace(count=1, trace=1, countfuncs=0, countcallers=0, ignoremods=(
), ignoredirs=(), infile=None, outfile=tracker_out, timing=True)


class RocksChecker:
    # Todo: these aren't really views but handlers. Refactor/Rename.
    views = {}

    @staticmethod
    def add(view):
        key = RocksChecker.get_key(view)
        # try:
        #     from .git_gutter_handler import GitGutterHandler
        # except (ImportError, ValueError):
        #     from git_gutter_handler import GitGutterHandler
        # handler = RocksChecker.views[key] = GitGutterHandler(view)
        # handler.reset()
        handler = RocksChecker.views[key] = view
        return handler

    @staticmethod
    def get_key(view):
        return view.file_name()

    @staticmethod
    def has_view(view):
        key = RocksChecker.get_key(view)
        return key in RocksChecker.views

    @staticmethod
    def get_handler(view):
        if RocksChecker.has_view(view):
            key = RocksChecker.get_key(view)
            return RocksChecker.views[key]
        else:
            return RocksChecker.add(view)

    @staticmethod
    def all_lines(view):
        logger.debug("all_lines")
        chars = view.size()
        region = sublime.Region(0, chars)
        lines = view.lines(region)

        logger.debug("%s", view.substr(region))
        rocks_tracker.run(view.substr(region))

        # trace.CoverageResults.
        r = rocks_tracker.results()

        logger.debug(r)
        return range(0, len(lines))
