# Hannif Roast Generator (Tkinter)

Small desktop app that generates fictional, light-hearted roasts for a fictional man named `Hannif`.

Files
- `hannif_app.py` — main application (GUI + `--console` mode)

Requirements
- Python 3.8+ (Tkinter included in standard library on Windows)

Run (GUI)

```powershell
python "c:\Users\fatma\code attempts\New folder\hannif_app.py"
```

Run (console smoke-test)

```powershell
python "c:\Users\fatma\code attempts\New folder\hannif_app.py" --console
```

Notes
- The program intentionally generates fictional, playful roasts for `Hannif` and avoids real-person harassment.
- Keyboard shortcuts in the GUI: Ctrl+1, Ctrl+2, Ctrl+3 for the three roast buttons.

Building an executable (Windows)

1. Make sure Python is installed and available on your PATH, or edit `build_exe.ps1` to set the full path to your `python.exe`.
2. From PowerShell in the project folder, run:

```powershell
.
\build_exe.ps1
```

This will install `PyInstaller` (from `requirements.txt`) and produce a single-file windowed executable named `HannifRoast.exe` in the `dist\` folder.

