import sublime, sublime_plugin
from .server import start_server, request as server_request
from .completion_manager import clear_ghost

class CodeiumListener(sublime_plugin.ViewEventListener):
    @classmethod
    def is_applicable(cls, settings):
        return True

    def on_modified_async(self):
        # debounce like windsurf 75ms
        sublime.set_timeout_async(lambda: self.trigger(), 75)

    def on_selection_modified_async(self):
        pass

    def trigger(self):
        if not self.view.settings().get("codeium_enabled", True):
            return
        # TODO: call server.request
        pass

    def on_post_text_command(self, command_name, args):
        if command_name in ("hide_auto_complete",):
            clear_ghost(self.view)
