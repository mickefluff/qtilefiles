from typing import Optional
from libqtile.widget.textbox import TextBox

def lower_left_triangle():
    return TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background="#282a36",
        foreground="#f8f8f8")

