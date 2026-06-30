@echo off
echo ===================================================
echo Copying ViduraAgent Generated Icons into docs/icons/
echo ===================================================
echo.

mkdir "docs\icons" 2>nul

copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\vidura_logo_ancient_1782573366664.png" "docs\icons\logo.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_stocks_temple_1782573803521.png" "docs\icons\stocks.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_it_yantra_1782573813458.png" "docs\icons\it.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_ai_surya_1782573822605.png" "docs\icons\ai.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_pulse_shankha_1782573833084.png" "docs\icons\pulse.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_5year_stupa_1782573842785.png" "docs\icons\horizon5.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_10year_shikhara_1782573853516.png" "docs\icons\horizon10.png"
copy /y "%USERPROFILE%\.gemini\antigravity-ide\brain\1f55fd35-d144-45cb-a46d-ede7b9c0bb07\icon_scroll_lotus_1782573863282.png" "docs\icons\scroll.png"

echo.
echo ===================================================
echo Done! All icons copied successfully.
echo ===================================================
echo.
pause
