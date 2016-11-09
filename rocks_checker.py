import sublime


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
        chars = view.size()
        region = sublime.Region(0, chars)
        lines = view.lines(region)
        return lines
