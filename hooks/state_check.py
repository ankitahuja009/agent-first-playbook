"""Session hook for agent-first repos.

start: print branch, uncommitted files and the last STATE entry, so a new
       session begins from facts.
stop:  warn if files changed but docs/STATE.md did not.

Standard library only. Usage: python hooks/state_check.py start|stop
"""

import subprocess
import sys
from pathlib import Path

STATE = Path("docs/STATE.md")


def git(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def changed_files():
    # -uall lists files inside new folders, so a new docs/STATE.md is seen by name
    lines = git("status", "--porcelain", "-uall").splitlines()
    return [line[3:] for line in lines if line.strip()]


def last_entry():
    if not STATE.exists():
        return None
    headings = [l for l in STATE.read_text(encoding="utf-8").splitlines() if l.startswith("### ")]
    return headings[-1][4:] if headings else None


def start():
    branch = git("branch", "--show-current") or "(no git)"
    files = changed_files()
    print(f"Branch: {branch}  |  uncommitted files: {len(files)}")
    entry = last_entry()
    print(f"Last STATE entry: {entry}" if entry else "No docs/STATE.md entry yet. Add one when you ship.")


def stop():
    files = changed_files()
    if files and str(STATE).replace("\\", "/") not in [f.replace("\\", "/") for f in files]:
        print(f"{len(files)} file(s) changed but {STATE} was not updated. Append a dated entry before you finish.")
        return 1
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "start"
    if mode == "start":
        start()
    elif mode == "stop":
        sys.exit(stop())
    else:
        print("usage: state_check.py start|stop")
        sys.exit(2)
