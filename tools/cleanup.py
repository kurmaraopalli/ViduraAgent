"""
ViduraAgent — Project Cleanup Script
====================================
Cleans up older unused files and folders (e.g. frontend/ directory
and temporary root files) to keep the repository structure pristine.

Usage:
    python tools/cleanup.py
"""

import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)

TARGETS = [
    # (Type, Relative Path)
    ("dir", "frontend"),
    ("file", ".github.workflows.daily_update.yml.txt"),
]

def main():
    print("\n🧹 Cleaning up unused files and folders...\n")
    cleaned = 0
    for target_type, rel_path in TARGETS:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(full_path):
            print(f"  [SKIP] {rel_path} — does not exist")
            continue
        try:
            if target_type == "dir":
                shutil.rmtree(full_path)
                print(f"  [REMOVED] Directory: {rel_path}")
            elif target_type == "file":
                os.remove(full_path)
                print(f"  [REMOVED] File:      {rel_path}")
            cleaned += 1
        except Exception as exc:
            print(f"  [ERROR]   Could not remove {rel_path}: {exc}")
    print(f"\n✨ Cleanup completed. {cleaned} items removed.\n")

if __name__ == "__main__":
    main()
