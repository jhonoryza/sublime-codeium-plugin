import sublime
# Port dari windsurf.vim s:RenderCurrentCompletion + supermaven completion_preview
PHANTOM_KEY = "codeium"
HLGROUP = "CodeiumSuggestion"

def show_ghost(view, text):
    clear_ghost(view)
    if not text:
        return
    parts = text.split("\n")
    first = parts[0]
    # inline ghost
    view.add_phantom(PHANTOM_KEY, view.sel()[0], first, sublime.LAYOUT_INLINE)
    # block ghost
    for line in parts[1:]:
        if line:
            view.add_phantom(PHANTOM_KEY, view.sel()[0], line, sublime.LAYOUT_BELOW)

def clear_ghost(view):
    view.erase_phantoms(PHANTOM_KEY)

def accept(view, edit):
    # TODO: apply ghost text via view.insert
    pass
