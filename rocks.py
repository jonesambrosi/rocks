try:
    import sublime
    import sublime_plugin

    ST3 = int(sublime.version()) >= 3000
except:
    pass

import os
import logging


try:
    from rocks.process.checker import RocksChecker
except (ImportError, ValueError):
    pass


LOOP_RUNNING = False

logger = logging.getLogger()


def plugin_loaded():
    """Called directly from sublime on plugin load
    """
    global settings
    settings = sublime.load_settings('Rocks.sublime-settings')

    if not LOOP_RUNNING:
        print("unloop")


def plugin_unloaded():
    """Called directly from sublime on plugin unload
    """
    if LOOP_RUNNING:
        print("Loop")


def change_position_view(view):
    pt = view.text_point(0, 3)
    view.sel().clear()
    view.sel().add(sublime.Region(pt))

    view.show(pt)


class RocksCommand(sublime_plugin.TextCommand):
    region_names = ['tracked', 'untracked', 'skipped']

    def run(self, edit):
        on_view = self.view
        logger.debug('<<< RocksCommand')
        logger.debug(on_view)
        # self.view = self.active_view()
        if not on_view:
            # View is not ready yet, try again later.
            sublime.set_timeout(self.run, 1)
            return

        self.show_in_minimap = settings.get('show_in_minimap', True)

        tracked, skipped, untracked = RocksChecker.all_lines(on_view)
        self._clear_all()
        logger.debug("tracked", tracked)
        logger.debug("skipped", skipped)
        logger.debug("untracked", untracked)
        self.bind_icons('skipped', skipped)
        self.bind_icons('untracked', untracked)
        self.bind_icons('tracked', tracked)

    def _clear_all(self):
        for region_name in self.region_names:
            self.view.erase_regions('rocks_%s' % region_name)

    def lines_to_regions(self, lines):
        regions = []
        for line in lines:
            logger.debug("%s %s", line, line.__class__)
            position = self.view.text_point(line - 1, 0)
            region = sublime.Region(position, position + 1)
            # if not self.is_region_protected(region):
            #     regions.append(region)
            regions.append(region)
        logger.debug("regions %s", regions)
        return regions

    def plugin_dir(self):
        path = os.path.realpath(__file__)
        root = os.path.split(os.path.dirname(path))[1]
        return os.path.splitext(root)[0]

    def icon_path(self, icon_name):
        if int(sublime.version()) < 3014:
            path = '../Rocks'
            extn = ''
        else:
            path = 'Packages/' + self.plugin_dir()
            extn = '.png'

        return "/".join([path, 'icons', icon_name + extn])

    def bind_icons(self, event, lines):
        logger.debug("lines %s", lines)
        regions = self.lines_to_regions(lines)
        event_scope = event
        scope = 'markup.%s.rocks' % event_scope
        icon = self.icon_path(event)
        if ST3 and self.show_in_minimap:
            flags = sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE
        else:
            flags = sublime.HIDDEN
        logger.debug(icon)
        logger.debug(flags)
        self.view.add_regions('rocks_%s' % event, regions, scope, icon, flags)


class BackgroundChecker(sublime_plugin.EventListener):
    """Background linter, can be turned off via plugin settings
    """

    def on_load(self, view):
        if 'source.python' not in view.scope_name(0):
            return

        view.run_command('rocks')  # , on_view=view)

    def on_modified(self, view: sublime.View) -> None:
        pass

        # Revalidate all impacted points
    #     if 'source.python' not in view.scope_name(0):
    #         return

    #     view.run_command('rocks')  # , on_view=view)

    def on_post_save(self, view: sublime.View) -> None:
        logger.debug(sublime.View)
        if 'source.python' not in view.scope_name(0):
            return

        view.run_command('rocks')  # , on_view=view)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s "
                      "[%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "./logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
