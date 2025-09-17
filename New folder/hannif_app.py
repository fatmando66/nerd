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
    "Hannif could trip over a cordless phone and still call it a 'plot twist'.",
    "Hannif's calendar has a 'maybe' column for decisions.",
    "If curiosity killed the cat, Hannif would be on the witness protection list.",
    "Hannif's idea of multitasking is blinking with both eyes at once.",
    "Hannif once tried to download a sandwich — it expired in his inbox."
]

ROASTS_TWO = [
    "Hannif's sense of direction is the reason GPS now includes sympathy messages.",
    "When Hannif whispers \"I'll start tomorrow\", tomorrow files a restraining order.",
    "Hannif's confidence outruns facts at a full sprint.",
    "Hannif could get lost in a one-room cabin and blame the furniture.",
    "Hannif's mug says 'World's Okayest Planner'."
]

ROASTS_THREE = [
    "They say practice makes perfect — Hannif says practice makes interesting stories.",
    "Hannif puts the 'pro' in 'probably not'.",
    "Hannif's advice: 'If at first you don't succeed, redefine success.'",
    "Hannif's superpower is making simple things theatrical.",
    "If overthinking burned calories, Hannif would be a fitness model."
]


def pick_random(arr: list[str]) -> str:
    return random.choice(arr)


def generate_roast_one() -> str:
    return pick_random(ROASTS_ONE)


def generate_roast_two() -> str:
    return pick_random(ROASTS_TWO)


def generate_roast_three() -> str:
    return pick_random(ROASTS_THREE)


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

        self.result_var = tk.StringVar(value="")
        result = ttk.Label(frame, textvariable=self.result_var, wraplength=480, font=(None, 11))
        result.pack(pady=(12, 0))

        # keyboard shortcuts
        self.bind('<Control-1>', lambda e: self.show_one())
        self.bind('<Control-2>', lambda e: self.show_two())
        self.bind('<Control-3>', lambda e: self.show_three())

    def show_one(self) -> None:
        self.result_var.set(generate_roast_one())

    def show_two(self) -> None:
        self.result_var.set(generate_roast_two())

    def show_three(self) -> None:
        self.result_var.set(generate_roast_three())


def run_console_mode() -> None:
    print('Sample Roast #1:', generate_roast_one())
    print('Sample Roast #2:', generate_roast_two())
    print('Sample Roast #3:', generate_roast_three())


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description='Hannif Roast Generator')
    parser.add_argument('--console', action='store_true', help='print three sample roasts and exit')
    args = parser.parse_args(argv)

    if args.console:
        run_console_mode()
        return 0

    app = HannifApp()
    app.mainloop()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
