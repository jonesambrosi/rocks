import sublime
import sublime_plugin

import os
import logging
import sys

try:
    from .rocks_checker import RocksChecker
except (ImportError, ValueError):
    from rocks_checker import RocksChecker


ST3 = int(sublime.version()) >= 3000

LOOP_RUNNING = False

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


def plugin_loaded() -> None:
    """Called directly from sublime on plugin load
    """
    global settings
    settings = sublime.load_settings('Rocks.sublime-settings')
    # ViewCollection.compare_against = settings.get('compare_against', 'HEAD')

    if not LOOP_RUNNING:
        print("unloop")


def plugin_unloaded() -> None:
    """Called directly from sublime on plugin unload
    """
    print("unload")
    if LOOP_RUNNING:
        print("Loop")


def change_position_view(view):
    pt = view.text_point(0, 3)
    view.sel().clear()
    view.sel().add(sublime.Region(pt))

    view.show(pt)


class RocksWindowCommand(sublime_plugin.WindowCommand):
    region_names = ['tracked', 'unverified',
                    'untracked', 'success', 'errro']

    def run(self, force_refresh=False):
        logger.info('<<< RocksWindowCommand')
        # self.view = self.window.active_view()
        logger.info(self.view)
        if not self.view:
            # View is not ready yet, try again later.
            sublime.set_timeout(self.run, 1)
            return

        self.clear_all()
        logger.info('<<< RocksWindowCommand')

    def clear_all(self):
        for region_name in self.region_names:
            self.view.erase_regions('rocks_%s' % region_name)

    def lines_to_regions(self, lines):
        regions = []
        for line in lines:
            logger.debug("%s %s", line, line.__class__)
            position = self.view.text_point(line, 0)
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
        # if ST3 and self.show_in_minimap:
        #     flags = sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE
        # else:
        #     flags = sublime.HIDDEN
        flags = sublime.HIDDEN
        self.view.add_regions('rocks_%s' % event, regions, scope, icon, flags)


class RocksCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # self.view.get_settings(self.view, 'rocks_on')
        # self.view.insert(edit, 0, "Hello, World!")
        logger.debug('<<< RocksCommand')
        logger.debug(self.view)
        # self.view = self.active_view()
        if not self.view:
            # View is not ready yet, try again later.
            sublime.set_timeout(self.run, 1)
            return

        modified = RocksChecker.all_lines(self.view)
        logger.debug("modified %s", modified)
        self.bind_icons('untracked', modified)
        self.show_in_minimap = settings.get('show_in_minimap', True)

    def clear_all(self):
        for region_name in self.region_names:
            self.view.erase_regions('rocks_%s' % region_name)

    def lines_to_regions(self, lines):
        regions = []
        for line in lines:
            logger.debug("%s %s", line, line.__class__)
            position = self.view.text_point(line, 0)
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
        # if ST3 and self.show_in_minimap:
        #     flags = sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE
        # else:
        #     flags = sublime.HIDDEN
        flags = sublime.HIDDEN
        self.view.add_regions('rocks_%s' % event, regions, scope, icon, flags)


class BackgroundChecker(sublime_plugin.EventListener):
    """Background linter, can be turned off via plugin settings
    """

    def on_modified(self, view: sublime.View) -> None:
        logger.debug('.')
        if 'py' in view.settings().get('syntax'):
            logger.debug('python')
            # self.run_linter(view)
