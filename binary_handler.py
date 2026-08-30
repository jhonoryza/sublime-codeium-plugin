import os, platform, stat, json, urllib.request, gzip, shutil
# Port dari windsurf.vim server.vim:256 + binary_fetcher.lua
def get_bin_suffix():
    os_name = platform.system()
    arch = platform.machine()
    is_arm = arch in ("arm64","aarch64")
    if os_name == "Linux" and is_arm: return "linux_arm"
    if os_name == "Linux": return "linux_x64"
    if os_name == "Darwin" and is_arm: return "macos_arm"
    if os_name == "Darwin": return "macos_x64"
    return "windows_x64.exe"

def home_dir():
    data_home = os.getenv("XDG_DATA_HOME")
    if data_home: return os.path.join(data_home, ".codeium")
    return os.path.join(os.path.expanduser("~"), ".codeium")

def bin_path():
    sha = "37f12b83df389802b7d4e293b3e1a986aca289c0"  # v1.20.8, akan auto update via windsurf
    suffix = get_bin_suffix()
    return os.path.join(home_dir(), "bin", sha, f"language_server_{suffix}")

def ensure_binary():
    bin = bin_path()
    if os.path.isfile(bin):
        return bin
    os.makedirs(os.path.dirname(bin), exist_ok=True)
    url = f"https://github.com/Exafunction/codeium/releases/download/language-server-v1.20.8/language_server_{get_bin_suffix()}.gz"
    gz = bin + ".gz"
    print(f"Downloading Codeium {url} -> {gz}")
    urllib.request.urlretrieve(url, gz)
    with gzip.open(gz, 'rb') as f_in:
        with open(bin, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.chmod(bin, os.stat(bin).st_mode | stat.S_IEXEC)
    os.remove(gz)
    return bin
