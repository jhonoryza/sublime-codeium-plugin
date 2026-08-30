# sublime-codeium

Codeium/Windsurf for Sublime Text 4 — port of [windsurf.vim](https://github.com/Exafunction/windsurf.vim) (Vimscript `job` + `curl` http `GetCompletions`) to Sublime Text Python `phantom` + `language_server`.

> Auto-download `language_server` to `~/.local/share/.codeium/bin/<sha>/` (Mac/Linux/Windows).

## Install

```bash
git clone https://github.com/jhonoryza/sublime-codeium-plugin.git ~/Library/Application\ Support/Sublime\ Text/Packages/Codeium
# Linux: ~/.config/sublime-text/Packages/Codeium
```

Or via Package Control: `Install Package` → `Codeium` (after publish).

## Auth

```bash
mkdir -p ~/.config/Codeium
echo '{"apiKey":"sk-ws-..."}' > ~/.config/Codeium/config.json  # Linux
mkdir -p ~/.codeium && echo '{"apiKey":"sk-..."}' > ~/.codeium/config.json  # Mac
```

## Keymap

`Tab` accept, `Esc` clear, `Ctrl+Right` accept word — via `Default.sublime-keymap`.

## Status

WIP — scaffold from `sublime-supermaven` + `windsurf.vim/server.vim`.
