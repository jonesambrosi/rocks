import sublime
# import trace
import logging
# import sys
import os
# try:
#     from StringIO import StringIO as StringIO
# except (ImportError, ValueError):
#     from io import StringIO as StringIO
try:
    from .rocks_coverage import check_code
except (ImportError, ValueError):
    from rocks.rocks.rocks_coverage import check_code

print("check_code", check_code)
logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

# tracker_out_last = StringIO()
# tracker_out = StringIO()
# rocks_tracker = trace.Trace(count=1, trace=1, countfuncs=0,
#                             countcallers=0, ignoremods=(), ignoredirs=(),
#                             infile=None, outfile=tracker_out, timing=True)


class RocksChecker:
    # Todo: these aren't really views but handlers. Refactor/Rename.
    views = {}
    coverage = None

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
    def get_coverage(view):
        logger.debug("Get Coverage: %s", view)
        path = os.path.dirname(view.file_name())
        logger.debug("Path: %s", path)
        data = check_code(path)
        logger.debug("Data: %s", data)
        RocksChecker.coverage = data
        logger.debug("RocksChecker.coverage: %s", RocksChecker.coverage)

    @staticmethod
    def all_lines(view):
        if view.file_name() is None:
            return None

        if RocksChecker.coverage is None:
            RocksChecker.get_coverage(view)

        logger.debug("all_lines")

        chars = view.size()
        region = sublime.Region(0, chars)
        lines = view.lines(region)

        # logger.debug("%s", view.substr(region))
        # rocks_tracker.run(view.substr(region))

        logger.debug("file_name analysis2: %s", view.file_name())
        r = RocksChecker.coverage.analysis2(view.file_name())

        logger.debug(r)

        return range(0, len(lines))
