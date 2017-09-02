# -*- coding: utf8 -*-

# -----------------------------------------------------------------------------
# Author : yongchan jeon (Kris) poucotm@gmail.com
# File   : Guna.py
# Create : 2017-08-18 19:41:37
# Editor : sublime text3, tab size (4)
# -----------------------------------------------------------------------------


import sublime, sublime_plugin
from .engine import engine


ST3 = int(sublime.version()) >= 3000


def plugin_loaded():
    """ plugin_loaded """
    engine.observe_prefs()
    sublime.set_timeout_async(engine.guna_reload, 0)
    return

##  class GunaEventListener  _____________________________________

class GunaEventListener(engine.GunaEvent):
    pass

##  class GunaSetTheme  _____________________________________

class GunaSetTheme(sublime_plugin.TextCommand):

    def run(self, edit):
        try:
            prefs = sublime.load_settings("Preferences.sublime-settings")
            prefs.set('theme', 'Guna.sublime-theme')
            prefs.set('color_scheme', 'Packages/Guna/Guna.tmTheme')
            sublime.save_settings("Preferences.sublime-settings")
        except Exception as e:
            print ('Guna : ' + str(e))
            traceback.print_exc()
            return
