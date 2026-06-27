"""
ViduraAgent — Icon Setup Script
================================
Run this ONCE to copy the generated AI icons into docs/icons/
so they can be served by GitHub Pages.

Usage:
    python tools/setup_icons.py
"""

import os
import shutil

BRAIN_DIR = os.path.join(
    os.path.expanduser("~"),
    ".gemini", "antigravity-ide", "brain",
    "1f55fd35-d144-45cb-a46d-ede7b9c0bb07"
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
ICONS_DIR   = os.path.join(REPO_ROOT, "docs", "icons")

ICON_MAP = {
    "logo.png":       "vidura_logo_ancient_1782573366664.png",
    "stocks.png":     "icon_stocks_temple_1782573803521.png",
    "it.png":         "icon_it_yantra_1782573813458.png",
    "ai.png":         "icon_ai_surya_1782573822605.png",
    "pulse.png":      "icon_pulse_shankha_1782573833084.png",
    "horizon5.png":   "icon_5year_stupa_1782573842785.png",
    "horizon10.png":  "icon_10year_shikhara_1782573853516.png",
    "scroll.png":     "icon_scroll_lotus_1782573863282.png",
}

def main():
    os.makedirs(ICONS_DIR, exist_ok=True)
    print(f"\nCopying icons to: {ICONS_DIR}\n")
    ok = 0
    for dest_name, src_name in ICON_MAP.items():
        src  = os.path.join(BRAIN_DIR, src_name)
        dest = os.path.join(ICONS_DIR, dest_name)
        if not os.path.exists(src):
            print(f"  [MISS] {src_name} — not found in brain dir, skipping.")
            continue
        shutil.copy2(src, dest)
        size = os.path.getsize(dest)
        print(f"  [OK]   {dest_name}  ({size:,} bytes)")
        ok += 1
    print(f"\n{ok}/{len(ICON_MAP)} icons copied successfully.\n")
    if ok < len(ICON_MAP):
        print("Note: Missing icons will use SVG fallbacks in the dashboard.\n")

if __name__ == "__main__":
    main()
