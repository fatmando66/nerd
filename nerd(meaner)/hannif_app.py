#!/usr/bin/env python3
"""
Hannif Roast Generator (Tkinter)

Creates a small desktop app with three buttons. Each button generates a fictional,
light-hearted roast for a fictional man named "Hannif". The program also supports
`--console` mode to print sample outputs for testing.

Usage:
    python hannif_app.py        # run GUI
    python hannif_app.py --console  # print three sample roasts and exit
"""

from __future__ import annotations

import argparse
import random
import sys
import tkinter as tk
from tkinter import ttk


ROASTS_ONE = [
    "Hannif could trip over a cordless phone and still call it destiny, you damn genius.",
    "If common sense were gasoline, Hannif wouldn't power a damn flashlight.",
    "Hannif's idea of preparation is gluing yesterday's plans to tomorrow's nonsense.",
    "Watching Hannif think is like watching a slow-motion car crash — messy and somehow his fault.",
    "Hannif is the human version of a participation trophy: baffling and slightly embarrassing."
]

ROASTS_ONE_CLEAN = [
    "Hannif could trip over a cordless phone and still call it destiny, you genius.",
    "If common sense were gasoline, Hannif wouldn't power a small flashlight.",
    "Hannif's idea of preparation is gluing yesterday's plans to tomorrow's nonsense.",
    "Watching Hannif think is like watching a slow-motion car crash — messy and somehow his fault.",
    "Hannif is the human version of a participation trophy: baffling and slightly embarrassing."
]

ROASTS_TWO = [
    "Hannif's sense of direction is so terrible even breadcrumbs file a missing-person report.",
    "When Hannif says 'I'll handle it', the world quietly braces for impact.",
    "Hannif's confidence is impressive — a delusional billboard of 'mostly wrong'.",
    "Hannif could lose a staring contest with a doorknob and still call the knob dramatic.",
    "Hannif's planning process looks a lot like improv that's been given too much trust."
]

ROASTS_TWO_CLEAN = [
    "Hannif's sense of direction is so bad even breadcrumbs get worried.",
    "When Hannif says 'I'll handle it', people quietly make backup plans.",
    "Hannif's confidence is impressive — often mistaken, rarely helpful.",
    "Hannif could lose a staring contest with a doorknob and still call the knob dramatic.",
    "Hannif's planning process looks a lot like improv that's been given too much trust."
]

ROASTS_THREE = [
    "If bad ideas were currency, Hannif would be a filthy, bankrupt tycoon.",
    "Hannif's advice is like a broken GPS: loud, wrong, and somehow convincing.",
    "Calling Hannif a hot mess would be an insult to messes everywhere.",
    "Hannif could start a meeting and somehow make it an hour-long comedy of errors.",
    "If overthinking burned calories, Hannif would be a ripped disaster."
]

ROASTS_THREE_CLEAN = [
    "If bad ideas were currency, Hannif would be an unfortunate tycoon.",
    "Hannif's advice is like a broken GPS: loud, wrong, and somehow convincing.",
    "Calling Hannif a hot mess would be an insult to messes everywhere.",
    "Hannif could start a meeting and somehow make it an hour-long comedy of errors.",
    "If overthinking burned calories, Hannif would be a very distracted fitness enthusiast."
]


def pick_random(arr: list[str]) -> str:
    return random.choice(arr)


def generate_roast_one(use_profanity: bool = True) -> str:
    return pick_random(ROASTS_ONE if use_profanity else ROASTS_ONE_CLEAN)


def generate_roast_two(use_profanity: bool = True) -> str:
    return pick_random(ROASTS_TWO if use_profanity else ROASTS_TWO_CLEAN)


def generate_roast_three(use_profanity: bool = True) -> str:
    return pick_random(ROASTS_THREE if use_profanity else ROASTS_THREE_CLEAN)


class HannifApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Hannif Roast Generator")
        self.geometry("520x240")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill=tk.BOTH, expand=True)

        header = ttk.Label(frame, text="Hannif Roast Generator", font=(None, 16, 'bold'))
        header.pack()

        sub = ttk.Label(frame, text="Click a button to generate a fictional, light-hearted roast for Hannif.")
        sub.pack(pady=(4, 12))

        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        btn1 = ttk.Button(btn_frame, text="Roast #1", command=self.show_one)
        btn1.grid(row=0, column=0, padx=6)

        btn2 = ttk.Button(btn_frame, text="Roast #2", command=self.show_two)
        btn2.grid(row=0, column=1, padx=6)

        btn3 = ttk.Button(btn_frame, text="Roast #3", command=self.show_three)
        btn3.grid(row=0, column=2, padx=6)

        copy_btn = ttk.Button(btn_frame, text="Copy", command=self.copy_result)
        copy_btn.grid(row=0, column=3, padx=6)

        # profanity toggle
        self.profanity_var = tk.BooleanVar(value=True)
        prof_chk = ttk.Checkbutton(frame, text="Enable profanity", variable=self.profanity_var)
        prof_chk.pack(pady=(8, 0))

        self.result_var = tk.StringVar(value="")
        result = ttk.Label(frame, textvariable=self.result_var, wraplength=480, font=(None, 11))
        result.pack(pady=(12, 0))

        # keyboard shortcuts
        self.bind('<Control-1>', lambda e: self.show_one())
        self.bind('<Control-2>', lambda e: self.show_two())
        self.bind('<Control-3>', lambda e: self.show_three())
        self.bind('<Control-c>', lambda e: self.copy_result())

    def show_one(self) -> None:
        self.result_var.set(generate_roast_one(use_profanity=self.profanity_var.get()))

    def show_two(self) -> None:
        self.result_var.set(generate_roast_two(use_profanity=self.profanity_var.get()))

    def show_three(self) -> None:
        self.result_var.set(generate_roast_three(use_profanity=self.profanity_var.get()))

    def copy_result(self) -> None:
        try:
            text = self.result_var.get()
            self.clipboard_clear()
            self.clipboard_append(text)
        except Exception:
            # ignore clipboard errors silently
            pass


def run_console_mode(use_profanity: bool = True) -> None:
    print('Sample Roast #1:', generate_roast_one(use_profanity=use_profanity))
    print('Sample Roast #2:', generate_roast_two(use_profanity=use_profanity))
    print('Sample Roast #3:', generate_roast_three(use_profanity=use_profanity))


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description='Hannif Roast Generator')
    parser.add_argument('--console', action='store_true', help='print three sample roasts and exit')
    parser.add_argument('--no-profanity', action='store_true', help='print non-profane variants')
    args = parser.parse_args(argv)

    if args.console:
        run_console_mode(use_profanity=not args.no_profanity)
        return 0

    app = HannifApp()
    app.mainloop()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
