<#
PowerShell build script to create a single-file windowed executable using PyInstaller.

Usage (PowerShell):
  - Open an elevated or normal PowerShell where Python is available in PATH.
  - Run: `.uild_exe.ps1`

This script will:
  1. Optionally create a virtual environment (commented out by default).
  2. Install requirements from `requirements.txt`.
  3. Run PyInstaller to create a one-file, windowed executable named `HannifRoast.exe`.

Adjust the `$PythonExe` variable if you need to point to a specific python executable.
#>

Set-StrictMode -Version Latest

# Path to the script and files
$Root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Script = Join-Path $Root 'hannif_app.py'
$DistDir = Join-Path $Root 'dist'

# Optionally set this to the full path of the python.exe you want to use.
# Leave empty to use 'python' from PATH.
$PythonExe = 'python'

Write-Host "Using Python executable: $PythonExe"

if (-not (Test-Path $Script)) {
    Write-Error "Can't find $Script. Run this script from the project folder where hannif_app.py exists."
    exit 1
}

Write-Host "Installing requirements (PyInstaller)..."
& $PythonExe -m pip install --upgrade pip
& $PythonExe -m pip install -r (Join-Path $Root 'requirements.txt')

Write-Host "Running PyInstaller to build a single-file windowed executable..."

# Remove old build artifacts if present
if (Test-Path (Join-Path $Root 'build')) { Remove-Item -Recurse -Force (Join-Path $Root 'build') }
if (Test-Path $DistDir) { Remove-Item -Recurse -Force $DistDir }
if (Test-Path (Join-Path $Root 'HannifRoast.spec')) { Remove-Item -Force (Join-Path $Root 'HannifRoast.spec') }

$ExeName = 'HannifRoast'

# PyInstaller options:
# --onefile : produce a single-file executable
# --windowed : no console window (useful for GUI apps); remove if you want a console
# --name : name of the executable

& $PythonExe -m PyInstaller --onefile --windowed --name $ExeName $Script

if ($LASTEXITCODE -ne 0) {
    Write-Error "PyInstaller failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}

Write-Host "Build complete. Executable is at: $(Join-Path $DistDir ($ExeName + '.exe'))"
