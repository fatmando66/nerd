# Hannif Roast Generator (Tkinter)

Small desktop app that generates fictional, light-hearted roasts for a fictional man named `Hannif`.


Warning: explicit language
---------------------------------
This program now includes stronger, fictional roasts and may contain explicit language and mild profanity. Content is fictional and not targeted at any real person. If you prefer clean output, use the `--no-profanity` flag in console mode or toggle the profanity option in the GUI.

GUI additions
---------------------------------
- Profanity toggle: a checkbox to enable or disable profanity in generated roasts.
- Copy button: copies the displayed roast to the clipboard.

Console options
---------------------------------
- `--console` — print three sample roasts and exit (existing)
- `--no-profanity` — when used with `--console`, prints cleaned versions without profanity

Building an executable (Windows)

1. Make sure Python is installed and available on your PATH, or edit `build_exe.ps1` to set the full path to your `python.exe`.
2. From PowerShell in the project folder, run:

```powershell
.\build_exe.ps1
```

This will install `PyInstaller` (from `requirements.txt`) and produce a single-file windowed executable named `HannifRoast.exe` in the `dist\` folder.
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

