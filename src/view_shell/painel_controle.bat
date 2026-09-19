@echo off
chcp 65001 >nul
set SCRIPT_DIR=%~dp0
set SCRIPT=%SCRIPT_DIR%painel_controle.ps1

where wt >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    start "" wt powershell.exe -NoExit -File "%SCRIPT%"
) else (
    start "" powershell.exe -ExecutionPolicy Bypass -File "%SCRIPT%"
)
