import sublime, sublime_plugin
from .server import start_server
from .completion_manager import clear_ghost, show_ghost

def plugin_loaded():
    start_server()
    print("Codeium Sublime loaded")

class CodeiumAcceptCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # TODO: apply ghost text
        pass

class CodeiumClearCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        from .completion_manager import clear_ghost
        clear_ghost(self.view)

class CodeiumStatusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        from .server import PORT
        sublime.message_dialog(f"Codeium port: {PORT}")

