import os, subprocess, tempfile, time, json, threading, urllib.request
from .binary_handler import bin_path, ensure_binary
from .completion_manager import show_ghost, clear_ghost

PORT = None
PROC = None
MANAGER_DIR = None

def start_server():
    global PROC, MANAGER_DIR, PORT
    if PROC and PROC.poll() is None:
        return
    bin = ensure_binary()
    MANAGER_DIR = tempfile.mkdtemp(prefix="codeium_") + "/codeium/manager"
    os.makedirs(MANAGER_DIR, exist_ok=True)
    # windsurf: --api_server_url https://server.codeium.com --manager_dir <dir>
    api_url = "https://server.codeium.com"
    # check key for windsurf
    for p in [os.path.expanduser("~/.config/Codeium/config.json"), os.path.expanduser("~/.codeium/config.json")]:
        if os.path.isfile(p):
            try:
                j = json.load(open(p))
                k = j.get("apiKey","") or j.get("api_key","")
                if k.startswith("sk-ws-"):
                    api_url = "https://server.windsurf.com"
                    break
            except: pass
    cmd = [bin, "--api_server_url", api_url, "--manager_dir", MANAGER_DIR]
    PROC = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # find port (windsurf: file in manager_dir)
    def find_port():
        global PORT
        for _ in range(20):
            time.sleep(0.25)
            for name in os.listdir(MANAGER_DIR):
                path = os.path.join(MANAGER_DIR, name)
                if os.path.isfile(path) and name.isdigit():
                    PORT = name
                    print(f"Codeium port {PORT}")
                    return
                # windsurf new binary: child_random_port subdir
                if os.path.isdir(path) and name.startswith("child_random_port"):
                    for sub in os.listdir(path):
                        sp = os.path.join(path, sub)
                        if os.path.isfile(sp):
                            try:
                                c = open(sp).read().strip()
                                if c.isdigit(): PORT = c
                                elif sub.isdigit(): PORT = sub
                                if PORT: return
                            except: pass
            # fallback find
            try:
                import subprocess as sp
                out = sp.check_output(f"find {MANAGER_DIR} -type f -mmin -0.1 2>/dev/null", shell=True).decode()
                for f in out.splitlines():
                    try:
                        c = open(f).read().strip()
                        if c.isdigit() and 1024 < int(c) < 65535: PORT=c; return
                    except: pass
                    if os.path.basename(f).isdigit(): PORT=os.path.basename(f); return
                except: pass
            except: pass
    threading.Thread(target=find_port, daemon=True).start()

def request completion(view):
    if not PORT:
        return
    # TODO: build document json similar to windsurf GetDocument
    pass
